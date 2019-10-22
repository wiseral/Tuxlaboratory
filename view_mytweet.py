import tweepy

# KEYの指定
CONSUMER_KEY = '************'
CONSUMER_SECRET = '************'
ACCESS_TOKEN = '************'
ACCESS_TOKEN_SECRET = '************'

auth = tweepy.OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)