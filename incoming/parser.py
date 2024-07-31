import xml.etree.ElementTree as ET

tree = ET.parse('/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/testFiles/demo.xml')
root = tree.getroot()

data = {}

for child in root:
    tag = child.tag
    text = child.text.strip()

    data[tag] = text

for key, value in data.items():
    print(f"{key.replace('_',' ').title()} = \"{value}\"")
