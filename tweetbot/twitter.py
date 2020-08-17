import tweepy
import time
 
auth = tweepy.OAuthHandler('ux72OXYlQagWU8a1cJmIQ3lz4','KsWYjVX1oW33U0Cg2jAOcc6khnEoCermG5TWREb2yzHuUDBjpX')
auth.set_access_token('911260629796716544-fB4lzp5GLlZcVJD7mcCfItUe14tiAgj','ICOJji5QYl7C61wKpzxd8QQvqQ2kpNiUgz7L3dBdRk7aq')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '#hashtag'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('tweet liked')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
         print(e.reason)
    except StopIteration:
         break

