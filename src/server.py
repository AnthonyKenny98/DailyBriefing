"""Satisfy Heroku Requirement."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-24 18:56:44
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-24 18:57:00
from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))
