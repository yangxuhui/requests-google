# -*- coding: utf-8 -*-
"""
requests_google.api
"""

import feedparser
import requests

from .utils import get_google_news_location_news_rss_url


def _gen_item(item):
    return {
        'title': item.title,
        'link': item.link,
        'description': item.description,
        # 'published': item.publishhed,
    }


def get_google_news_location_news(city, state):
    """Get news of a location from google news.

    Parameters
    ----------
    city : string
        city name
    state : string
        state name
    """
    url = get_google_news_location_news_rss_url(city, state)
    r = requests.get(url)
    if r.status_code != 200:
        raise RuntimeError('requests status_code={}'.format(status_code))
    d = feedparser.parse(r.text)
    result = {}
    result['title'] = d.feed.title
    result['link'] = d.feed.link
    result['description'] = d.feed.description
    # result['published'] = d.feed.published
    result['items'] = [_gen_item(item) for item in d.entries]
    return result