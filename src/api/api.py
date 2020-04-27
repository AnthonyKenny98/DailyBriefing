"""Super API Accessing Class to reduce code complexity."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-21 15:13:04
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-27 10:51:44

import os
import requests
import sys


class API:
    """Super API Class."""

    # Class Attributes
    BASE_URL = ''

    def __init__(self):
        """Super Init."""
        cred = self.__class__.__name__.upper()
        try:
            with open(self.dir_path() + '/' + cred.lower() + '.creds') as f:
                self.api_key = f.read().rstrip()
        except Exception:
            self.api_key = os.environ[cred]

    def dir_path(self):
        path = sys.modules[self.__module__].__file__
        return os.path.dirname(os.path.realpath(path))

    def get(self, params):
        return requests.get(self.BASE_URL, params=params).json()
