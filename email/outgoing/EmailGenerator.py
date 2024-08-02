import smtplib

from XMLforDMCA.email.creation.EmailTemplate import generated_email_subject, generated_email_body
from XMLforDMCA.email.outgoing.privateUserInfo.JsonConverter import (UserEmail, Password, EmailTo)

"""
The smtplib library is a powerful tool that allows you to send emails using the Simple Mail Transfer Protocol (SMTP). 
To use the smtplib library, you must first set up an email account that can be used to send emails programmatically.
"""

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = f"{UserEmail}"
smtp_password = f"{Password}"

from_email = f"{UserEmail}"
to_email = f"{EmailTo}"

message = f'Subject: {generated_email_subject()}\n\n{generated_email_body()}'


def sender():
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)


print("Email sent successfully!")
