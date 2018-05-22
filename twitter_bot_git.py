# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tweepy
from keys import keys
from get_response import response

#get keys
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

#authenticate 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#get trump tweets
statuses=api.user_timeline(id=INPUT ID)
inputs = [s.text for s in statuses]
ids=[s.id_str for s in statuses]
test_tweet=inputs[0]

#call function to generate response
tweet=response(test_tweet, ids[0])
#print(tweet)
#if haven't already responded to last tweet then respond
if tweet[0]=='True':
    status = api.update_status(status=tweet[1]) 
else:
    print('nothing tweeted')
