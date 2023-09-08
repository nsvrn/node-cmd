from view import info
import argparse
 


def _args():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', nargs='?', const='info')
    return parser.parse_args()


def main():
    args = _args()
    cmd = 'info'
    if args.cmd:
        cmd = (args.cmd).lower()  
    if cmd == 'info':
        info.load()
    elif cmd == 'wallets':
        pass #TODO
    elif cmd == 'myutxos':
        pass #TODO
    elif cmd == 'mempool':
        pass #TODO
    


if __name__ == '__main__':
    main()