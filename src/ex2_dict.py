def afficher_profil_etudiant(etudiant: dict) -> None:
    """Affiche proprement les infos d'un étudiant."""
    print("Profil étudiant :")
    print(f"- Nom      : {etudiant.get('nom')}")
    print(f"- Prénom   : {etudiant.get('prenom')}")
    print(f"- Pays     : {etudiant.get('pays')}")
    print(f"- Ville FR : {etudiant.get('ville_france')}")
    print(f"- Filière  : {etudiant.get('filiere')}")
    print(f"- pather  :  {etudiant.get('pather')}")
    print(f"Voici l'ensemble des matieres de:' {etudiant.get('nom')}")
    for matiere in etudiant.get('modules'):
        print(matiere)
    
        
        
def main():
    listEtudiant = [{
        "nom": "Ngassam",
        "prenom": "Rodrigue",
        "pays": "Cameroun",
        "ville_france": "Paris",
        "filiere": "Informatique",
        "modules":["Java", "webMethods", "Python"]
    },
    {
        "nom": "Dassi",
        "prenom": "sophonie",
        "pays": "Cameroun",
        "ville_france": "Yaounde",
        "filiere": "Maths",
        "modules":["physiques", "chimie", "Télephones"]
    },
    {
        "nom": "Youmbi",
        "prenom": "Patrick",
        "pays": "Angleterre",
        "ville_france": "Chelsea",
        "filiere": "plantation",
        "modules":["IA", "Spring", "Java"]
    }]
    
    listEtudiant.append({
        "nom": "Ornelas",
        "prenom": "Tania",
        "pays": "espagne",
        "ville_france": "Chars",
        "filiere": "psychololgie",
        "modules":["Hotelerie", "espagnol", "psycho"]
    }
    )   
    
    for elt in listEtudiant:
        afficher_profil_etudiant(elt)
if __name__ == "__main__":
    main()