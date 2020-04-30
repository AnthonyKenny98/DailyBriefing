"""Init."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-21 14:05:07
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 13:58:23

from src.api.api import API
from src.api.weather import WeatherToday
from src.api.news import NewsToday
from src.api.language import Language


def test_api():
    """Test API Base Class."""
    a = API()
    assert hasattr(a, 'BASE_URL')
    assert hasattr(a, 'api_key')


def test_weathertoday():
    """Test initialization of weather class."""
    w = WeatherToday('sydney')
    assert hasattr(w, 'temp')
    assert hasattr(w, 'min_temp')
    assert hasattr(w, 'max_temp')
    assert hasattr(w, 'description')
    assert hasattr(w, 'icon_url')


def test_newstoday():
    """Test initialization of weather class."""
    n = NewsToday()
    assert hasattr(n, 'articles')


def test_article():
    """Test initialization of article class."""
    a = NewsToday().articles[0]
    assert hasattr(a, 'source')
    assert hasattr(a, 'title')
    assert hasattr(a, 'description')
    assert hasattr(a, 'url')
    assert hasattr(a, 'img_url')


def test_language():
    """Test initialization of language class."""
    l = Language('latin')  # noqa: E741
    assert hasattr(l, 'language')
    assert hasattr(l, 'phrase')
    assert hasattr(l, 'translation')
