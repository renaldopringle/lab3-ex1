import smtplib

fromaddr = 'pigeonflight@gmail.com'

toaddr  = 'david@alteroo.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}""" messagetosend = message.format(

                             fromname,

                             fromaddr,

                             toname,

                             toaddr,

                             subject,

                             msg)

# Credentials (if needed)

username = 'pigeonflight@gmail.com'

password = '{youremailapppassword}''

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddrs, messagetosend)

server.quit()
