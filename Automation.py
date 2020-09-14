#Libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_addr='your_mail_id'
to_addr=['recipient_mail_id']

#instance of MIMEMultipart 
msg=MIMEMultipart()

#storing sender's email address and recipient's email address
msg['From']=from_addr
msg['To']=" ,".join(to_addr)

#adding subject
msg['subject']='add_your_subject_here'
#adding body
body='add_your_body_here'
msg.attach(MIMEText(body,'plain'))

#attaching a file
filename = 'enter_your_filename_with_extension'
attachment = open (filename,'rb')

#changing payload into encoded form
file_input = MIMEBase('application','octet-stream')
file_input.set_payload((attachment).read())
encoders.encode_base64(dile_input)
file_input.add_header('Content-Disposition',"attachment; filename= "+filename)

#sender's details
email='your_email_id'
password='your_password'

#setting the server, convertion of text into string and sending the mail
msg.attach(file_input)
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()
