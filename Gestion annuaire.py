# Partie 1: Gestion d'un annuaire

# Structure pour une personne dans l'annuaire
class Personne:
    def __init__(self, nom, prenom, numero, rue, telephone, code_postal, ville):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        self.rue = rue
        self.telephone = telephone
        self.code_postal = code_postal
        self.ville = ville

# Fonction pour saisir les informations de toutes les personnes dans l'annuaire
def saisie_tab():
    annuaire = []
    while True:
        nom = input("Nom: ")
        if nom == "":
            break
        prenom = input("Prénom: ")
        numero = input("Numéro dans la rue: ")
        rue = input("Nom de la rue: ")
        telephone = input("Numéro de téléphone: ")
        code_postal = input("Code postal: ")
        ville = input("Ville: ")

        personne = Personne(nom, prenom, numero, rue, telephone, code_postal, ville)
        annuaire.append(personne)

    return annuaire

# Fonction pour choisir le critère de recherche
def critere_recherche():
    choix = input("Choisissez le critère de recherche (nom, prénom, nom de rue, numéro de téléphone, code postal, ville): ")
    return choix

# Fonction de recherche dans l'annuaire
def recherche(annuaire, critere):
    recherche = input("Entrez la valeur de recherche: ")
    resultat = []
    for personne in annuaire:
        if critere == "nom" and personne.nom == recherche:
            resultat.append(True)
         critere == "prénom" and personne.prenom == recherche:
            resultat.append(True)
         critere == "nom de rue" and personne.rue == recherche:
            resultat.append(True)
         critere == "numéro de téléphone" and personne.telephone == recherche:
            resultat.append(True)
         critere == "code postal" and personne.code_postal == recherche:
            resultat.append(True)
         critere == "ville" and personne.ville == recherche:
            resultat.append(True)
        else:
            resultat.append(False)
    return resultat

# Procédure pour afficher les informations des personnes correspondant à la recherche
def affiche_tab(annuaire, resultat):
    for i in range(len(annuaire)):
        if resultat[i]:
            personne = annuaire[i]
            print(f"Nom: {personne.nom}")
            print(f"Prénom: {personne.prenom}")
            print(f"Numéro dans la rue: {personne.numero}")
            print(f"Nom de la rue: {personne.rue}")
            print(f"Numéro de téléphone: {personne.telephone}")
            print(f"Code postal: {personne.code_postal}")
            print(f"Ville: {personne.ville}")
            print()

# Partie 2: Récursivité

# Fonction récursive pour la division entière
def divinRec(a, b):
    if a < b:
        return 0
    else:
        return 1 + divinRec(a - b, b)

# Partie 3: Fichier

# Fonction pour compter le nombre de mots commençant par une voyelle dans un fichier
def nbMotsAvecVoyelle(nomf):
    count = 0
    with open(nomf, 'r') as file:
        for line in file:
            word = line.strip()
            if word[0] in ['a', 'e', 'i', 'o', 'u']:
                count += 1
    return count

# Procédure pour compter et écrire les occurrences de chaque mot unique dans un fichier
def compterChaqueMot(nomf1, nomf2):
    word_count = {}
    with open(nomf1, 'r') as file1:
        for line in file1:
            word = line.strip()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    with open(nomf2, 'w') as file2:
        for word, count in word_count.items():
            file2.write(f"{word} {count}\n")
