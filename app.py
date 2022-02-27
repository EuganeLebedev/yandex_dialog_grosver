import json

from flask import Flask, request
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def main():
    logging.info(request.json)
    responce = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False
        }
    }

    req = request.json
    if req["session"]["new"]:
        responce["response"]["text"] = "Привет!"
    return json.dumps(responce)