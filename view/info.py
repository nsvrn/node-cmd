import time
from rich.live import Live
from rich.table import Table
from datetime import datetime as dtm
import util, rpc


def _table(data: dict, clr: str, updt_in:int):
    if data: 
        tbl = Table(show_header=False, show_lines=True)
        datestr = dtm.now().strftime('%a %b %-d')
        timestr = dtm.now().strftime('%-I:%M %p')        
        vlist, row = [], []
        vlist.append(['date', datestr, 'time', timestr])
        data['rpc.update_in'] = f'[{clr}]{updt_in}s'
        for k, v in data.items():
            row.append(k)
            row.append(v)
            if len(row) == 4:
                vlist.append(row)
                row = []
        for v in vlist: 
            tbl.add_row(v[0], f'[{clr}]{v[1]}', v[2], f'[{clr}]{v[3]}')
        return tbl
    

def get_data(is_txoutset):
    data = rpc.get_info(is_txoutset)
    return data


def load():
    cfg = util.get_conf('console')
    is_txoutset = bool(int(cfg['txoutset']))
    data = get_data(is_txoutset)
    clr = cfg['font_color']
    updt_in = int(cfg['rpc_update_freq'])
    with Live(_table(data, clr, updt_in), auto_refresh=False) as live:
        while(True):
            for i in range(updt_in, 0, -1):
                live.update(_table(data, clr, i), refresh=True)
                time.sleep(1)
            data = get_data(is_txoutset)
            live.update(_table(data, clr, updt_in), refresh=True)