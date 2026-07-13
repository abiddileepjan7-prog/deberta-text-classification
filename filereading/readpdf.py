from pypdf import PdfReader

reader = PdfReader("NIPS-2017-attention-is-all-you-need-Paper.pdf")

print(reader)

page = reader.pages[1]
print(page)

text = page.extract_text()

print(text)




import pdfplumber

with pdfplumber.open("NIPS-2017-attention-is-all-you-need-Paper.pdf") as pdf:
    page = pdf.pages[1]

    print(page.extract_text())


with pdfplumber.open("DRAFT-IADC_DDR_Plus_XML_Guide_v1.0-1-24-20191.pdf") as pdf:
    page = pdf.pages[6]

    tables = page.extract_tables()

    print(tables)







import fitz

doc = fitz.open("NIPS-2017-attention-is-all-you-need-Paper.pdf")

for page in doc:
    print(page.get_text())

import fitz  # PyMuPDF
from PIL import Image
import io
import matplotlib.pyplot as plt

# Open the PDF
doc = fitz.open("NIPS-2017-attention-is-all-you-need-Paper.pdf")

# Select the first page
page = doc[2]

# Get all images on the page
images = page.get_images()

print(f"Number of images found: {len(images)}")

# Loop through all images
for i, img in enumerate(images):
    xref = img[0]   # Image reference number

    # Extract image bytes
    base_image = doc.extract_image(xref)

    image_bytes = base_image["image"]
    image_ext = base_image["ext"]

    print(f"\nImage {i+1}")
    print(f"Extension: {image_ext}")

    # Convert bytes to PIL Image
    image = Image.open(io.BytesIO(image_bytes))

    # Display the image
    plt.imshow(image)
    plt.title(f"Image {i+1}")
    plt.axis("off")
    plt.show()