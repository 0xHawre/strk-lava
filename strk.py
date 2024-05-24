import requests
import random
import time

def call_rpc_starknet(url):
    try:
        response = requests.post(url, json={"jsonrpc": "2.0", "id": 1, "method": "starknet_blockNumber"})
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error in StarkNet RPC: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error in StarkNet RPC: {e}")
    return None

if __name__ == "__main__":
    urls = [
        "https://rpc.starknet.lava.build/lava-referer-b3ebd262-006d-4555-8273-6d1508c4e92d/",
        "https://rpc.starknet-testnet.lava.build/lava-referer-b3ebd262-006d-4555-8273-6d1508c4e92d/",
    ]

    while True:
        for url in urls:
            response = call_rpc_starknet(url)
            if response:
                print(f"StarkNet RPC response: {response}")
            time.sleep(random.uniform(0.1, 0.5))
