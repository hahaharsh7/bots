import tweepy
import time


consumer_key='GW0UnfVMcwDlCgQr7q1CI2j8q'
consumer_secret='ZiAJytJ1xKCQal256dl0itnRlUWTcCxRkeN0Zz2KiKP52Aw25F'

key='1288846695275454464-RaXEre4yzD464NDuASoCwSJO1222X1'
secret='n3b7VxohXNTUyPyamUwfjHSqVOtbxTDhazNCOOGipCmiY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

search="freecodecamp"
nrTweets=20

for tweet in tweepy.cursor(api.search,search).items(nrTweets):
	try:
		print("tweet liked")
		tweet.favorite()
		time.sleep(10)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break