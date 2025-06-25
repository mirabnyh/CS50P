import json
import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    n = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=dba9bb2657da5b357487ae1e647f3b1aeb9891dd91d6720db527bbea245fed4c")

    o = response.json()
    data = o["data"]
    price = float(data["priceUsd"])
    amount = n * price
    print(f"${amount:,.4f}")
except (requests.RequestException,ValueError):
    sys.exit("Command-line argument is not a number")
