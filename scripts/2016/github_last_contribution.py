#!/usr/bin/env python
'''
This script takes a list of Github usernames separated by space as argument and
delivers the timestamps of their last contributions to their forks
of zulip and zulip-gci.
'''
import argparse
import json
import requests

from datetime import datetime, time

GIT_API_ADDRESS = 'https://api.github.com/repos/{0}/{1}'

def last_contribution(username, repo):
    address = GIT_API_ADDRESS.format(username, repo)
    request = requests.get(address)
    if request.ok:
        user_data = json.loads(request.text or request.content)
        return user_data['pushed_at']
    print (("User {0}: Error while fetching data from Github "
            "for the repository {1}! Status code: {2}")
           .format(username, repo, request.status_code))

def get_datetime(date):
    return None if not date else datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

def date_output(repo, date):
    if not date:
        print('This user has never contributed to {0}.'.format(repo))
    else:
        span = datetime.now() - date
        print('Last {0} contribution: {1}, {2} day(s) and {3:.2f} hour(s) ago.'
              .format(repo, date, span.days, span.seconds/3600))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("usernames",
                        help="Enter usernames separated with spaces.",
                        type=str,
                        nargs='+')
    args = parser.parse_args()

    result = []

    for username in args.usernames:
        date_zulip = get_datetime(last_contribution(username, 'zulip'))
        date_zulip_gci = get_datetime(last_contribution(username, 'zulip-gci'))

        if date_zulip and date_zulip_gci:
            last_date = max(date_zulip, date_zulip_gci)
        else:
            last_date = date_zulip if date_zulip else date_zulip_gci

        result.append((last_date, date_zulip, date_zulip_gci, username))

    result.sort(key=lambda entry: datetime.min if entry[0] is None else entry[0])

    for last_date, date_zulip, date_zulip_gci, username in result:
        print('{0}:'.format(username))
        if last_date is None:
            print('This user does not exist or has never '
                  'contributed to zulip or zulip-gci.\n')
        else:
            span = datetime.now() - last_date
            print('Last contribution: {0}, {1} day(s) and {2:.2f} hour(s) ago.'
                  .format(last_date, span.days, span.seconds/3600))
            date_output('zulip', date_zulip)
            date_output('zulip-gci', date_zulip_gci)
            print('\n')

if __name__ == '__main__':
    main()
