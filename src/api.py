"""Super API Accessing Class to reduce code complexity."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-21 15:13:04
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-21 15:50:54

import os
import requests
import sys

API_KEY = '/api.credentials'


class API:
    """Super API Class."""

    # Class Attributes
    BASE_URL = ''

    def __init__(self):
        """Super Init."""
        with open(self.dir_path() + API_KEY) as f:
            self.api_key = f.read().rstrip()

    def dir_path(self):
        path = sys.modules[self.__module__].__file__
        return os.path.dirname(os.path.realpath(path))

    def get(self, params):
        return requests.get(self.BASE_URL, params=params).json()
        
