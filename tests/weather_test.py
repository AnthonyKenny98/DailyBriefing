"""Init."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-21 14:05:07
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-21 14:44:17


from src.weather import WeatherToday


def test_init():
    """Test initialization of weather module."""
    f = WeatherToday('sydney')
    assert hasattr(f, 'temp')
    assert hasattr(f, 'min_temp')
    assert hasattr(f, 'max_temp')
    assert hasattr(f, 'description')
    assert hasattr(f, 'icon_url')
