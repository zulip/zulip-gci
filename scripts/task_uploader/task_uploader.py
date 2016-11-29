# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A simple CSV uploader client for the GCI API.

Usage:
  ./csv_uploader --apikey abc123 tasks.csv

Note:
 This uploader will attempt to upload all tasks in the file.  If you run it
 more than once on a file, you will end up with duplicate tasks.

"""

import argparse
import csv

import requests
from .client import GCIAPIClient
from .config import PUBLISH, URL, DEBUG, VERBOSE, DELIMITER, API_KEY, FILES


argparser = argparse.ArgumentParser(description='GCI CSV Task Uploader.')
argparser.add_argument('--apikey', type=str, nargs='?', required=False,
                       help='api key')
argparser.add_argument('files', nargs=argparse.REMAINDER,
                       help='csv file to upload')

CONFIG = argparser.parse_args()

API_KEY = CONFIG.apikey if CONFIG.apikey is not None else API_KEY
FILES = CONFIG.files if len(CONFIG.files) > 0 else FILES


def upload(client, filename):
    """Creates new tasks for each line in the csv pointed to by filename.

    Args:
      client: A GCIAPIClient to form and make the requests.
      filename: A string filename containing the csv encoded tasks.

    Raises:
      none
    """

    # One line order:
    # [
    # 'name', 'description', 'max_instances', 'mentors', 'tags',
    # 'is_beginner', 'categories', 'time_to_complete_in_days',
    # 'private_metadata'
    # ]
    with open(filename, 'rb') as csvfile:
        tasks = csv.reader(csvfile, delimiter=DELIMITER)

        for task in tasks:
            t = dict()
            t['name'] = task[0]
            t['description'] = task[1]
            t['status'] = 2 if PUBLISH else 1
            t['mentors'] = task[3].split(',') if len(task[3]) else []
            t['categories'] = task[6].split(',') if len(task[6]) else []
            t['tags'] = task[4].split(',') if len(task[4]) else []
            t['is_beginner'] = task[5].lower() in ['yes', 'true', '1']
            t['time_to_complete_in_days'] = int(task[7])
            t['max_instances'] = int(task[2])
            t['private_metadata'] = task[8]

            try:
                t = client.create_new_task(t)
                if VERBOSE:
                    print('\t'.join(['OK', str(t['id']), t['name'], '']))
            except requests.exceptions.HTTPError as e:
                if VERBOSE:
                    print('\t'.join(['ERROR', '', t['name'], e.response.text]))


def main():
    client = GCIAPIClient(
        auth_token=API_KEY,
        url_prefix=URL,
        debug=DEBUG)

    for filename in FILES:
        upload(client, filename)


if __name__ == '__main__':
    main()

