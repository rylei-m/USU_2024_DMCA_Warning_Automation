# Load a schema
from lxml import etree

schema_root = etree.XML('''<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="root">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="child" type="xs:string"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>''')
schema = etree.XMLSchema(schema_root)

xml_string = '''<root>
    <child>Some text</child>
</root>'''
root = etree.fromstring(xml_string)

# Validate XML
try:
    schema.assertValid(root)
    print("XML is valid")
except etree.DocumentInvalid as e:
    print("XML is invalid:", e)
