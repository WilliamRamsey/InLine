import smtplib
from email.message import EmailMessage
import ssl

sender = "in.line.notification@gmail.com"
password = "lxbcaltjtzbegkjj"
recipient = "4705096044@"

subject = "It is your turn to appoach the counter"
body = "Thanks for choosing InLine"

em = EmailMessage()
em["From"] = sender
em['To'] = recipient
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, recipient, em.as_string())

