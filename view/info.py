import time, json
from rich.live import Live
from rich.table import Table
from datetime import datetime as dtm
import util, rpc
from pathlib import Path
from datetime import datetime

next_price_up_at = None

def _table(data: dict, clr: str, updt_in:int):
    if data: 
        tbl = Table(show_header=False, show_lines=True)
        datestr = dtm.now().strftime('%a %b %-d')
        timestr = dtm.now().strftime('%-I:%M %p')        
        vlist, row = [], []
        vlist.append(['date', datestr, 'time', timestr])
        data['rpc.update_in'] = f'[{clr}]{updt_in}s'
        for idx, k in enumerate(data):
            v = data[k]
            row.append(k)
            row.append(v)
            if len(row) == 4 or idx == len(data) - 1:
                vlist.append(row)
                row = []
        for v in vlist: 
            if len(v) == 4:
                tbl.add_row(v[0], f'[{clr}]{v[1]}', v[2], f'[{clr}]{v[3]}')
            elif len(v) == 2:
                tbl.add_row(v[0], f'[{clr}]{v[1]}')                
        return tbl
    

def get_data(fetch_price):
    data = rpc.get_info()
    f = Path(__file__).parents[1] / 'ext_data.json'
    if fetch_price == 1 and f.exists():
        delay = int(util.get_conf('stats')['price_fetch_delay'])
        ext = json.loads(f.read_text(encoding='UTF-8'))
        data['usd_price'] = f"${ext['price']:,}"
        data['last_price'] = (datetime.fromtimestamp(ext['timestamp'])).strftime('%-I:%M %p')

    return data


def load(fetch_price):
    cfg = util.get_conf('console')
    data = get_data(fetch_price)
    clr = cfg['font_color']
    updt_in = int(cfg['rpc_update_freq'])
    with Live(_table(data, clr, updt_in), auto_refresh=False) as live:
        while(True):
            for i in range(updt_in, 0, -1):
                live.update(_table(data, clr, i), refresh=True)
                time.sleep(1)
            data = get_data(fetch_price)
            live.update(_table(data, clr, updt_in), refresh=True)