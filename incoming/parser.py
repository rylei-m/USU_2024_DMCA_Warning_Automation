import xml.etree.ElementTree as ET

tree = ET.parse('/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/testFiles/demoIgnore.xml')
root = tree.getroot()
namespace = {'ns': 'http://www.acns.net/ACNS'}


def strip_namespace(tag):
    return tag.split("}")[1] if "}" in tag else tag


def extract_data(element):
    data = {}
    for child in element:
        tag = strip_namespace(child.tag)
        text = child.text.strip() if child.text is not None else ''
        if len(child.attrib) > 0:
            for attr, value in child.attrib.items():
                data[f"{tag}.{attr}"] = value
        if text:
            data[tag] = text
        child_data = extract_data(child)
        if child_data:
            data.update(child_data)
    return data
