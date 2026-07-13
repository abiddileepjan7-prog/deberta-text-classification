
import json

from unstructured.partition.auto import partition

from unstructured.documents.elements import (
    Title,
    NarrativeText,
    Table,
    ListItem,
    Header,
    Footer,
)

FILE = "NIPS-2017-attention-is-all-you-need-Paper.pdf"

# ============================================================
# PARTITION DOCUMENT
# ============================================================

print("=" * 70)
print("Reading Document")
print("=" * 70)

elements = partition(filename=FILE)

print("Total Elements :", len(elements))


# ============================================================
# PRINT EVERY ELEMENT
# ============================================================

print("\n")
print("=" * 70)
print("ALL ELEMENTS")
print("=" * 70)

for i, element in enumerate(elements, start=1):

    print("\n-----------------------------------")

    print("Element :", i)

    print("Type :", type(element).__name__)

    if hasattr(element, "text"):

        print(element.text[:200])


# ============================================================
# TITLES
# ============================================================

print("\n")
print("=" * 70)
print("TITLES")
print("=" * 70)

titles = [
    e for e in elements
    if isinstance(e, Title)
]

for t in titles:

    print(t.text)



# ============================================================
# TABLES
# ============================================================

print("\n")
print("=" * 70)
print("TABLES")
print("=" * 70)

tables = [
    e for e in elements
    if isinstance(e, Table)
]

print("Tables Found :", len(tables))

for i, table in enumerate(tables, start=1):

    print()

    print("Table", i)

    print(table.text[:500])


# ============================================================
# LIST ITEMS
# ============================================================

print("\n")
print("=" * 70)
print("LIST ITEMS")
print("=" * 70)

lists = [
    e for e in elements
    if isinstance(e, ListItem)
]

print("List Items :", len(lists))

for item in lists:

    print(item.text)


# ============================================================
# HEADERS
# ============================================================

print("\n")
print("=" * 70)
print("HEADERS")
print("=" * 70)

headers = [
    e for e in elements
    if isinstance(e, Header)
]

print("Headers :", len(headers))

for h in headers:

    print(h.text)


# ============================================================
# FOOTERS
# ============================================================

print("\n")
print("=" * 70)
print("FOOTERS")
print("=" * 70)

footers = [
    e for e in elements
    if isinstance(e, Footer)
]

print("Footers :", len(footers))

for f in footers:

    print(f.text)



print("\nDone.")