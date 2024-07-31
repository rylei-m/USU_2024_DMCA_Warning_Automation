import os
import json
from XMLforDMCA.Main import main  # Import the main function

script_dir = os.path.dirname(os.path.abspath(__file__))
xml_path = os.path.join(script_dir, '../testFiles/demoIgnore.xml')

output_data = main(xml_path)

output_path = os.path.join(script_dir, 'parsedData.json')

with open(output_path, 'w') as file:
    json.dump(output_data, file, indent=4)

print(f"Data saved to {output_path}")
