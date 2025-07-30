import tweepy

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
bearer_token = "YOUR_BEARER_TOKEN"

client = tweepy.Client(bearer_token=bearer_token)

query = "OpenAI -is:retweet lang:en"
tweets = client.search_recent_tweets(query=query, max_results=10)

for tweet in tweets.data:
    print(tweet.text)
