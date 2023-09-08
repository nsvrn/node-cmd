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

def get_info():
    info = {}
    
    # blockchain
    bc = get_rpc('getblockchaininfo')
    info['chain'] = bc['chain']
    info['blocks'] = f"{int(bc['blocks']):,}"
    info['node.size'] = f"{int(bc['size_on_disk']/(1024**3))} GB"
    
    # network
    nt = get_rpc('getnetworkinfo')
    info['node'] = f"v{nt['version']}"
    info['connections'] = nt['connections']
    
    # hashrate
    nh = get_rpc('getnetworkhashps', [100])
    info['hashrate'] = f"{int(nh/1e18)} EH/s"

    info['difficulty'] = f"{int(bc['difficulty']/1e12)}T"
    
    # mempool
    mp = get_rpc('getmempoolinfo')
    info['mempool.count'] = f"{mp['size']:,}"
    info['mempool.size'] = f"{int(mp['bytes']/(1024**2))} MB"
    info['mempool.total_fee'] = round(float(mp['total_fee']), 4)
    
    # wallets
    wcount, wtotal = get_wallets(True)
    info['wallet_count'] = wcount
    info['total_balance'] = f"{wtotal}"

    # estimated fee
    # outputs in BTC/kvB
    n = int(util.get_conf('console')['fee_estimate_blocks'])
    fe = get_rpc('estimatesmartfee', [n])
    info['fee_estimate'] = f"{int(fe['feerate'] * 100e6 / 1000)} s/vB"
    
    return info


def get_wallets(only_summary=False):
    wallets = get_rpc('listwallets')    
    balance = 0
    wallet_info = []
    for w in wallets:
        wt = get_rpc('getwalletinfo', wallet=w)
        balance += float(wt['balance'])
        wallet_info.append(wt)
    if only_summary:
        return len(wallets), balance
    else:
        return wallet_info


def get_unspent():
    wallets = get_rpc('listwallets')    
    wallet_info = []
    for w in wallets:
        utxos = get_rpc('listunspent', wallet=w)
        utxos = sorted(utxos, reverse=True, key=lambda x: x['amount'])
        if utxos: wallet_info.append((w, utxos))
    return wallet_info
    

def get_chainstate():
    ux = get_rpc('gettxoutsetinfo')
    info = {}
    info['utxo.count'] = f"{ux['txouts']:,}"
    info['utxo.total_amt'] = f"{int(ux['total_amount']):,}"
    info['utxo.txs'] = f"{ux['transactions']:,}"
    info['utxo.size'] = f"{round(ux['disk_size']/(1024**3),1)} GB"
    return info
