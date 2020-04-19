"""Main."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-19 21:10:05
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-19 21:41:24

from mail import send_mail
from weather import Weather
from datetime import datetime

text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""

w = Weather('canyonleigh')
weather = w.today()

data = {
    'subject': datetime.now().strftime("%H:%M:%S"),
    'text': text,
    'weather': weather
}

send_mail(data)
