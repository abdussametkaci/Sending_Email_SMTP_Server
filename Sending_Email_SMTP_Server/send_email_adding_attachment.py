import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

my_address = 'my_email_address'
target_email = "target_email"
my_password = "my_password"

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

subject = "Full Example Code Test"
text = """\
Hi,
How are you?
I want to code on PyCharm.
Can you help me?
"""
html = """\
<html>
    <body>
        <p>Hi,<br>
            How are you?<br>
            <a href="http://www.youtube.com">This channel</a> 
            has many great videos.
        </p>
    </body>
</html>
"""

filename = "helloWorld.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)


# setup the parameters of the message
message['From'] = my_address
message['To'] = target_email
message['Subject'] = subject

# add in the message body
message.attach(MIMEText(text, 'plain'))
message.attach(MIMEText(html, "html"))
message.attach(part)

# send the message via the server set up earlier.
server.send_message(message)

# Terminate the SMTP session and close the connection
server.quit()

