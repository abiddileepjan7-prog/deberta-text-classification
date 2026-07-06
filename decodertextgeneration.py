from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-360M-Instruct"
)

prompt = "Write a short paragraph about Artificial Intelligence."

result = generator(
    prompt,
    max_new_tokens=80,
    temperature=0.7
)

print(result[0]["generated_text"])

