
import smtplib
import getpass
from email.message import EmailMessage

email_address = input('Enter your Mail Address :')
email_password = getpass.getpass(prompt='Enter your password :')

message = EmailMessage()
message['Subject'] = 'Task1 : Email Application'
message['From'] = email_address
message['To'] = 'sarankintern@gmail.com'
message.set_content('Payment successful')

with smtplib.SMTP('localhost',1025) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(message)
