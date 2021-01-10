import tweepy
import time

tw_keys = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token_key': '',
    'access_token_secret': ''
}

auth = tweepy.OAuthHandler(tw_keys['consumer_key'], tw_keys['consumer_secret'])
auth.set_access_token(tw_keys['access_token_key'], tw_keys['access_token_secret'])

api = tweepy.API(auth)

dp, comparisons = "DailyProgress", ["NewsAndRecord", "RoanokeTimes", "TucsonStar", "HeraldCourier"]

def rt_tweets(comparisons):
    dp_tweets = api.user_timeline(screen_name="DailyProgress",
                                  count=10,
                                  include_rts=False,
                                  tweet_mode='extended')

    time.sleep(300)

    compare_tweets = []

    for compare in comparisons:
        cmp_twts =  api.user_timeline(screen_name=compare,
                                        count=50,
                                        include_rts=False,
                                        tweet_mode='extended')

        for tweet in cmp_twts:
            compare_tweets.append(tweet.full_text.split('https://t.co')[0])

    for tweet in dp_tweets:
        if tweet.full_text.split('https://t.co')[0] not in compare_tweets:
            try:
                api.retweet(tweet.id)
            except tweepy.TweepError as e:
                print(e)
                continue


def handler(event, context):
    rt_tweets(comparisons)
