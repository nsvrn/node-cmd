from view import info, wallets, unspent, chainstate, mempool
import argparse
import util
 


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
        info.load()
    elif cmd == 'wallets':
        wallets.load()
    elif cmd == 'unspent':
        unspent.load()
    elif cmd == 'chainstate':
        chainstate.load()
    elif cmd == 'mempool':
        mempool.load()
    


if __name__ == '__main__':
    main()