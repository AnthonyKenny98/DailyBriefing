"""Language."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-30 08:16:08
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 08:33:48

from .api import API


class Language(API):
    """Language Module."""

    # Redfine Class Attributes
    BASE_URL = 'https://caecilius.herokuapp.com'

    def __init__(self):
        """Init Latin Phrase."""
        super().__init__()
        r = self.get()
        self.phrase = r['latin']
        self.translation = r['english']
