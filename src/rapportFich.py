from pathlib import Path

def main():
    # 1. Demander un chemin de fichier à l'utilisateur
    chemin_str = input("Chemin du fichier texte à lire : ").strip()
    chemin = Path(chemin_str)

    if not chemin.is_file():
        print("Fichier introuvable :", chemin)
        return

    # 2. Lire le contenu
    contenu = chemin.read_text(encoding="utf-8")

    # 3. Compter les lignes et les mots
    lignes = contenu.splitlines()
    nb_lignes = len(lignes)
    nb_mots = len(contenu.split())

    # 4. Écrire un petit rapport dans un nouveau fichier
    rapport = (
        f"Fichier analysé : {chemin}\n"
        f"Nombre de lignes : {nb_lignes}\n"
        f"Nombre de mots   : {nb_mots}\n"
    )

    rapport_path = chemin.with_suffix(".rapport.txt")
    rapport_path.write_text(rapport, encoding="utf-8")

    print("Rapport écrit dans :", rapport_path)

if __name__ == "__main__":
    main()
    