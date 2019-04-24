from urllib.parse import urlparse
import re

"""
Extracts the first url if the tweet contains one. Currently, urls
must contain the protocol (http or https) in order to be recognized.
"""
def extract_urls(tweet_text):
    matches = re.finditer("(?P<url>https?://[^\s]+)", tweet_text)
    return [match.group("url") for match in matches]

"""
TODO
Obtains the domain name from a url, excluding the protocol.
"""
def get_domains(url_list):
    return [urlparse(url).netloc for url in url_list]

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
