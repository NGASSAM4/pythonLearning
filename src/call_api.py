import requests
import json

def main():
    url = "https://api.coindesk.com/v1/bpi/currentprice/EUR.json"

    try:
        resp = requests.get(url, timeout=10)
        print("HTTP status code:", resp.status_code)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("HTTP error:", e)
        return

    try:
        data = resp.json()
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        print("Raw response text:", resp.text[:500])
        return

    # Afficher les clés du JSON pour voir la structure réelle
    print("Top-level keys:", list(data.keys()))

    # Afficher la partie 'bpi' si elle existe
    if "bpi" in data:
        print("bpi keys:", list(data["bpi"].keys()))
    else:
        print("'bpi' key not found in JSON")

    # Essayer de récupérer les champs, mais en mode sécurisé
    try:
        rate = data["bpi"]["EUR"]["rate_float"]
        updated = data["time"]["updated"]
        print(f"Bitcoin price in EUR: {rate:.2f} € (updated: {updated})")
    except KeyError as e:
        print("KeyError, missing key in JSON:", e)
        print("Complete JSON:")
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()