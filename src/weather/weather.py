"""Weather Handling."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-19 11:46:58
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-21 09:01:38

import requests
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

COORDINATES = {
    'sydney': {'lat': -33.87, 'long': 151.21},
    'canyonleigh': {'lat': -34.54, 'long': 150.13}
}

API_KEY = dir_path + '/api.credentials'
BASE_URL = 'https://api.openweathermap.org/data/2.5/onecall?'
ICON_URL = 'http://openweathermap.org/img/wn/{}@2x.png'
UNITS = 'metric'


class Weather:
    """Weather Class."""

    def __init__(self, city):
        """Initialize Function."""
        with open(API_KEY) as f:
            self.api_key = f.read()
        self.coordinates = COORDINATES[city]

    def get(self):
        params = {
            'lat': self.coordinates['lat'],
            'lon': self.coordinates['long'],
            'appid': self.api_key,
            'units': UNITS
        }
        return requests.get(BASE_URL, params=params).json()


class WeatherToday(Weather):
    """Today's Weather."""

    def __init__(self, city):
        """Initialize today's forecast."""
        super().__init__(city)

        today = self.get()['daily'][0]
        self.min_temp = today['temp']['min']
        self.max_temp = today['temp']['max']
        # First item in list of weather descriptions
        # [TODO? Account for rest of list?]
        self.description = today['weather'][0]['description']
        self.icon_url = ICON_URL.format(today['weather'][0]['icon'])
