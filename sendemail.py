import smtplib

fromaddr = 'rapchristoff@gmail.com'

toaddr  = 'renaldopringle@yahoo.com'

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

username = 'myemail@gmail.com'

password = 'mypassword'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddrs, messagetosend)

server.quit()
