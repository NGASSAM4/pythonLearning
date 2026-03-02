import json

def main():
    # 1. Exemple de dictionnaire Python
    student = {
        "name": "Rodrigue",
        "country": "Cameroon",
        "city_france": "Chars",
        "skills": ["webMethods", "MuleSoft", "Python"]
    }

    # 2. Convertir en JSON (string)
    json_str = json.dumps(student, ensure_ascii=False, indent=2)
    print("JSON string:")
    print(json_str)

    # 3. Sauvegarder dans un fichier
    with open("student.json", "w", encoding="utf-8") as f:
        f.write(json_str)

    # 4. Relire le fichier JSON
    with open("student.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print("\nLoaded from file:")
    print("Name:", data["name"])
    print("Skills:", ", ".join(data["skills"]))

if __name__ == "__main__":
    main()