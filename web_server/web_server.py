from flask import Flask
from flask import request
from flask import jsonify
from utils import *
app = Flask(__name__)

@app.route("/score")
def score():
    tweet = request.args.get("tweet")
    response = {"domain": None,
                "bias": 0,
                "credibility": 0,
                "negative": 0,
                "manipulation": 0,
                "success": False}
    url = extract_url(tweet)
    if (url == None): #no URL was found
        return jsonify(response)
    domain = get_domain(url)
    response["domain"] = domain
    success = False
    #query database for scores using domain and set scores/success accordingly
    success = True #simulating successful database access
    if (success):
        response["success"] = True
    response["negative"] = sentiment_negative(tweet)
    response["manipulation"] = sentiment_manipulation(tweet)
    return jsonify(response)

if __name__ == "__main__":
    app.run()
