import util
import json, requests



def get_rpc(method, params=[], wallet=None):
    conf = util.get_conf('rpc')    
    url = f"http://{conf['user']}:{conf['password']}@{conf['ip']}:{conf['port']}"
    if wallet: url += f'/wallet/{wallet}'
    headers = {'content-type': 'application/json'}
    payload = json.dumps({"method": method, "params": params, "jsonrpc": "2.0", "id":"node-dash"})
    response = requests.post(url, headers=headers, data=payload).json()
    if response['error']:
        raise Exception(response['error'])
    else:
        return response['result']

def get_mempool(verbose=False, sequence=False):
    params = [verbose, sequence]
    result = get_rpc('getrawmempool', params)
    return result

def get_info(is_txoutset=False):
    info = {}
    # blockchain
    bc = get_rpc('getblockchaininfo')
    info['chain'] = bc['chain']
    info['blocks'] = f"{int(bc['blocks']):,}"
    info['difficulty'] = f"{int(bc['difficulty']/1e12)}T"
    info['node.size'] = f"{int(bc['size_on_disk']/(1024**3))} GB"
    # network
    nt = get_rpc('getnetworkinfo')
    info['node'] = f"v{nt['version']}"
    info['connections'] = nt['connections']
    # mempool
    mp = get_rpc('getmempoolinfo')
    info['mempool.size'] = f"{mp['size']:,}"
    info['mempool.bytes'] = f"{int(mp['bytes']/(1024**2))} MB"
    info['mempool.total_fee'] = round(float(mp['total_fee']), 4)
    # wallets
    wallets = get_rpc('listwallets')
    info['wallet_count'] = len(wallets)
    balance = 0
    for w in wallets:
        wt = get_rpc('getwalletinfo', wallet=w)
        balance += float(wt['balance'])
    info['total_sats'] = f"{int(balance * 100e6):,}"

    # gettxoutsetinfo : global utxo set stats/chainstate
    # NOTE: This is too slow without coinstatsindex enabled
    if is_txoutset:
        ux = get_rpc('gettxoutsetinfo')
        info['utxo.count'] = f"{ux['txouts']:,}"
        info['utxo.total_amt'] = round(float(ux['total_amount']), 4)
        info['utxo.txs'] = f"{ux['transactions']:,}"
        info['utxo.size'] = f"{int(ux['disk_size']/(1024**3))} GB"

    return info

