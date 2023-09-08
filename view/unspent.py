from rich.console import Console
from rich.table import Table
import util, rpc


def _table(data: list, clr):
    if data and len(data) > 0: 
        tbl = Table(show_header=True)
        cols = ['wallet', 'vout', 'amount', 'confirmations', 'spendable', 'reused', 'txid']
        for c in cols: tbl.add_column(c)
        for wallet, unspent_list in data:
            for w in unspent_list:
                tbl.add_row(f"[{clr}]{wallet}", f"[{clr}]{w['vout']}", f"[{clr}]{w['amount']}", 
                            f"[{clr}]{w['confirmations']}", f"[{clr}]{w['spendable']}", 
                            f"[{clr}]{w['reused']}", f"[{clr}]{w['txid']}")
        return tbl
    

def load():
    cfg = util.get_conf('console')
    data = rpc.get_unspent()
    clr = cfg['font_color']
    console = Console()
    tbl = _table(data, clr)
    console.print(tbl)
    