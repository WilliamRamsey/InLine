import smtplib
from email.message import EmailMessage
import ssl

def send_mail(recipient):
    sender = "in.line.notification@gmail.com"
    password = "lxbcaltjtzbegkjj"

    subject = "<Company Name>"
    body = "It's your turn to approach the counter"

    em = EmailMessage()
    em["From"] = sender
    em['To'] = recipient
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, em.as_string())
