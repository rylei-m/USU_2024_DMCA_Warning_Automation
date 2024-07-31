import xml.etree.ElementTree as ET

tree = ET.parse('/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/testFiles/demo.xml')
root = tree.getroot()
namespace = {'ns': 'http://www.acns.net/ACNS'}

data = {}


def strip_namespace(tag):
    return tag.split("}")[1] if "}" in tag else tag


def extract_and_print(element, ns):
    for child in element:
        tag = strip_namespace(child.tag)
        text = child.text.strip() if child.text is not None else ''
        if len(child.attrib) > 0:
            for attr, value in child.attrib.items():
                print(f"{tag}.{attr} = \"{value}\"")
        if text:
            print(f"{tag} = \"{text}\"")
        extract_and_print(child, ns)
        # data[tag] = text


print(f"Root element: {strip_namespace(root.tag)}\n")
extract_and_print(root, namespace)
