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

    user_id = req["session"]["user_id"]

    if req["session"]["new"]:
        responce["response"]["text"] = "Привет!"
    else:
        tokens = req["request"]["nlu"]["tokens"]
        if list(set(tokens) & {"оее", "oee", "эффективность" }) :
            responce["response"]["text"] = "Общая эфективность производства составила 50%"
        elif list(set(tokens) & {"план", "плановая"}) and list(set(tokens) & {"отгрузки", "отгрузка"}):
            responce["response"]["text"] = "План отгрузки на этот месяц составил 500 тысяч рублей до обвала курса"
        elif list(set(tokens) & {"сколько"}) and list(set(tokens) & {"станки", "обрудование", "станков"}) and list(set(tokens) & {"прерывание", "прерывании", "простое"}):
             responce["response"]["text"] = f"На прерывании 3 станка. Из них 1 в токарной группе и 2 во фрезерной"
        elif list(set(tokens) & {"какие"}) and list(set(tokens) & {"станки", "обрудование", "станков"}) and list(
                 set(tokens) & {"прерывание", "прерывании", "простое"}):
            responce["response"]["text"] = f"На прерывании станки M03 DMU eVo, L02 Twin 42, L10 Romi GL280"
        elif list(set(tokens) & {"людей", "человек", "персонала"}) and list(set(tokens) & {"работает", "работе", "цеху"}):
             responce["response"]["text"] = f"На данный момент на работе находится 5 человек"
        # elif list(set(tokens) & {"id"}):
        #     responce["response"]["text"] = f"id пользователя {user_id}"
        else:
            responce["response"]["text"] = "Не могу понять запрос. Попробуйте переформулировать"
    return json.dumps(responce)