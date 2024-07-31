import xml.etree.ElementTree as ET
import json
import os
from XMLforDMCA.incoming.parser import extract_data, strip_namespace


def main(path):
    tree = ET.parse(path)
    root = tree.getroot()
    data = extract_data(root)
    return {
        "Root element": strip_namespace(root.tag),
        "Data": data
    }


def save_to_json(data, path):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_path = '/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/testFiles/demoIgnore.xml'

    output_dir = '/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/parsedData'
    output_path = os.path.join(output_dir, 'parsedData.json')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_data = main(xml_path)
    save_to_json(output_data, output_path)

    print(f"Data saved to {output_path}")
