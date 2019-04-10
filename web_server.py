from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route("/get_url")
def get_url():
    return request.args.get("url")

if __name__ == "__main__":
    app.run()
