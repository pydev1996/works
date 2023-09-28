import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 465  # For SSL
image_folder = "JPG FILES"  # Folder containing images

# Lists of sender credentials, subjects, bodies, and receiver emails
sender_credentials = [
    {"email": "pydev1996@gmail.com", "password": "tgtnojwjssurjjev"},
    {"email": "naveensoft31@gmail.com", "password": "jpcfmdquhkplhnfj"},
]

subject_list = ["Subject 1", "Subject 2"]
body_list = ["Body 1", "Body 2"]
receiver_emails = ["newch1996@gmail.com", "naveenchikile123@gmail.com"]

# Get a list of image filenames from the specified folder
image_files = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder)]

# Create an SSL context
context = ssl.create_default_context()

# Loop through emails in parallel using zip
for i, (sender_info, subject, body, recipient_email) in enumerate(zip(sender_credentials, subject_list, body_list, receiver_emails)):
    sender_email = sender_info["email"]
    sender_password = sender_info["password"]

    # Create a multipart message
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    # Email body
    message.attach(MIMEText(body, "plain"))

    # Get and use the corresponding image filename
    image_filename = image_files[i % len(image_files)]
    with open(image_filename, "rb") as image_file:
        img = MIMEImage(image_file.read(), name=os.path.basename(image_filename))
    message.attach(img)

    # Create an SMTP server connection
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

print("All emails sent.")
