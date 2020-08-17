import tweepy
import time

print("This is my twitter bot")

# Authenticate to Twitter
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


#Here it will likes first 20 posts by default
#if we want to like specific number of posts use count='countno' in home_timeline function
tweets = api.home_timeline()
for tweet in tweets:

    try:
            print("Tweet liked, posted by ", end='')
            print(tweet.user.name)
            tweet.favorite()
            time.sleep(1)
    except:
            print("Error! Please check")
