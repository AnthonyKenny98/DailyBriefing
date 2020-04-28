"""News Class."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-21 15:03:22
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-27 11:10:12

from .api import API


class News(API):
    """News Class."""

    # Redefine Class Attributes
    BASE_URL = 'https://newsapi.org/v2/top-headlines'

    def __init__(self):
        """Initialize."""
        super().__init__()


class NewsToday(News):
    """"Today's News."""

    def __init__(self):
        """Init."""
        super().__init__()
        params = {
            'apiKey': self.api_key,
            'language': 'en'
        }
        # self.intl = [Article(a) for a in self.get(params)['articles']]
        # params['country'] = 'au'
        # self.aus = [Article(a) for a in self.get(params)['articles']]
        # params.pop('country')
        params['sources'] = 'australian-financial-review'
        self.afr = [Article(a) for a in self.get(params)['articles']]
        params['sources'] = 'the-wall-street-journal'
        self.wsj = [Article(a) for a in self.get(params)['articles']]


class Article:
    """News Article."""

    def __init__(self, article):
        """
        Init Story.

        Take an article dict and put them into class attributes.
        """
        self.source = article['source']['name']
        self.title = article['title']
        self.description = article['description']
        self.url = article['url']
        self.img_url = article['urlToImage']
