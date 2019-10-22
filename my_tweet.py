import tweepy
# KEYの指定
CONSUMER_KEY = '************'
CONSUMER_SECRET = '************'
ACCESS_TOKEN = '************'
ACCESS_TOKEN_SECRET = '************'
# tweepyの設定
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#ツイートの実行
api.update_status("hello world from python")