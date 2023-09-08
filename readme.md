### node-cmd
---

Command line tool that aggregates information from the Bitcoin RPC.

#### Setup
1. Clone and install requirements:
```
    git clone https://github.com/ns-xvrn/node-cmd.git &&
    cd node-cmd &&
    cp settings.conf.sample settings.conf &&
    pip install -r requirements.txt
```
2. Setup config file: edit the `settings.conf` file

---

#### info - live view
`python node_cmd.py info` or `python node_cmd.py`

![alt info](docs/info.png)

#### wallets summary
`python node_cmd.py wallets`

![alt wallets](docs/wallets.png)
