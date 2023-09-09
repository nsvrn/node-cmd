### node-cmd
---

Command line tool that aggregates information from the Bitcoin RPC.

#### Setup
1. *Don't trust, verify*: audit the code thoroughly.
2. Clone and install requirements:
```
    git clone https://github.com/ns-xvrn/node-cmd.git &&
    cd node-cmd &&
    cp settings.conf.sample settings.conf &&
    pip install -r requirements.txt
```
3. Setup config file: edit the `settings.conf` file
4. You can add an alias in your `.bashrc` and run `source .bashrc`:

`alias nodecmd="python3 /path/to/node-cmd/node_cmd.py`"

---

#### info - live view
`python node_cmd.py info` or `python node_cmd.py`

NOTE: only price fetch is a non Bitcoin rpc fetch, you can disable it in `settings.conf` with `enable_price_fetch=0`

![alt info](docs/info.png)

#### chainstate (utxo summary)
`python node_cmd.py chainstate`

![alt chainstate](docs/chainstate.png)

#### wallets summary
`python node_cmd.py wallets`

![alt wallets](docs/wallets.png)

#### unspent (wallet utxos)
`python node_cmd.py unspent`

![alt unspent](docs/unspent.png)


#### rpc calls:
- RPC calls [ref](https://developer.bitcoin.org/reference/rpc/)
- Passes through RPC calls and returns the json response as-is

`python node_cmd.py rpc -method=getblockchaininfo`

`python node_cmd.py rpc -rpcwallet=test -method=getwalletinfo`

`python node_cmd.py rpc -method=estimatesmartfee -params=[1]`

![alt rpc](docs/rpc.png)