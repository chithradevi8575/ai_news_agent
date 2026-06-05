import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")


def send_email(file_path, news):
    msg = MIMEMultipart()

    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO
    msg["Subject"] = "AI News Report (Top 10)"

    # Email body
    body = "Top 10 AI News Headlines\n\n"

    for i, item in enumerate(news, 1):
        body += f"{i}. {item['title']}\n"
        body += f"{item['link']}\n\n"

    body += "\nWord report is attached."

    msg.attach(MIMEText(body, "plain"))

    # Attachment
    with open(file_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f'attachment; filename="{file_path}"'
    )

    msg.attach(part)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    

    server.login(
        EMAIL_USER.strip(),
        EMAIL_PASS.strip()
    )

    server.send_message(msg)
    server.quit()

    print("✅ Email Sent Successfully")