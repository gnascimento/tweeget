from tweeget import Tweeget
import time
import json

try:
    tweeget = Tweeget('xxxxx', 'xxxxx')

    get_tweets = True
    next_page = 'eyJtYXhJZCI6MTIzODc3Mjc4ODc4MzE2OTUzNn0='
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

