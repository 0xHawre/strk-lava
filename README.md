StarkNet RPC Data Fetcher
This Python script fetches block number data from specified StarkNet RPC endpoints. It makes repeated requests to the endpoints, logs the responses, and includes a timestamp for each request.

Prerequisites
Ensure you have Python and the requests package installed on your system.

Install Python
If Python is not already installed, you can install it using the following commands:

```bash 
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
```
Install Required Python Packages
Install the requests package using pip:
```bash 
pip3 install requests
```
Clone the Repository:
```bash 
git clone https://github.com/Hafxhak/strk-lava.git
cd strk-lava

```
Edit the Script:

Open the script in a text editor:
```bash
nano strk.py
```
Replace the placeholder URLs in the urls list with your own StarkNet RPC endpoint URLs. Example:

```bash 
urls = [
    "https://rpc.starknet.lava.build/lava-referer-your-unique-id/",  # replace with your RPC
    "https://rpc.starknet-testnet.lava.build/lava-referer-your-unique-id/",  # replace with your RPC
]
```
Save and exit the editor (for nano, press CTRL + X, then Y, and Enter).


Running the Script

Install and Use Screen:

Install screen to run the script in a detached session:

```bash
sudo apt install screen -y
screen -S starknet
```
Run the Script:

Execute the script using Python 3:
```bash
python3 strk.py
```
Example Output
The script will log the response from the RPC endpoint for each request. Example output:

```plaintext
StarkNet RPC response: {'jsonrpc': '2.0', 'id': 1, 'result': 12345}
```
Detach from the Screen Session:

Detach from the screen session without stopping the script by pressing CTRL + A, then D.



