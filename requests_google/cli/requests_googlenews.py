# -*- coding: utf-8 -*-

import argparse
import json
import sys

from ..googlenews import get_news_by_geolocation

FIELDS = ['title', 'url', 'description']


def execute(args):
    if args.geolocation:
        city, state = args.geolocation
        result = get_news_by_geolocation(city, state)
    if args.fields:
        d = args.d
        for item in result:
            print(d.join([getattr(item, field) for field in args.fields]))
    else:
        print(json.dumps([item._asdict() for item in result]))


def main():
    parser = argparse.ArgumentParser(
        prog='requests_googlenews',
        description='A command line tool for parsing google news'
    )

    parser.add_argument('-g', '--geolocation', nargs=2, metavar=('city', 'state'),
                        help='geographic location')
    parser.add_argument('-d', metavar='delim', default='\t',
                        help='field delimiter character (default: tab)')
    parser.add_argument('-f', '--fields', nargs='+', 
                        metavar=('field1', 'field2'), choices=FIELDS,
                        help=('list of output fields, separated by the ' + 
                              'field delimiter character (see the -d option).' +
                              ' Allowed fields are: ' + ', '.join(FIELDS)))

    args = parser.parse_args()
    execute(args)


if __name__ == '__main__':
    main()
