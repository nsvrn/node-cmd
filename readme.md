### node-cmd
---

Command line tool that aggregates information from the Bitcoin RPC.

#### Setup
1. *Don't trust, verify*: audit the code thoroughly.
2. Clone and install requirements:
```
    git clone https://github.com/ns-xvrn/node-cmd.git &&
    cd node-cmd &&
    pip install -r requirements.txt
```
3. You can add an alias in your `.bashrc` and run `source .bashrc`:

`alias nodecmd="python3 /path/to/node-cmd/node_cmd.py"`

4. The first time your run it, it will automatically copy `settings.conf.sample` and open `settings.conf` in `vim`,
<br>make sure to setup the RPC settings correctly. 
<br>Thereafter you can edit conf using `nodecmd settings` command when needed.

---

#### info - live view (auto-refreshes)

NOTE: only price fetch is a non Bitcoin rpc fetch, you can disable it in `settings.conf` with `enable_price_fetch=0`

`nodecmd` or `nodecmd info`

![alt info](docs/info.png)

#### chainstate (utxo summary)

![alt chainstate](docs/chainstate.png)

#### wallets summary

![alt wallets](docs/wallets.png)

#### unspent (wallet utxos)

![alt unspent](docs/unspent.png)

#### fees (estimatesmartfees for target n blocks)
![alt fees](docs/fees.png)


#### rpc calls:
- RPC calls [ref](https://developer.bitcoin.org/reference/rpc/)
- Passes through RPC calls and returns the json response as-is
- Pass multiple parameters as comma-separated string (strings in double quotes, numerics without quotes)
- Example 1: `nodecmd rpc -method=getblockchaininfo`
- Example 2: `nodecmd rpc -rpcwallet=test -method=getwalletinfo`
- Example 3: `nodecmd rpc -method=estimatesmartfee -params=1`
- Example 4: `nodecmd rpc -method=getmempoolentry -params="9b0b033ddd5ebe5f6a78cedb2432e33d2e739ff04d59278017298564391272fb"`

![alt rpc](docs/rpc.png)