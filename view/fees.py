from rich.console import Console
from rich.table import Table
import util, rpc


def _table(data: dict, clr):
    if data and len(data) > 0: 
        tbl = Table(show_header=True)
        cols = ['target_blocks', 'fees']
        for c in cols: tbl.add_column(c)
        for key, value in data.items():
            tbl.add_row(f"[{clr}]{key}", f"[{clr}]{value}")
        return tbl
    

def load():
    cfg = util.get_conf('console')
    fees_dict = {1:None, 6:None, 36:None, 144:None}
    for key in fees_dict.keys():
        r = rpc.get_rpc(method='estimatesmartfee', params=[key])
        fees_dict[key] = f"{int(r['feerate'] * 100e6 / 1000)} s/vB"
    clr = cfg['font_color']
    console = Console()
    tbl = _table(fees_dict, clr)
    console.print(tbl)
    