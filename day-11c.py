# sending email - plain or html

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "John Smith"
message["to"] = "test@test.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("image-name.png").read_bytes()))

with smtplib.SMTP(host="smtp.google.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("username@test.com", "passwordtext")
    smtp.send_message(message)
    print("sent...")
