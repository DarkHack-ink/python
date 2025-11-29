import smtplib
import ssl
from email.message import EmailMessage

Email = "shidhartsharma183@gmail.com"
App_password = "xxxxxxxx"  # Use an app password for security
Recivier_email = "latashrma592@gmail.com"
msg = EmailMessage()

msg['From'] = Email
msg['To'] = Recivier_email
msg['Subject'] = "Test email from python"
msg.set_content("This is a test email sent from a Python script using smtplib and EmailMessage.")
msg.set_content("This is a test email sent from a Python script using smtplib and EmailMessage.")
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(Email, App_password)
    server.send_message(msg)
    print("Email sent successfully!")
    print("Email sent successfully!")