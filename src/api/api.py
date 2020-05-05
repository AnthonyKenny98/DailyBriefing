"""Super API Accessing Class to reduce code complexity."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-21 15:13:04
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-05-05 19:49:29

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
            # Credentials stored in local file with name of class
            with open(self.dir_path() + '/' + cred.lower() + '.creds') as f:
                self.api_key = f.read().rstrip()
        except Exception:
            # Will set to None if no OS environment variable set
            self.api_key = os.environ.get(cred)

    def dir_path(self):
        """Return path to instance of child class."""
        path = sys.modules[self.__module__].__file__
        return os.path.dirname(os.path.realpath(path))

    def get(self, endpoint=None, params=None):
        """Get request to Base URL."""
        url = self.BASE_URL if endpoint is None else self.BASE_URL + endpoint
        return requests.get(url, params=params).json()
