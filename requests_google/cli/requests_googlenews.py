# -*- coding: utf-8 -*-

import argparse
import json
import sys

from ..api import get_google_news_location_news


def execute(args):
    if args.search_for == 'locations':
        if (not args.city) or (not args.state):
            sys.stderr.write('no city or state\n')
            exit(1)
        result = get_google_news_location_news(args.city, args.state)
    if args.output == 'item_link':
        for item in result['items']:
            print(item['link'])



def main():
    parser = argparse.ArgumentParser(
        prog='requests_googlenews',
        description='A command line tool for parsing google news'
    )

    parser.add_argument('--search_for', default='locations',
                        help='Search for topics, locations & sources')
    parser.add_argument('--city', help='City name')
    parser.add_argument('--state', help='State name')
    parser.add_argument('--output', default='item_link',
                        help='Output control')

    args = parser.parse_args()
    execute(args)


if __name__ == '__main__':
    main()
