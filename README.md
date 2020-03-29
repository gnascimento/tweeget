# Tweeget - Twitter Premium API library

This python library serves to get Twitter data from Twitter using Twitter Premium API.

### History

The need to collect data from COVID-19 emerged when the pandemy begun in Brazil. I believe that the first cases begun after the carnival. But, to collect data from Twitter archive, we need access to Twitter Premium API. The need to write a new library emerged when I realized that  the Tweepy API had no support to Twitter Premium API. 

### Documentation

The library consists in the class Tweeget. Below are the methods implemented:

```python
# Tweeget constructor
tweeget = Tweeget(consumer_key = 'xxxxxxx', consumer_secret = 'xxxxxxxx')
#parameters
env = 'dev' #environment in the twitter dev account
fromDate = 'YYYYMMDDHHMM' #initial date
toDate = 'YYYYMMDDHHMM' #end date
maxResults = 100 #max results
next_page = None # Next page value returned on pagination
bucket = 'day' #unit for tweets counts (day, hour, minute)
#Methods implemented
tweeget.full_archive(query, env, fromDate, toDate, maxResults, next_page) # Access to Full Archive
tweeget.thirty_archive(query, env, fromDate, toDate, maxResults, next_page) # Access to 30-day Archive
tweeget.full_archive_count(self, query, env, fromDate, toDate, maxResults, bucket, next_page) # Count API - Full archive
tweeget.thirty_archive_count(self, query, env, fromDate, toDate, maxResults, bucket, next_page) # Count API - 30-day archive

```

### Example

```python
from tweeget import Tweeget
import time
import json

try:
    tweeget = Tweeget('xxxxx', 'xxxxx')

    get_tweets = True
    next_page = None
    while get_tweets:
        json_return = tweeget.thirty_archive('(febre OR "falta de ar" OR tossindo OR tosse OR "dor de garganta" OR resfriado OR gripado) lang:pt place_country:BR place:"Rio de Janeiro"', \
                                             env = 'DEV', fromDate ='202003010000', toDate='202003280000', next_page = next_page)
        next_page = json_return['next']
        get_tweets = next_page is not None
        print(json_return)
        json_str = json.dumps(json_return['results'])
        ts = time.time()
        file_name ='data/' + str(ts) + '.json'
        with open(file_name, 'w') as f:
            f.write(json_str)
        time.sleep(0.5)
        json_str = json.dumps(json_return)
        ts = time.time()
        file_name = 'data/full/' + str(ts) + '.json'
        with open(file_name, 'w') as f:
            f.write(json_str)
except (Exception) as err:
    print(err)
```

