# -*- coding: utf-8 -*-
"""
requests_google.utils
"""

import urllib


def get_google_news_location_news_rss_url(city, state):
    base = 'https://news.google.com/news/rss/local/section/geo/'
    location = '{}, {}, United States/'.format(city, state)
    return base + urllib.quote_plus(location) 