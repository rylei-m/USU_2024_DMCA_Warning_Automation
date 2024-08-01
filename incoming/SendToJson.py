import os

from XMLforDMCA.Main import main
from XMLforDMCA.parsedData.json_utils import save_to_json

script_dir = os.path.dirname(os.path.abspath(__file__))
xml_path = os.path.join(script_dir, '../testFiles/demo3.xml')

output_data = main(xml_path)

output_dir = os.path.join(script_dir, 'parsedData')
base_name = "parsedData"
extension = ".json"

output_path = save_to_json(output_data, output_dir, base_name, extension)

print(f"Data saved to {output_path}")
