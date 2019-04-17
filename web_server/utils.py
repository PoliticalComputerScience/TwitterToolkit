from urllib.parse import urlparse
import re

"""
Extracts the first url if the tweet contains one. Currently, urls
must contain the protocol (http or https) in order to be recognized.
"""
def extract_url(tweet_text):
    match = re.search("(?P<url>https?://[^\s]+)", tweet_text)
    if (match != None):
        return match.group("url")
    else:
        return None

"""
TODO
Obtains the domain name from a url, excluding the protocol.
"""
def get_domain(url):
    return url

"""
TODO
Produces a negativity score for a tweet using sentiment analysis.
"""
def sentiment_negative(tweet):
    return 0

"""
# TODO
Produces a manipulation score for a tweet using sentiment analysis.
"""
def sentiment_manipulation(tweet):
    return 0
