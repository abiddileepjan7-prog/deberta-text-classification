"""
=========================================================
XML Processing Demo

Libraries
1. xml.etree.ElementTree
2. lxml
3. BeautifulSoup

=========================================================
"""

import xml.etree.ElementTree as ET
from lxml import etree
from bs4 import BeautifulSoup

FILE = "BhaRuns.xml"

# ==========================================================
# 1. ELEMENTTREE
# ==========================================================

print("=" * 70)
print("1. ELEMENTTREE")
print("=" * 70)

tree = ET.parse(FILE)
root = tree.getroot()

print("\nRoot Tag")
print(root.tag)

print("\nAttributes")
print(root.attrib)

# Namespace
ns = {
    "witsml": "http://www.witsml.org/schemas/1series"
}

# ----------------------------------------------------------
# BHA Runs
# ----------------------------------------------------------

bha_runs = root.findall("witsml:bhaRun", ns)

print("\nNumber of BHA Runs :", len(bha_runs))

for run in bha_runs:

    print("\n-----------------------------")

    print("UID :", run.attrib.get("uid"))

    print("Well UID :", run.attrib.get("uidWell"))

    print("Wellbore UID :", run.attrib.get("uidWellbore"))

    print("Well Name :",
          run.find("witsml:nameWell", ns).text)

    print("Wellbore :",
          run.find("witsml:nameWellbore", ns).text)

    print("Run Name :",
          run.find("witsml:name", ns).text)

    print("Start :",
          run.find("witsml:dTimStart", ns).text)

    print("Stop :",
          run.find("witsml:dTimStop", ns).text)

# ==========================================================
# 2. LXML
# ==========================================================

print("\n")
print("=" * 70)
print("2. LXML")
print("=" * 70)

tree = etree.parse(FILE)

root = tree.getroot()

print("\nRoot")

print(root.tag)

print("\nXPath - Well Names")

for name in tree.xpath(
    "//witsml:nameWell/text()",
    namespaces=ns
):
    print(name)

print("\nXPath - Run Names")

for name in tree.xpath(
    "//witsml:name/text()",
    namespaces=ns
):
    print(name)

print("\nXPath - Mud Weight")

for mud in tree.xpath(
    "//witsml:wtMud/text()",
    namespaces=ns
):
    print(mud)

print("\nXPath - Flow Rate")

for flow in tree.xpath(
    "//witsml:flowratePump/text()",
    namespaces=ns
):
    print(flow)

print("\nXPath - All UID Attributes")

uids = tree.xpath("//@uid")

for uid in uids:
    print(uid)

# ==========================================================
# 3. BEAUTIFULSOUP
# ==========================================================

print("\n")
print("=" * 70)
print("3. BEAUTIFULSOUP")
print("=" * 70)

with open(FILE,
          "r",
          encoding="utf-8") as f:

    soup = BeautifulSoup(
        f,
        "xml"
    )

print("\nRoot")

print(soup.find().name)

print("\nWell Name")

print(soup.find("nameWell").text)

print("\nRun Name")

print(soup.find("name").text)

print("\nDrilling Parameters")

for p in soup.find_all("drillingParams"):

    print("UID :", p["uid"])

print("\nMud Weights")

for mud in soup.find_all("wtMud"):

    print(mud.text)

print("\nFlow Rates")

for flow in soup.find_all("flowratePump"):

    print(flow.text)

print("\nDone.")