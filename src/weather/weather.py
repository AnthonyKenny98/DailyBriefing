"""Weather Handling."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-19 11:46:58
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-19 21:42:45

import requests
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

COORDINATES = {
    'sydney': {'lat': -33.87, 'long': 151.21},
    'canyonleigh': {'lat': -34.54, 'long': 150.13}
}

API_KEY = dir_path + '/api.credentials'
BASE_URL = 'https://api.openweathermap.org/data/2.5/onecall?'
UNITS = 'metric'


class Weather:
    """Weather Class."""

    def __init__(self, city):
        """Initialize Function."""
        with open(API_KEY) as f:
            self.api_key = f.read()

        self.coordinates = COORDINATES[city]

    def __get(self):
        params = {
            'lat': self.coordinates['lat'],
            'lon': self.coordinates['long'],
            'appid': self.api_key,
            'units': UNITS
        }
        r = requests.get(BASE_URL, params=params)
        return r.json()

    def today(self):
        """Return Today's Forecast."""
        r = self.__get()
        # First item in 7 day forecast list
        today = r['daily'][0]
        return {
            'min_temp': today['temp']['min'],
            'max_temp': today['temp']['max'],
            # First item in list of weather descriptions
            # [TODO? Account for rest of list?]
            'description': today['weather'][0]['description'],
            'icon_url': 'http://openweathermap.org/img/wn/{}@2x.png'.format(
                today['weather'][0]['icon'])
        }


# For Development --> needs deleting
if __name__ == '__main__':
    w = Weather('canyonleigh')
    print(w.today())
