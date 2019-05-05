from flask import Flask
from flask import request
from flask import jsonify
from utils import *
import sqlite3
app = Flask(__name__)
db_filename = '/tmp/SourceScores.db'
connection = sqlite3.connect(db_filename, check_same_thread=False)
cursor = connection.cursor()

@app.route("/score")
def score():
    tweet = request.args.get("tweet")
    response = {"domain": "",
                "source": "",
                "bias": 0,
                "credibility": 0,
                "negative": 0,
                "manipulation": 1}
    urls = extract_urls(tweet)
    if (urls == []): #no URL was found
        return jsonify(response)
    domains = get_domains(urls)
    rows = extract_scores(domains[0])#connection.execute("SELECT * from scraped31 where domain_name = " + "\'www.cnn.com\'")
    #row = rows[0]#extract_scores(domains[0])#connection.execute("SELECT * from scraped31 where domain_name = " + domains[0])
    for row in rows:
        response["bias"] = row[3]
        response["credibility"] = row[2]
        response["source"] = row[0]
        response["domain"] = row[1]
    #response["bias"] = -2
    #response["credibility"] = 3
    #response["source"] = "CNN"
    #response["domain"] = domains[0]
    response["negative"] = sentiment_negative(tweet)
    response["manipulation"] = sentiment_manipulation(tweet)
    return str(response)

def extract_scores(domain_name):
    rows = connection.execute("SELECT * from scraped31 where domain_name = " + "\'www.cnn.com\'")
    return rows


if __name__ == "__main__":
    app.run()
