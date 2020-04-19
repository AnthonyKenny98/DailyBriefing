"""Main."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-16 12:13:34
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-19 11:11:41

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

PORT = 465
GMAIL = 'gmail.credentials'
PASS = 'password.credentials'
SMTP_SERVER = "smtp.gmail.com"

RECEIVER_EMAIL = "anthonyjwkenny@gmail.com"


def main():
    """main."""
    # Get Sender Gmail Address
    with open(GMAIL, 'r') as g:
        sender_email = g.read()

    # Get Gmail Password
    with open(PASS, 'r') as p:
        password = p.read()

    message = MIMEMultipart('alternative')
    message['subject'] = datetime.now().strftime("%H:%M:%S")
    message["From"] = sender_email
    message["To"] = RECEIVER_EMAIL

    text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
    with open('e-mail.html') as f:
        html = f.read()

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, RECEIVER_EMAIL, message.as_string())


if __name__ == '__main__':
    main()
