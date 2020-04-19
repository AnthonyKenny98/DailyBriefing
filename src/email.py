"""Main."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-16 12:13:34
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-16 12:42:18

import smtplib
import ssl

PORT = 465
GMAIL = 'gmail.credentials'
PASS = 'password.credentials'
SMTP_SERVER = "smtp.gmail.com"


def main():
    """main."""
    with open(GMAIL, 'r') as g:
        sender_email = g.read()

    with open(PASS, 'r') as p:
        password = p.read()

    receiver_email = "anthonyjwkenny@gmail.com"  # Enter receiver address
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


if __name__ == '__main__':
    main()
