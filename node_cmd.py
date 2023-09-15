from view import info, wallets, unspent, chainstate, fees
import argparse, json
from threading import Thread
import util, external, rpc
 


def _args():
    cmd_choices = ['info', 'wallets', 'unspent', 'chainstate', 'settings', 'fees']
    parser = argparse.ArgumentParser(prog='nodecmd')
    subparser = parser.add_subparsers(help='types of cmd', dest='cmd')
    for c in cmd_choices:
        subparser.add_parser(c)
    rpc_sp = subparser.add_parser('rpc')
    rpc_sp.add_argument('-rpcwallet', required=False, help='use specific wallet')
    rpc_sp.add_argument('-method', required=True, nargs='?', default='', help="rpc method name")
    rpc_sp.add_argument('-params', required=False, type=json.loads, help="rpc method params separated by commas")
    return parser.parse_args()


def main():
    args = _args()
    
    if args.cmd:
        cmd = args.cmd.lower()
    else:
        cmd = util.get_conf('console')['default_view']

    if cmd == 'settings':
        util.load_settings()        
    elif cmd == 'info':
        fetch_price = int(util.get_conf('info')['enable_price_fetch'])
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
    elif cmd == 'fees':
        fees.load()
    elif cmd == 'rpc':
        params = args.params if args.params else []
        output = rpc.get_rpc(args.method, params, args.rpcwallet)
        if type(output) == dict and 'code' in output and output['code'] == -1:
            err = str(output)
            err = err.replace('\\n', '\n')
            err = err.replace('\\t', '\t')
            print(err)
        else:
            print(json.dumps(output, indent=2, sort_keys=False))
    


if __name__ == '__main__':
    main()