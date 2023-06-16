
import random

class Personne:
    def __init__(self, nom):
        self.nom = nom
        self.annee = None
        self.temps = None

def saisie():
    t = []
    while True:
        nom = input("Entrez le nom de la personne (ou 'q' pour quitter) : ")
        if nom == 'q':
            break
        personne = Personne(nom)
        t.append(personne)
    return t

def calcul_annee(personne, annee_min, annee_max):
    periode = input(f"Pour quelle période souhaitez-vous faire un voyage dans le temps, {personne.nom} ? (entre {annee_min} et {annee_max}) : ")
    periode = [int(x) for x in periode.split()]
    personne.annee = random.randint(periode[0], periode[1])

def calcul_temps(personne):
    personne.temps = abs(2017 - personne.annee) * 10

personnes = saisie()

annee_min = -10000
annee_max = 10000

for personne in personnes:
    calcul_annee(personne, annee_min, annee_max)
    calcul_temps(personne)

print("Résultats :")
for personne in personnes:
    print(f"Nom : {personne.nom}, Année : {personne.annee}, Temps nécessaire : {personne.temps} secondes")

print("Prendriez-vous ce risque ?")
