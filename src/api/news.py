"""News Class."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-21 15:03:22
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 09:13:39

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
            'language': 'en',
            'sources': 'australian-financial-review'
        }
        self.articles = [Article(a) for a in self.get(params=params)['articles']]


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
