from rich.console import Console
from rich.table import Table
from rich.text import Text
import util, rpc


def _table(utxos: list, clr):
    if utxos and len(utxos) > 0: 
        tbl = Table(show_header=False)
        tbl.add_column('')
        tbl.add_column('')
        for k, v in utxos.items():
            tbl.add_row(k, f"[{clr}]{v}")
        return tbl
    

def load():
    console = Console()
    cfg = util.get_conf('console')
    console.print(Text('Standby, this may take a minute or two!', style='red italic'))
    utxos = rpc.get_chainstate()
    clr = cfg['font_color']
    tbl = _table(utxos, clr)
    console.print(tbl)
    