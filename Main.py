import xml.etree.ElementTree as ET
import os

from XMLforDMCA.parsedData.json_utils import save_to_json
from XMLforDMCA.incoming.parser import extract_data, strip_namespace


def main(path):
    tree = ET.parse(path)
    root = tree.getroot()
    data = extract_data(root)
    return {
        "Root element": strip_namespace(root.tag),
        "Data": data
    }


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_path = '/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/testFiles/demo.xml'

    output_dir = '/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/parsedData/JSONS'
    base_name = "parsedData"
    extension = ".json"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_data = main(xml_path)
    output_path = save_to_json(output_data, output_dir, base_name, extension)

    print(f"Data saved to {output_path}")
