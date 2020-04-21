"""Main."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-19 21:10:05
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-21 11:55:03

from mail import send_mail
from weather import WeatherToday
from datetime import datetime


class Date():
    """Date."""

    def __init__(self):
        """Init date."""
        dt = datetime.now()
        self.dayname = dt.strftime('%A')
        self.day = dt.strftime('%d')
        self.month = dt.strftime('%B')
        self.year = dt.strftime('%Y')


class Briefing:
    """Holds the entire briefing."""

    def __init__(self):
        """Initialize briefing."""
        self.user = 'Anthony Kenny'
        self.date = Date()
        self.weather = WeatherToday('canyonleigh')


text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""

briefing = Briefing()

data = {
    'subject': datetime.now().strftime("%H:%M:%S"),
    'text': text,
    'briefing': briefing
}

send_mail(data)
