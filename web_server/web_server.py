from flask import Flask
from flask import request
from flask import jsonify
from utils import *
app = Flask(__name__)

@app.route("/score")
def score():
    tweet = request.args.get("tweet")
    response = {"domain": "",
                "bias": 0,
                "credibility": 0,
                "negative": 0,
                "manipulation": 0,
                "success": str(False)}
    urls = extract_urls(tweet)
    if (urls == []): #no URL was found
        return jsonify(response)
    domains = get_domains(urls)
    success = False
    #query database for scores using domain and set scores/success accordingly for all links
    success = True #simulating successful database access
    if (success):
        response["success"] = str(True)
    response["domain"] = domains[0]
    response["negative"] = sentiment_negative(tweet)
    response["manipulation"] = sentiment_manipulation(tweet)
    return str(response)#jsonify(response)#jsonify(response)

if __name__ == "__main__":
    app.run()
