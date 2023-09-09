from rich.console import Console
from rich.table import Table
import util, rpc


def _table(mp: list, clr):
    if mp and len(mp) > 0: 
        tbl = Table(show_header=True)
        cols = ['name', 'balance', 'unconf_bal', 'txcount', 'pk_enabled', 'avoid_reuse']
        for c in cols: tbl.add_column(c)
        for w in mp:
            tbl.add_row(f"[{clr}]{w['walletname']}", f"[{clr}]{w['balance']}", f"[{clr}]{w['unconfirmed_balance']}", 
                        f"[{clr}]{w['txcount']}", f"[{clr}]{w['private_keys_enabled']}", f"[{clr}]{w['avoid_reuse']}")
        return tbl
    

def load():
    cfg = util.get_conf('console')
    mp = rpc.get_mempool(verbose=True)
    clr = cfg['font_color']
    console = Console()
    tbl = _table(mp, clr)
    console.print(tbl)
    