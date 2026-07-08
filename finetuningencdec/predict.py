"""
Run the fine-tuned LED summarizer locally on custom input.

Just edit ARTICLE_TEXT below with the text you want to summarize, then run:
    python predict.py
"""

import torch
from transformers import AutoTokenizer, LEDForConditionalGeneration

MODEL_DIR = "led_bbc_finetuned"
MAX_INPUT_LENGTH = 1024
MAX_NEW_TOKENS = 256

# ---------------------------------------------------------------------------
# Paste the text you want to summarize here
# ---------------------------------------------------------------------------
ARTICLE_TEXT = """
Quarterly profits at US media giant TimeWarner jumped 76% to $1.13bn
(£600m) for the three months to December, from $639m year-earlier.
The firm, which is now one of the biggest investors in Google, benefited
from sales of high-speed internet connections and higher advert sales.
TimeWarner said fourth quarter sales rose 2% to $11.1bn from $10.9bn.
Its profits were buoyed by one-off gains which offset a profit dip at
Warner Bros, and less users for AOL.
"""
# ---------------------------------------------------------------------------


def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = LEDForConditionalGeneration.from_pretrained(MODEL_DIR)
    model.to(device)
    model.eval()
    return tokenizer, model, device


def summarize(text, tokenizer, model, device):
    inputs = tokenizer(
        text, return_tensors="pt", truncation=True, max_length=MAX_INPUT_LENGTH
    ).to(device)

    global_attention_mask = torch.zeros_like(inputs["input_ids"]).to(device)
    global_attention_mask[:, 0] = 1

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            global_attention_mask=global_attention_mask,
            max_new_tokens=MAX_NEW_TOKENS,
            num_beams=4,
        )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


def main():
    tokenizer, model, device = load_model()
    print(f"Model loaded from ./{MODEL_DIR} on {device}\n")

    print("ARTICLE:\n" + ARTICLE_TEXT.strip())
    summary = summarize(ARTICLE_TEXT.strip(), tokenizer, model, device)
    print("\nSUMMARY:\n" + summary)


if __name__ == "__main__":
    main()