"""Init."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-21 14:05:07
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-27 10:07:40


from src.api.weather import WeatherToday
from src.api.news import NewsToday


def test_weathertoday():
    """Test initialization of weather module."""
    w = WeatherToday('sydney')
    assert hasattr(w, 'temp')
    assert hasattr(w, 'min_temp')
    assert hasattr(w, 'max_temp')
    assert hasattr(w, 'description')
    assert hasattr(w, 'icon_url')


def test_newstoday():
    """Test initialization of weather module."""
    n = NewsToday()
    assert hasattr(n, 'afr')
