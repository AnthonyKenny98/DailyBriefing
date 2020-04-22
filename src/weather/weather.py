"""Weather Handling."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-19 11:46:58
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-21 16:10:23

from api import API

COORDINATES = {
    'sydney': {'lat': -33.87, 'long': 151.21},
    'canyonleigh': {'lat': -34.54, 'long': 150.13}
}

ICON_URL = 'http://openweathermap.org/img/wn/{}@2x.png'
UNITS = 'metric'


class Weather(API):
    """Weather Class."""

    # Redefine Class Attributes
    BASE_URL = 'https://api.openweathermap.org/data/2.5/onecall?'

    def __init__(self, city):
        """Initialize Function."""
        super().__init__()
        self.coordinates = COORDINATES[city]


class WeatherToday(Weather):
    """Today's Weather."""

    def __init__(self, city):
        """Initialize today's forecast."""
        super().__init__(city)
        params = {
            'lat': self.coordinates['lat'],
            'lon': self.coordinates['long'],
            'appid': self.api_key,
            'units': UNITS
        }
        r = self.get(params)
        print(self.api_key)
        today = r['daily'][0]
        self.temp = int(r['current']['temp'])
        self.min_temp = today['temp']['min']
        self.max_temp = today['temp']['max']
        # First item in list of weather descriptions
        # [TODO? Account for rest of list?]
        self.description = today['weather'][0]['description']
        self.icon_url = ICON_URL.format(today['weather'][0]['icon'])
