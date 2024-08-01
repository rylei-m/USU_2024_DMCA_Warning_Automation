import smtplib

from XMLforDMCA.outgoing.EmailTemplate import subject, body

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

message = f'Subject: {subject}\n\n{body}'

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(from_email, to_email, message)
