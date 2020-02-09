# Retweet and Like bot for Twitter, using Python and Tweepy.
# Search query via hashtag or keyword.
# Author: Joz-Bruer Quince
# Date: Friday, Feb 7th - 2020.
# License: MIT License.

import tweepy
import time

# Import in your Twitter application keys, tokens, and secrets.
# Make sure you add your own keys

API_Key = 'HiagdSG72jxVUBTYmn1RDqB4e'
API_SECRET_Key = 'KhVkn1vCNvZDs4rdYt8lBTQA3zxk2vVPqFNrMdSDKzTIGJtoIS'

ACCESS_TOKEN = '392341891-VQOG0xbITcYqyfQgC8sMqrcxTeJX0e3MUcwnHG6j'
ACCESS_TOKEN_SECRET = 'F0LsArgZtbM6Fc8cuEleKlt32Pna7mZImVVYDAfR0iBpc'


auth = tweepy.OAuthHandler(API_Key,API_SECRET_Key)

auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

api = tweepy.API(auth)

user = api.me()
print(user.screen_name)


search = ("Cristiano Ronaldo")
nbOfTweets = 40

for tweet in tweepy.Cursor(api.search,search).items(nbOfTweets):

    try:

        tweet.favorite()
        print('Tweet Liked')
        tweet.retweet()
        print('Tweet Retweeted')
        time.sleep(3)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# search2 = ("Javascript")
# nbOfTweets2 = 20

# for tweet in tweepy.Cursor(api.search,search2).items(nbOfTweets2):

#     try:

#         tweet.favorite()
#         print('Tweet Liked')
#         tweet.retweet()
#         print('Tweet Retweeted')
#         time.sleep(3)
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break

