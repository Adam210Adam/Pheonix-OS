import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
email = EmailMessage()
html = Template(Path("index.html").read_text())

email["to"] = "programmingdumdum@hotmail.com"
email["from"] = "programmingdumdum@hotmail.com"
email["subject"] = "We have detected that you have a virus on your Pheonix OS Careful do not restart your computer or else the virus might activate for safety Reinstall Pheonix OS on a brand new drive before 5 days pass."
email.set_content(html.substitute({"version": 1.926,"Trial": "7-days"}), 'html')

with smtplib.SMTP("smtp-mail.outlook.com",587) as SMTP:
    SMTP.ehlo()
    SMTP.starttls()
    SMTP.login("programmingdumdum@hotmail.com", "domy6666")
    SMTP.send_message(email)