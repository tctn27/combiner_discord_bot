from flask import Flask, request
import json
import updater

app = Flask(__name__)


@app.route('/', methods=['POST'])
def foo():
    data = json.loads(request.data)
    print("New commit by: {}".format(data['commits'][0]['author']['name']))
    updater.run()
    return "OK"


if __name__ == '__main__':
    app.run()
