print("Bienvenue dans dans Softcore AI chat bot, la pour repondre a tes questions")

# Dictionnaire avec les sujets disponnible
sujet = {
    "ia": "cool l ia c stylé et cool",
    "sport": " bon pour la santé",
    "argent": "ultra important mec",
    "voiture": "supercar etc c incroyable",
    "mclaren": "meilleur marque de voiture",
    "lambo": "oe cool aussi comme marque",
    "entreprenariat": "stylé",
    "santé": "une des choses les plus precieuses"
}

# Boucle de discussion
while True:
    sujet_utilisateurs = input("De quoi veut tu parler[tape stop pour quitter]").lower().strip()

    if sujet_utilisateurs == "stop":
        print("Au revoir")
        break

    elif sujet_utilisateurs in sujet:
        print(sujet[sujet_utilisateurs])

    else:
        print("je ne peux pas en discuter")