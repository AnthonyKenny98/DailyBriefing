"""Main."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-19 21:10:05
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-09-12 09:01:03

from mail.mail import send_mail
from api.weather import WeatherToday
from api.news import NewsToday
from api.language import Language
from datetime import datetime
import pytz

import sqlite3
import ast


import os
dir_path = os.path.dirname(os.path.realpath(__file__))


class Date:
    """Date."""

    def __init__(self, timezone):
        """Init date."""
        dt = datetime.now(pytz.timezone(timezone))
        self.dayname = dt.strftime('%A')
        self.day = dt.strftime('%d')
        self.month = dt.strftime('%B')
        self.year = dt.strftime('%Y')
        self.time = dt.strftime('%H:%M:%S')


class User:
    """User."""

    def __init__(self, sql_user):
        """Initialise user object based on SQL query."""
        self.first = sql_user['first']
        self.last = sql_user['last']
        self.location = sql_user['location']
        self.languages = ast.literal_eval(sql_user['languages'])
        self.email = sql_user['email']
        self.timezone = sql_user['pytimezone']


class Briefing:
    """Holds the entire briefing."""

    def __init__(self, user):
        """Initialize briefing."""
        self.user = user
        self.date = Date(user.timezone)
        self.weather = WeatherToday(user.location)
        self.news = NewsToday()
        self.languages = [Language(language) for language in user.languages]


# THIS SQL STUFF IS UGLY AND IS JUST TEMPORARY UNTIL I SCALE UP TO DJANGO.
def dict_factory(cursor, row):
    """Function to turn sqllite query into dict."""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect(dir_path + '/main.db')
conn.row_factory = dict_factory
c = conn.cursor()
users = c.execute('''SELECT * FROM users''').fetchall()

for user in users:
    print('Preparing Briefing for {}'.format(user['first']))
    data = {
        'subject': "Your Daily Briefing, {}".format(
            datetime.now().strftime("%A, %d %B")),
        'briefing': Briefing(User(user))
    }
    send_mail(data)
