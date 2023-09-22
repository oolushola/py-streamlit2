import smtplib
import ssl
import os


def sendEmail(message, receiver,  subject):
    host = "smtp.gmail.com"
    port = 465

    username = "odejobiolushola@gmail.com"
    password = "uvjm dpig yymz zvef"
    password = os.getenv("PASSWORD")

    my_context = ssl.create_default_context()
    content = f"""\
    Subject: {subject}

    From: {receiver}
    {message} - {receiver}
"""
    print(content)

    try:
        with smtplib.SMTP_SSL(host, port, context=my_context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, content)
        pass
    except Exception as e:
        print(e)
