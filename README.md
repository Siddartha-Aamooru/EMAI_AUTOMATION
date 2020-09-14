# EMAI_AUTOMATION
Code Explanation
-----------------------------

➤ Libraries used:
import smtplib,
from email.mime.multipart import MIMEMultipart,
from email.mime.text import MIMEText,
from email.mime.base import MIMEBase,
from email import encoders,

➤ Create an instance of MIMEMultipart (msg)

➤ Mention the sender’s email id, recipient’s email id and the subject in the “From”, “To” and “Subject” key of the created instance “msg”

➤ Write the body of the message you want to send, namely body. Now, attach the body with the instance msg using attach function

➤ Open the file you wish to attach in the “rb” mode

➤ set_payload is used to change the payload the encoded form. Encode it in encode_base64.

➤ And finally attach the file with the MIMEMultipart created instance msg


Note
------

➤ This code will not work if you have enabled 2-step verification on your gmail account. It is required to switch off the 2-step verification first

➤ Now using this link: https://myaccount.google.com/lesssecureapps, allow less secure apps and torn it on

➤ With this method, Gmail will always put your mail in the primary section and the mails sent will not be Spam
