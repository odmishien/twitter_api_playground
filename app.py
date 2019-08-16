from requests_oauthlib import OAuth1Session
import os
import config
import json

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
screen_name = str(input("Your screen name > "))

params = {'count': 100, 'screen_name': screen_name}
req = twitter.get(url, params=params)

if req.status_code == 200:
    tl = json.loads(req.text)
    for tweet in tl:
        print(tweet['user']['name']+'::'+tweet['text'])
        print(tweet['created_at'])
        print('----------------------------------------------------')
else:
    print("ERROR: %d" % req.status_code)
