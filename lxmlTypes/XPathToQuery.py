from lxml import etree

# Define an XML document as a string
xml_string = '''<root>
    <child name="example">Some text</child>
</root>'''

# Parse the XML document
root = etree.fromstring(xml_string)

# Query using XPath
child = root.xpath('//child')[0]

print(child.text)
print(child.get('name'))
