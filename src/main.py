"""Main."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-19 21:10:05
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 09:47:23

from mail.mail import send_mail
from api.weather import WeatherToday
from api.news import NewsToday
from api.language import Language
from datetime import datetime

LANGUAGES = ['latin', 'french']


class Date():
    """Date."""

    def __init__(self):
        """Init date."""
        dt = datetime.now()
        self.dayname = dt.strftime('%A')
        self.day = dt.strftime('%d')
        self.month = dt.strftime('%B')
        self.year = dt.strftime('%Y')
        self.time = dt.strftime('%H:%M:%S')


class Briefing:
    """Holds the entire briefing."""

    def __init__(self):
        """Initialize briefing."""
        self.user = 'Anthony Kenny'
        self.date = Date()
        self.weather = WeatherToday('canyonleigh')
        self.news = NewsToday()
        self.languages = [Language(language) for language in LANGUAGES]

data = {
    'subject': datetime.now().strftime("%H:%M:%S"),
    'briefing': Briefing()
}

send_mail(data)
