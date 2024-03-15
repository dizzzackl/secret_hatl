from flask import Flask, request
import requests


app = Flask(__name__)
message_list = []
@app.route('/', methods=['GET', 'POST'])
def message():
    name = request.json["name"]
    messsage = request.json["message"]
    result = f"{name} : {messsage} \n"
    message_list.append(result)
    return '\n'.join(message_list)


if __name__ == '__main__':
    app.run()
