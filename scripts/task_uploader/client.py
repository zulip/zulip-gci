import json
import logging
import urllib.parse

import requests


class GCIAPIClientException(Exception):
    pass


class GCIAPIClient(object):
    """
    GCIAPIClient provides a thin wrapper around the GCI Task API.

    A GCIAPIClient simplifies working with tasks by forming the HTTP requests on
    behalf of the caller.

    Attributes:
      url_prefix: A string prefix for the codin URL
      headers: A dictionary of HTTP headers
    """

    def __init__(
            self,
            auth_token=None,
            url_prefix='https://codein.withgoogle.com/',
            debug=False
    ):
        self.url_prefix = urllib.parse.urljoin(url_prefix, 'api/program/current/')
        self.headers = {
            'Authorization': 'Bearer {}'.format(auth_token),
            'Content-Type': 'application/json',
        }

        if debug:
            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger('requests.packages.urllib3')
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True

    def _build_url(self, path):
        return urllib.parse.urljoin(self.url_prefix, path) + '/'

    def get_list_tasks(self, page=1):
        """
        Fetches a list of tasks.

        Args:
          page: Which page of results to return.

        Returns:
          A JSON encoded list of tasks.
        """
        r = requests.get(self._build_url('tasks'), headers=self.headers, params={'page': page})
        r.raise_for_status()
        return r.json()

    def get_task(self, task_id):
        """
        Fetches a single task.

        Args:
          task_id: An integer id for the task.

        Returns:
            A JSON encoded task.
        """
        r = requests.get(self._build_url('tasks/{}'.format(task_id)), headers=self.headers)
        r.raise_for_status()
        return r.json()

    def create_new_task(self, task):
        """
        Creates a single new task.

        Args:
          task: A task object.

        Returns:
          A JSON encoded response.
        """
        r = requests.post(self._build_url('tasks'), headers=self.headers, data=json.dumps(task))
        r.raise_for_status()
        if r.status_code != 201:
            raise GCIAPIClientException("Task wasn't created. Something went wrong.")
        return r.json()

    def modify_task(self, task_id, task):
        """
        Modifies a single task.

        Args:
          task_id: An integer id for the task.
          task: A task object.

        Returns:
          A JSON encoded response.
        """
        r = requests.put(self._build_url('tasks/{}'.format(task_id)), data=json.dumps(task), headers=self.headers)
        r.raise_for_status()
        return r.json()

    def delete_task(self, task_id):
        """
        Deletes a single task.

        Args:
          task_id: An integer id for the task.

        Returns:
          A JSON encoded response, if there is content in the response.
          Otherwise None.
        """
        r = requests.delete(self._build_url('tasks/{}'.format(task_id)), headers=self.headers)
        r.raise_for_status()
        # DELETE returns nothing on success, don't try and parse it.
        if r.content:
            return r.json()
