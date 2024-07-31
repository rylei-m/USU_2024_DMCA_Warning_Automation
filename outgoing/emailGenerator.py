# File for automatically generating an outgoing email that should include all required information
# import XMLforDMCA.parsedData
import smtplib

from XMLforDMCA.parsedData.JsonConverter import Username, Title, Contact, Type, FileName, SubType_Protocol, Timestamp

"""
The smtplib library is a powerful tool that allows you to send emails using the Simple Mail Transfer Protocol (SMTP). 
To use the smtplib library, you must first set up an email account that can be used to send emails programmatically.
"""

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'youremail@gmail.com'
smtp_password = 'your password'

from_email = 'youremail@gmail.com'
to_email = 'recipient@example.com'
subject = 'NOTICE: Copyright Infringement Warning'
body = f"""
Dear {Username},

You are receiving this message to bring to your attention a matter of urgent importance regarding an infringement of copyright. It has come to our attention that you have unlawfully accessed content owned by {Contact} via {SubType_Protocol} at {Timestamp}.

Details of Infringement:

Description of Infringing Content: {Title} owned by {Contact} was unlawfully accessed by {Username}.
Location of Infringement: {Type}
Original Work Details: {FileName}

The copyright holder for the aforementioned content requests that you take immediate action to address this infringement.

Specifically, we ask that you:

1. Remove the Infringing Content: Please remove or disable access to the infringing material.
2. Confirm Removal: Once the content has been removed, kindly confirm by replying to this email with a written acknowledgment.

Please be aware that failure to address this issue promptly may result in further legal action to protect intellectual property rights.

We also ask that you refrain from future use and sharing of the Rights Owners’ materials and property. In complying with this notice, you should not destroy any evidence that may be relevant in a lawsuit relating to the infringement alleged; including all associated electronic documents and data relating to the presence of the infringing items on your site, which shall be preserved while disabling public access, irrespective of any document retention or corporate policy to the contrary.

Thank you for your prompt attention to this matter.

Sincerely,

[Name]
[Your Position]
[Your Company/Organization Name]
[Your Contact Information]
[Your Email Address]
"""

message = f'Subject: {subject}\n\n{body}'

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(from_email, to_email, message)
