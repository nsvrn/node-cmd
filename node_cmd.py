from view import info, wallets, unspent, chainstate, mempool
import argparse
from threading import Thread
import util, external
 


def _args():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', nargs='?', const='info')
    return parser.parse_args()


def main():
    args = _args()
    cmd = util.get_conf('console')['default_view']
    
    if args.cmd:
        cmd = (args.cmd).lower()  
    
    if cmd == 'info':
        fetch_price = int(util.get_conf('stats')['enable_price_fetch'])
        if int(fetch_price) == 1: 
            external.save_price(run_forever=False)
            b = Thread(name='bg', daemon=True, target=external.save_price)
            b.start()
        info.load(fetch_price)    

    elif cmd == "wallets":
        wallets.load()
    elif cmd == 'unspent':
        unspent.load()
    elif cmd == 'chainstate':
        chainstate.load()
    elif cmd == 'mempool':
        mempool.load()
    


if __name__ == '__main__':
    main()