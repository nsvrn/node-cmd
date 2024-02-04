import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
from rpc import get_rpc
import pickle
from tqdm import tqdm
from loguru import logger
# from bitcoin.core import CTransaction


FPATH = Path(__file__).parents[0] / f'mempool.pickle'

def get_mempool_txs(limit=None):
    tx_ids = get_rpc('getrawmempool')
    txs = {}
    logger.info(f'{len(tx_ids)} txs found in mempool')
    for txid in tqdm(tx_ids):
        tx = get_rpc('getrawtransaction', f'{txid},2')
        txs[txid] = tx
        if limit and len(txs) == limit: break
    return txs


def save_mempool_txs(limit=None):
    txs = get_mempool_txs(limit)
    with open(FPATH, 'wb') as handle:
        pickle.dump(txs, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_mempool_txs():
    with open(FPATH, 'rb') as handle:
        txs = pickle.load(handle)
    # TODO
    pass
    

if __name__ == '__main__':
    save_mempool_txs(limit=None)
    # load_mempool_txs()