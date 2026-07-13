"""
=========================================================
HTML Processing Demo

Libraries

1. BeautifulSoup
2. lxml
3. html5lib

=========================================================
"""

from bs4 import BeautifulSoup
from lxml import html

FILE = "sample.html"

# =========================================================
# BEAUTIFULSOUP
# =========================================================

print("="*70)
print("1. BEAUTIFULSOUP")
print("="*70)

with open(FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

print("\nTitle")

print(soup.title.text)

# ---------------------------------------------------------
# Headings
# ---------------------------------------------------------

print("\nHeadings")

for tag in soup.find_all(["h1", "h2", "h3"]):
    print(tag.text)

# ---------------------------------------------------------
# Paragraphs
# ---------------------------------------------------------

print("\nParagraphs")

for p in soup.find_all("p"):
    print(p.text)

# ---------------------------------------------------------
# Links
# ---------------------------------------------------------

print("\nLinks")

for link in soup.find_all("a"):
    print("Text :", link.text)
    print("URL  :", link["href"])
    print()

# ---------------------------------------------------------
# Images
# ---------------------------------------------------------

print("\nImages")

for img in soup.find_all("img"):
    print(img["src"])

# ---------------------------------------------------------
# Tables
# ---------------------------------------------------------

print("\nTables")

tables = soup.find_all("table")

print("Tables Found :", len(tables))

for table in tables:

    for row in table.find_all("tr"):

        data = []

        for cell in row.find_all(["th","td"]):

            data.append(cell.text.strip())

        print(data)

# ---------------------------------------------------------
# Lists
# ---------------------------------------------------------

print("\nDepartments")

for li in soup.find_all("li"):
    print(li.text)

# ---------------------------------------------------------
# Forms
# ---------------------------------------------------------

print("\nForms")

forms = soup.find_all("form")

print("Forms Found :", len(forms))

for form in forms:

    inputs = form.find_all("input")

    for inp in inputs:

        print(inp["type"], inp.get("name"))


# =========================================================
# LXML
# =========================================================

print("\n")
print("="*70)
print("2. LXML")
print("="*70)

with open(FILE,"r",encoding="utf-8") as f:
    tree = html.fromstring(f.read())

print("\nTitle")

print(tree.xpath("//title/text()"))

print("\nHeadings")

print(tree.xpath("//h1/text()"))

print(tree.xpath("//h2/text()"))

print("\nLinks")

print(tree.xpath("//a/@href"))

print("\nImage")

print(tree.xpath("//img/@src"))

print("\nTable Rows")

rows = tree.xpath("//table/tr")

for row in rows:

    print(row.xpath("./th/text() | ./td/text()"))

print("\nParagraphs")

print(tree.xpath("//p/text()"))

# =========================================================
# HTML5LIB
# =========================================================

print("\n")
print("="*70)
print("3. HTML5LIB")
print("="*70)

with open(FILE,"r",encoding="utf-8") as f:

    soup = BeautifulSoup(f,"html5lib")

print("Title :", soup.title.text)

print("\nHeadings")

for h in soup.find_all("h2"):
    print(h.text)

print("\nLinks")

for a in soup.find_all("a"):
    print(a["href"])

print("\nImages")

for img in soup.find_all("img"):
    print(img["src"])

print("\nDone.")