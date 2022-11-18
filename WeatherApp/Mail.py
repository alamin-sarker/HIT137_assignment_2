###
# We were planning to send real time weather report to user 
# but currently not inrigated in our App due to time constraints, 
# we will do that later
###

import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email form Python!"
sender_email = "justintaylor7890@gmail.com"
receiver_email = "haiderimran13224@gmail.com"
password = "gwddfptlvvhqzbow"

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, sender_email, message.as_string())

print("Success")