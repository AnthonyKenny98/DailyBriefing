"""Main."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-16 12:13:34
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-05-05 20:12:41

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import sys
import jinja2
from premailer import transform

dir_path = os.path.dirname(os.path.realpath(__file__))
PORT = 465
GMAIL = dir_path + '/gmail.creds'
PASS = dir_path + '/password.creds'
SMTP_SERVER = "smtp.gmail.com"


def render_template(template, **kwargs):
    """Render a Jinja template into HTML."""
    # check if template exists
    if not os.path.exists(template):
        print('No template file present: %s' % template)
        sys.exit()

    template_loader = jinja2.FileSystemLoader(searchpath="/")
    template_env = jinja2.Environment(loader=template_loader)
    templ = template_env.get_template(template)
    return templ.render(**kwargs)


def send_mail(data):
    """main."""
    # Get Sender Gmail Address
    try:
        with open(GMAIL, 'r') as g:
            sender_email = g.read()
    except Exception:
        sender_email = os.environ['GMAIL']

    # Get Gmail Password
    try:
        with open(PASS, 'r') as p:
            password = p.read()
    except Exception:
        password = os.environ['GMAIL_PASSWORD']

    # Create MIME multipart message
    message = MIMEMultipart('alternative')
    message["From"] = sender_email
    message["To"] = data['briefing'].user.email
    message['subject'] = data['subject']

    # Use Jinga to render template with variables
    html = render_template(dir_path + '/mail.html', briefing=data['briefing'])
    # Transform html from css to inline styling (needed for emails)
    html = transform(html, strip_important=False)

    # DEVELOPMENT - write to html file
    with open(dir_path + '/../mailout.html', 'w') as f:
        f.write(html)

    # Create second part, html
    part = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part)

    # Uncomment to send email
    context = ssl.create_default_context()
    if os.environ.get('HEROKU') is not None:
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, data['briefing'].user.email, message.as_string())
