from lxml import etree

xml_dir = '/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/testFiles/demo.xml'

xml_string = '''<root><child name="example">Text</child></root>'''
root = etree.fromstring(xml_string)
