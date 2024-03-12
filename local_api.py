from rpc import get_rpc
import json
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
    bc = get_rpc('getblockchaininfo')
    info = {}
    info['blocks'] = int(bc['blocks'])
    info['node_size'] = int(bc['size_on_disk'])
    nh = get_rpc('getnetworkhashps', [100])
    info['hashrate'] = int(nh)
    info['difficulty'] = int(bc['difficulty'])
    fe = get_rpc('estimatesmartfee', [6])
    info['fee'] = int(fe['feerate'] * 100e6 / 1000)
    info['price'] = get_price()
    return info


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=False)