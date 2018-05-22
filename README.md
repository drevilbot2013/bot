# bot
# this is just an exercise in clustering language with kmeans, fitting to a tweet, and providing a similarly labeled tweet.
# there are three primary files: text_process, get_response, twitter_bot.
# text_process cleans and clusters text from austin power's movies and assigns labels to dr evil quotes
# get_response uses tweepy to get a series of tweets from a follower, assigns a label for most recent tweet based on text_process, 
# tests to see if a response has already been generated, tests if response has been used in the last 20 responses.  
# then returns a dr evil quote and a boolean to indicate if the bot has already replied
# twitter_bot interacts with API through tweepy.  it obtains latest tweets for input into get_response and then response tweet to API
