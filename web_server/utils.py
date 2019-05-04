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
    """domains = []
    for url in url_list:
        parsed = urlparse(url).netloc
        if (parsed != None):
            toks = parsed.split(".")
            if (len(toks) == 3):
                toks.pop(0)
            domains.append(toks[0] + '.' + toks[1])
        else:
            domains.append(url)"""
    #return domains
    return [urlparse(url).netloc for url in url_list]

"""
Strips www. from either if it exists and compares urls.
"""
def match_urls(a, b):
    a_toks = a.split('.')
    b_toks = b.split('.')
    if (len(a_toks) == 3):
        a_toks.pop(0)
    if (len(b_toks) == 3):
        b_toks.pop(0)
    return a_toks == b_toks

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
    return 1
