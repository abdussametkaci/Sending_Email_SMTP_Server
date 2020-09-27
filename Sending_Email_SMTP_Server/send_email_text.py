import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_address = ""
target_email = ""
my_password = ""

# read my password from file
"""
# if you want to write your own password to a file, you can read your password from a file
with open("password.txt", "r") as file:
    my_password = file.readline()
"""
# set up the SMTP server
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()

server.login(my_address, my_password)

# create a message
message = MIMEMultipart()

subject = "Saying Hello!"
text = "Hi! How are you?"

# setup the parameters of the message
message['From'] = my_password
message['To'] = target_email
message['Subject'] = subject

# add in the message body
message.attach(MIMEText(text, 'plain'))

# send the message via the server set up earlier.
server.send_message(message)

# Terminate the SMTP session and close the connection
server.quit()
