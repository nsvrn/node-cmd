import rpc, json
from external import get_price
from flask import Flask

app = Flask(__name__)

@app.route("/")
def info():
    return to_json(get_info())


def to_json(dict):
    response = app.response_class(
        response=json.dumps(dict),
        mimetype='application/json'
    )
    return response

def get_info():
    info = rpc.get_info()
    info['price'] = get_price()
    return info


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=False)