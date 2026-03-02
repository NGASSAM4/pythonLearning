def afficher_profil_etudiant(etudiant: dict) -> None:
    """Affiche proprement les infos d'un étudiant."""
    print("Profil étudiant :")
    print(f"- Nom      : {etudiant.get('nom')}")
    print(f"- Prénom   : {etudiant.get('prenom')}")
    print(f"- Pays     : {etudiant.get('pays')}")
    print(f"- Ville FR : {etudiant.get('ville_france')}")
    print(f"- Filière  : {etudiant.get('filiere')}")
    print(f"- pather  :  {etudiant.get('pather')}")

        
def somme(liste):
    _somme = 0
    for i in liste:
        _somme = _somme + i
    return _somme
        
def calcule_moyene_etudiant(etudiant: dict) -> float:
    moyenne=0.0
    notes=[]
    listeMat= list(etudiant.get('modulesNotes'))
    if len(listeMat) !=0 :
        notes=[(etudiant.get('modulesNotes'))[tel] for tel in listeMat]
   #     for cle in list[etudiant.get('modulesNotes')]:
   #         notes.append(etudiant.get('modulesNotes')[cle])
        moyenne= somme(notes)/len(notes)
    print("L'ETUDIANT:")
    print(f"- Nom      : {etudiant.get('nom')}")
    print(f"- Prénom   : {etudiant.get('prenom')}")
    print("A OBTENU UNE MOYENNE DE : "+ str(moyenne))
    return  moyenne
    
def affiche_moyene_generale(moyenneParEleve:list[float])-> float:
    return somme(moyenneParEleve)/len(moyenneParEleve)
        
    
    
        
        
def main():
    listEtudiant = [{
        "nom": "Ngassam",
        "prenom": "Rodrigue",
        "pays": "Cameroun",
        "ville_france": "Paris",
        "filiere": "Informatique",
        "modulesNotes":{"Java":14,"webMethods":15,"Python":12}
    },
    {
        "nom": "Dassi",
        "prenom": "sophonie",
        "pays": "Cameroun",
        "ville_france": "Yaounde",
        "filiere": "Maths",
        "modulesNotes":{"physiques":10, "chimie":17, "Télephones":20}
    },
    {
        "nom": "Youmbi",
        "prenom": "Patrick",
        "pays": "Angleterre",
        "ville_france": "Chelsea",
        "filiere": "plantation",
        "modulesNotes":{"IA":13, "Spring":19, "Java":18}
    }]
    
    listeMoyInd=[]
    for elt in listEtudiant:
        listeMoyInd.append(calcule_moyene_etudiant(elt))  
    print('la moyenne générale est :'+ str((affiche_moyene_generale(listeMoyInd))))
        
    
if __name__ == "__main__":
    main()