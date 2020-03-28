import requests
import base64
import urllib.parse
import json
import time


class Tweeget:
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        # authentication
        self.token = self.authenticate()

    def authenticate(self):
        if self.consumer_key is None or self.consumer_secret is None:
            raise TweegetAuthException('You must provide a consumer key and a consumer secret')
        consumer_key = urllib.parse.quote_plus(self.consumer_key)
        consumer_secret = urllib.parse.quote_plus(self.consumer_secret)

        print(consumer_key)
        print(consumer_secret)

        data_string = consumer_key + ':' + consumer_secret
        print(data_string)
        data_bytes = data_string.encode("ascii")
        basic_auth_bytes = base64.b64encode(data_bytes)
        # Transform from bytes back into Unicode
        b64_encoded_key = basic_auth_bytes.decode('ascii')
        header_basic = 'Basic %s' % (b64_encoded_key)
        print(header_basic)
        headers = {'Authorization': header_basic, \
                   'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        auth_data = {
            'grant_type': 'client_credentials'
        }
        response = requests.post('https://api.twitter.com/oauth2/token', headers=headers, data=auth_data)
        if response.status_code == 403:
            raise TweegetAuthException('Authentication failed')
        if response.status_code == 500:
            raise TweegetAuthException('Server error on authentication')
        elif response.status_code == 200:
            json_return = json.loads(response.content)
            print(json_return)
            return json_return

    def full_archive(self, query, env, fromDate, toDate, maxResults = 100, next_page = None):
        if self.token is None:
            raise TweegetAuthException('You need to authenticate before')

        if env is None or env == '':
            raise TweegetAuthException('Please, provide environment')

        if query is None or query == '':
            raise TweegetAuthException('Please, provide the query')

        if fromDate is None or fromDate == '':
            raise TweegetAuthException('Please, provide the initial date (fromDate)')

        if toDate is None or toDate == '':
            raise TweegetAuthException('Please, provide the initial date (toDate)')

        url_full_archive = 'https://api.twitter.com/1.1/tweets/search/fullarchive/{}.json'.format(env)

        access_token = self.token['access_token']

        headers = {'Authorization': 'Bearer %s' % (access_token), \
                   'Content-Type': 'application/json'}

        data = {
            'query': query,
            'fromDate': fromDate,
            'toDate': toDate,
            'maxResults': str(maxResults)
        }

        if next_page is not None:
            data['next'] = next_page

        response = requests.post(url_full_archive, headers=headers, data=data)

        if response.status_code == 403:
            raise TweegetAuthException('Authentication failed')
        if response.status_code == 500:
            raise TweegetAuthException('Server error')
        elif response.status_code == 200:
            json_return = json.loads(response.content)
            print(json_return)
            return json_return


    def thirty_archive(self, query, env, fromDate, toDate, maxResults = 100, next_page = None):
        if self.token is None:
            raise TweegetAuthException('You need to authenticate before')

        if env is None or env == '':
            raise TweegetAuthException('Please, provide environment')

        if query is None or query == '':
            raise TweegetAuthException('Please, provide the query')

        if fromDate is None or fromDate == '':
            raise TweegetAuthException('Please, provide the initial date (fromDate)')

        if toDate is None or toDate == '':
            raise TweegetAuthException('Please, provide the initial date (toDate)')


        url_full_archive = 'https://api.twitter.com/1.1/tweets/search/30day/{}.json'.format(env)

        access_token = self.token['access_token']

        print(access_token)

        headers = {'Authorization': 'Bearer %s' % (access_token), \
                   'Content-Type': 'application/json'}

        data = {
            'query': query,
            'fromDate': fromDate,
            'toDate': toDate,
            'maxResults': str(maxResults)
        }

        if next_page is not None:
            data['next'] = next_page

        response = requests.post(url_full_archive, headers=headers, json=data)
        print(response)
        if response.status_code == 403:
            raise TweegetAuthException('Authentication failed')
        if response.status_code == 500:
            raise TweegetAuthException('Server error')
        elif response.status_code == 200:
            json_return = json.loads(response.content)
            return json_return




    def full_archive_count(self, query, env, fromDate, toDate, maxResults = 100, bucket='day', next_page = None):
        if self.token is None:
            raise TweegetAuthException('You need to authenticate before')

        if env is None or env == '':
            raise TweegetAuthException('Please, provide environment')

        if query is None or query == '':
            raise TweegetAuthException('Please, provide the query')

        if fromDate is None or fromDate == '':
            raise TweegetAuthException('Please, provide the initial date (fromDate)')

        if toDate is None or toDate == '':
            raise TweegetAuthException('Please, provide the initial date (toDate)')

        url_full_archive = 'https://api.twitter.com/1.1/tweets/search/fullarchive/{}/counts.json'.format(env)

        access_token = self.token['access_token']

        headers = {'Authorization': 'Bearer %s' % (access_token), \
                   'Content-Type': 'application/json'}

        data = {
            'query': query,
            'fromDate': fromDate,
            'toDate': toDate,
            'maxResults': str(maxResults),
            'bucket': bucket
        }

        if next_page is not None:
            data['next'] = next_page

        response = requests.post(url_full_archive, headers=headers, data=data)

        if response.status_code == 403:
            raise TweegetAuthException('Authentication failed')
        if response.status_code == 500:
            raise TweegetAuthException('Server error')
        elif response.status_code == 200:
            json_return = json.loads(response.content)
            print(json_return)
            return json_return


    def thirty_archive_count(self, query, env, fromDate, toDate, maxResults = 100, bucket='day', next_page = None):
        if self.token is None:
            raise TweegetAuthException('You need to authenticate before')

        if env is None or env == '':
            raise TweegetAuthException('Please, provide environment')

        if query is None or query == '':
            raise TweegetAuthException('Please, provide the query')

        if fromDate is None or fromDate == '':
            raise TweegetAuthException('Please, provide the initial date (fromDate)')

        if toDate is None or toDate == '':
            raise TweegetAuthException('Please, provide the initial date (toDate)')

        if bucket is None or bucket == '':
            raise TweegetAuthException('Please, provide the bucket')


        url_full_archive = 'https://api.twitter.com/1.1/tweets/search/30day/{}/counts.json'.format(env)

        access_token = self.token['access_token']

        print(access_token)

        headers = {'Authorization': 'Bearer %s' % (access_token), \
                   'Content-Type': 'application/json'}

        data = {
            'query': query,
            'fromDate': fromDate,
            'toDate': toDate,
            'maxResults': str(maxResults),
            'bucket': bucket
        }

        if next_page is not None:
            data['next'] = next_page

        response = requests.post(url_full_archive, headers=headers, json=data)
        print(response)
        if response.status_code == 403:
            raise TweegetAuthException('Authentication failed')
        if response.status_code == 500:
            raise TweegetAuthException('Server error')
        elif response.status_code == 200:
            json_return = json.loads(response.content)
            return json_return





class TweegetAuthException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'TweegetAuthException: {0} '.format(self.message)
        else:
            return 'TweegetAuthException: Authentication failed'