def afficher_notes(notes: list[float]) -> None:
    """Affiche chaque note et la moyenne."""
    if not notes:
        print("Aucune note fournie.")
        return

    total = 0
    for n in notes:
        print(f"- note: {n}")
        total += n

    moyenne = total / len(notes)
    print(f"Moyenne: {moyenne:.2f}")


def main():
    notes = [12.5, 15.0, 9.5, 17.0, 13.0]
    afficher_notes(notes)
    reponse_clavier=False
    while True:
        note = input("ajouter une nouvelle note: ")
        if isinstance(float(note),float):
            reponse_clavier=True
            notes.append(float(note))
            afficher_notes(notes)
            break
        else:
            reponse_clavier=False

if __name__ == "__main__":
    main()