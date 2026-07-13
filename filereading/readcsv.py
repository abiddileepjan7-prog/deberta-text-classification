"""
=========================================================
CSV Processing using Python
Libraries:
1. csv (Built-in)
2. pandas
3. polars
=========================================================
"""

import csv
import pandas as pd
import polars as pl

FILE = "Employee_Salary_Dataset.csv"

# ==========================================================
# 1. CSV MODULE
# ==========================================================

print("=" * 70)
print("1. CSV MODULE")
print("=" * 70)

# Read all rows
with open(FILE, "r", encoding="utf-8") as file:

    reader = csv.reader(file)

    print("\nReading CSV")

    for row in reader:
        print(row)

# Count rows & columns
with open(FILE, "r", encoding="utf-8") as file:

    reader = list(csv.reader(file))

    print("\nRows (including header):", len(reader))
    print("Columns:", len(reader[0]))


# ==========================================================
# 2. PANDAS
# ==========================================================

print("\n")
print("=" * 70)
print("2. PANDAS")
print("=" * 70)

df = pd.read_csv(FILE)

print("\nFirst Five Rows")
print(df.head())

# ==========================================================
# 3. POLARS
# ==========================================================

print("\n")
print("=" * 70)
print("3. POLARS")
print("=" * 70)

pl_df = pl.read_csv(FILE)

print("\nShape")
print(pl_df.shape)

print("\nColumns")
print(pl_df.columns)

print("\nHead")
print(pl_df.head())

print("\nTail")
print(pl_df.tail())


print("\nDone.")