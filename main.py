import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port, attachment_path):
  message = MIMEMultipart()
  message['From'] = sender_email
  message['To'] = receiver_email
  message['Subject'] = subject

  message.attach(MIMEText(body, 'plain'))

  filename = os.path.basename(attachment_path)
  with open(attachment_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
      "Content-Disposition",
      f"attachment; filename= {filename}",
    )
    message.attach(part)

  try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print(f"Email sent successfully to {receiver_email}!")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    server.quit()

# Example usage
sender_email = "qrcodesender@outlook.com"
sender_password = "u4J7AhPneqJrrqM"
smtp_server = "smtp.office365.com"
smtp_port = 587
subject = "QR code of from ADA"
body = "Bu QR codu ADA-ya girişdə göstərməlisiz."

# List of recipient emails and their respective attachment paths
emails_and_attachments = [
  { "email": "random", "attachment": "./qr_codes/qr_code.png"},
]

for item in emails_and_attachments:
  if item["email"]!="nan":
    send_email(
      sender_email=sender_email,
      sender_password=sender_password,
      receiver_email=item["email"],
      subject=subject,
      body=body,
      smtp_server=smtp_server,
      smtp_port=smtp_port,
      attachment_path=item["attachment"]
    )
