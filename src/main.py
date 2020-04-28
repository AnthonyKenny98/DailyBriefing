"""Main."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-19 21:10:05
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-28 17:52:15

from mail.mail import send_mail
from api.weather import WeatherToday
from api.news import NewsToday
from datetime import datetime

import requests
LATIN = 'https://caecilius.herokuapp.com'


class Date():
    """Date."""

    def __init__(self):
        """Init date."""
        dt = datetime.now()
        self.dayname = dt.strftime('%A')
        self.day = dt.strftime('%d')
        self.month = dt.strftime('%B')
        self.year = dt.strftime('%Y')


class LatinPhrase():
    """Latin Phrase."""

    def __init__(self):
        """Init Latin Phrase."""
        r = requests.get(LATIN).json()
        self.phrase = r['latin']
        self.translation = r['english']


class Briefing:
    """Holds the entire briefing."""

    def __init__(self):
        """Initialize briefing."""
        self.user = 'Anthony Kenny'
        self.date = Date()
        self.weather = WeatherToday('canyonleigh')
        self.news = NewsToday()
        self.latin = LatinPhrase()


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
