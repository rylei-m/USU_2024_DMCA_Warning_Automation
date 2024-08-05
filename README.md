# DMCA Warning Automation

## About
The goal of this program is to remove XML tagging from emails sent by the DMCA and automate the sending of warning emails to infringing users. 

It begins by reading from an XML file and converting the XML Tags and their content into JSON format. JSON data referenced and implemented with existing Python patterns before being sent into the EmailTemplate that becomes email subject and body. EmailGenerator uses said subject and body as well as smtp to convert the message into correct email format. Using the link between the program and Google Gmail emails are sent.  

## How to Run
1. Configure your test files or connect to your external email account to import data 
    - Use Config.py to select what test file to run
2. Add your email information to the exampleEmailInfo directory
   - For more information see: EmailInfo 
3. Add your user information to the exampleUserInfo directory
   - For more information see: UserInfo
4. Run the program from Main

## EmailInfo
This section is used for the email signature configuration, it is built to be easily adjustable. The data is stored in a Json file to be stored before being sent to the Email Template. 

## UserInfo
This section is the link between the program and your email. This program is structured for Google Gmail addresses. 
To link your gmail:
1. Ensure that 2-Step Verification is enabled
   - Otherwise, enable it in Settings > Security > How you sign in to Google
2. Generate an App Password
- If not visible search for "App Password" in the navigation bar
- Choose "Other (Custom Name)"
- Enter Name for Password for this Program (Can be whatever you want)
- Click "Generate"
- Copy the 16-character password and paste it into the designated section

## Imports
- smtplib - Used for automatic email sending with Simple Mail Transfer Protocol (SMTP)
- MIME
  - MIMEText - Creates a text MIME object for plain text/HTML content
  - MIMEMultipart - Creates an email with multiple parts (Ex: text and subject)
- xml.etree.ElementTree - Used for parsing and creating XML data. ElementTree represents a XML document
- os - Interacts with the operating system to manipulate paths, create directories, and check file/directory existence
- json (JavaScript Object Notation) - Used for data parsing and passing

## Resources/More Info:

Digital Millennium Copyright Act (DMCA)
- A 1998 United States copyright law that criminalizes production and dissemination of technology, devices, or services intended to circumvent measures that control access to copyrighted works (commonly known as digital rights management or DRM)
- https://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act

smtplib
- https://docs.python.org/3/library/smtplib.html
- https://keentolearn.medium.com/automating-emails-with-python-a-comprehensive-guide-ba00fa98b92

MIME
- https://docs.python.org/3/library/email.mime.html

xml.etree.ElementTree
- https://docs.python.org/3/library/xml.etree.elementtree.html
