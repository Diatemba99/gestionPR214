"""
module pour la gestion des seances
"""
from datetime import datetime
import time

now = datetime.now()
date = now.strftime("%Y-%m-%d")

#liste pour toutes les donnees d'une séance
dico_seance = []

#liste pour la liste de présence
etudiants_presents = []

#liste pour les donnees a afficher
list_seance = []

def ajoutSeance():
   idseance = "seance" + now.strftime("%Y-%m-%d") 
   dateSeance = now.strftime("%Y-%m-%d")
   heureDebut = now.strftime("%H:%M")
   numeroSeance = input("Saisir numero de la seance: ")
   heureFin= input("Saisir heure de Fin de la seance ex:[18:58]: ")
   NomModule_seance = input("Saisir nom de module : ")
   NomSalle = input("Saisir le nom de la salle : ")
   NomProfesseur = input("Saisir nom complet du professeur : ")
   heureTotalModule = input('Saisir heures totales module : ')
   heureRestantModule = input('Saisir heures restantes module : ')
   numChapitre = input("Saisir le numero du chapitre : ")
   titreChapitre = input("Saisir le Titre du chapitre : ")
   objetifs = input("Objetifs pedagogiques du cours : ")
   #creer une fonction pour ajouter les etudiants presents
   def liste_presence():
        nombre = input("Saisir le nombre d'etudiant present : ")
        nbr = int(nombre)
        for i in range(nbr):
            etu_present = input("Saisir le nom et prenom : ") 
            etudiants_presents.append([etu_present])
   liste_presence()
   dico_seance.append([idseance,dateSeance,heureDebut,heureFin,NomModule_seance,
    NomSalle,NomProfesseur,heureTotalModule,heureRestantModule,numChapitre,
    titreChapitre,objetifs,NomSalle]) 
   list_seance.append([numeroSeance,dateSeance,NomSalle])
   menu_seance()

#Fonction pour afficher les seances
def afficherSeance():
    numSeance = "NUMERO_SEANCE"
    dateSeance = "DATE"
    salleSeance = "SALLE"
    print("Numéro séance, date séance, salle")
    print("------------------------------------------------------")
    print("--------------   AFFICHAGE DES DONNEES  --------------")
    print("------------------------------------------------------")
    print("=" * 80)
    print("{0:20s} {1:20s} {2:20s}".format(numSeance,dateSeance,salleSeance))
    print("-" * 80)
    
    for seance in list_seance:
        num,salle,date = seance
        print(f"|{num:18}",f"|{salle:19}", f"|{date:21}")
        print("-" * 80)
    menu_seance()  


#fonction pour afficher les seances avec l'id
def affiSeance():
    for i in range(len(dico_seance)):
        print(dico_seance[i], end=' ')
        print("\n\n")

#fonction pour modifier le contenu
def modifier_seance():
    affiSeance()
    bigiD = input("Saisir id module: ")
    idrecherche = bigiD.lower()
    for i in range(len(dico_seance)):
        for j in dico_seance[i]:
            if j == idrecherche:
                del dico_seance[i]
                ajoutSeance()
            else:
                 print("element introuvable")
                 menu_seance()

#fonction pour rechercher
def rechercher_seance():
    affiSeance()
    idrecherche = input("Saisir id module: ")
    for i in range(len(dico_seance)):
            if idrecherche in dico_seance[i]:
                print(dico_seance[i])
                menu_seance() 
            else:
                print("element introuvable")
                menu_seance()   

#fonction pour supprimer
def supprimer_seance():
    affiSeance()
    bigiD = input("Saisir id module: ")
    idrecherche = bigiD.lower()
    for i in range(len(dico_seance)):
        if idrecherche in dico_seance[i]:
            del dico_seance[i]
            menu_seance()            
        else:
            print("element introuvable")
            menu_seance()


#fonction pour le menu principal
def menu_seance():
    print('1-Ajouter un seance')
    print('2-Modifier les données d’un seance')
    print('3-Rechercher et afficher les informations d’un seance')
    print("4-Supprimer un seance")
    print('5-Afficher toutes les seances')
    
    while True:   
        choix = int(input('faites votre choix : '))
        if choix == 1:
            ajoutSeance()
        elif choix == 2:    
            modifier_seance()
        elif choix == 3:
            rechercher_seance()  
        elif choix == 4:
            supprimer_seance()
        elif choix == 5:
            afficherSeance()
        else:
            print("Choix non pris en compte")    

menu_seance()
