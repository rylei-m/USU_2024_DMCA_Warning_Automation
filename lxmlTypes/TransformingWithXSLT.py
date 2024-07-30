from lxml import etree

# Define the XML document
xml_string = '''<root>
    <child>Some text</child>
</root>'''

# Parse the XML document
root = etree.fromstring(xml_string)

# Define the XSLT stylesheet
xslt_string = '''<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2><xsl:value-of select="/root/child"/></h2>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>'''

# Parse the XSLT stylesheet
xslt_root = etree.XML(xslt_string)
transform = etree.XSLT(xslt_root)

# Apply the XSLT transformation
transformed_doc = transform(root)

# Print the transformed document
print(str(transformed_doc))
