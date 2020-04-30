"""Language."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-30 08:16:08
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 09:09:19

from .api import API


class Language(API):
    """Language Module."""

    # Redfine Class Attributes
    BASE_URL = 'https://caecilius.herokuapp.com'

    def __init__(self, language):
        """Init Language."""
        self.language = language
        super().__init__()
        r = self.get(endpoint='/{}'.format(self.language))
        self.phrase = r['phrase']
        self.translation = r['translation']
