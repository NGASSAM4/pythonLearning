import requests

def main():
    name = "rodrigue"
    url = f"https://api.agify.io?name={name}"
    
    try:
        resp = requests.get(url, timeout=10)
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
    # Exemple de réponse: {"name":"rodrigue","age":34,"count":1234}

    print("Raw JSON:", data)
    predicted_age = data.get("age")
    count = data.get("count")

    print(f"Name: {name}, predicted age: {predicted_age}, based on {count} samples")

if __name__ == "__main__":
    main()