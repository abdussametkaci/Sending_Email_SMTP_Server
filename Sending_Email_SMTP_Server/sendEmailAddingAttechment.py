import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_address = ""
target_email = ""
my_password = ""

# read my password from file
with open("password.txt", "r") as file:
    my_password = file.readline()

# set up the SMTP server
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()

server.login(my_address, my_password)

# Create a multipart message and set headers
message = MIMEMultipart()

subject = "Saying Hello!"
text = "Hello! What's up?"

message["From"] = my_address
message["To"] = target_email
message["Subject"] = subject
# message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(text, "plain"))

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

# Add attachment to message
message.attach(part)

# send the message via the server set up earlier.
server.send_message(message)

# Terminate the SMTP session and close the connection
server.quit()


