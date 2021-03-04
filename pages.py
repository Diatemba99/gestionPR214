"""
Module pour la gestion d'etudiant
"""
from datetime import datetime

now = datetime.now()
heureActu = now.strftime("%H:%M:%S")
heureActu_mat = now.strftime("%H%M%S")
date = now.strftime("%Y-%m-%d")

#liste pour toutes les donnees des
#liste pour toutes les donnees des etudiants
dico_etudiant = []
#liste pour les donnees a afficher
list_etudiant = []

#la fonction qui permet d'ajouter un etudiant dans la liste dico_module
def ajoutEtudiant():
    prenomEt= input("Saisir prenom: ")
    nomEt = input("Saisir nom: ")
    dateNaissEt = input(" Saisir date de Naissance ex:[00-04-19]")
    lieuNaissEt = input(" Saisir lieu de naissance: ")
    adressEt = input("Saisir adresse: ")
    telEt = input("Saisir telephone: ")
    emailEt = input("Saisir email: ")
    dateInscription = now.strftime("%Y-%m-%d")
    prenomContact = input("Saisir prenom du contact: ")
    nomContact = input("Saisir nom du contact: ")
    telContact = input("Saisir telephone du contact: ")
    emailContact = input("Saisir email du contact: ")
    #pour generer le matricule je fais une concatenation
    matEtudiant = prenomEt[:3] + heureActu_mat
    #avec append j'ajoute les donnees d'un etudiant sous forme de liste
    dico_etudiant.append([nomEt,dateNaissEt,lieuNaissEt,adressEt,telEt,emailEt,
    dateInscription,prenomContact,nomContact,telContact,emailContact,matEtudiant]) 
    list_etudiant.append([matEtudiant,prenomEt,nomEt,dateInscription])
    menu_gestionEtudiant()    

#fonction pour afficher le contenu de la liste dico_module
def afficherEtudiant():
    matEtu = "MATRICULE"
    prenomET = "PRENOM"
    nomEt = "NOM"
    dateIns= "DATE INSCRIPTION"
    print("------------------------------------------------------")
    print("--------------   AFFICHAGE DES DONNEES  --------------")
    print("------------------------------------------------------")
    print("=" * 80)
    print("{0:21s} {1:21s} {2:21s} {3:21s}".format(matEtu,prenomET,nomEt,dateIns))
    for etudiant in list_etudiant:
        matEtu,prenomET,nomEt,dateIns = etudiant
        print(f"|{matEtu:20}",f"|{prenomET:20}", f"|{nomEt:20}", f"|{dateIns:20}")
        print("-" * 80)
    menu_gestionEtudiant()  


#cette fonction affiche toute les donnees d'un etudiant
def affiEtudiant():
    for i in range(len(dico_etudiant)):
        print(dico_etudiant[i])

#fonction pour rechercher un etudiant 
def rechercheEtudiant():
    affiEtudiant()
    idrecherche = input("Saisir id module: ")
    for i in range(len(dico_etudiant)):
            if idrecherche in dico_etudiant[i]:
                print(dico_etudiant[i])
                menu_gestionEtudiant() 
            else:
                print("element introuvable")
                menu_gestionEtudiant()    

#fonction pour supprimer un etudiant
def supprimerEtudiant():
    affiEtudiant()
    bigiD = input("Saisir id module: ")
    idrecherche = bigiD.lower()
    for i in range(len(dico_etudiant)):
        if idrecherche in dico_etudiant[i]:
            del dico_etudiant[i]
            menu_gestionEtudiant()            
        else:
            print("element introuvable")
            menu_gestionEtudiant()

#fonction pour modifier les donnees d'un etudiant
def modifierEtudiant():
    affiEtudiant()
    bigiD = input("Saisir id module: ")
    idrecherche = bigiD.lower()
    for i in range(len(dico_etudiant)):
        for j in dico_etudiant[i]:
            if j in idrecherche:
                del dico_etudiant[i]
                ajoutEtudiant()
            else:
                 print("element introuvable")
    menu_gestionEtudiant()         

#menu principale de ce module
def menu_gestionEtudiant():
    print('1- AJOUTER UN ETUDIANT ')
    print('2- MODIFIER UN ETUDIANT ')
    print('3- RECHERCHER UN ETUDIANT ')
    print('4- SUPPRIMER UN ETUDIANT ')
    print('5- AFFICHER LES ETUDIANTS')
    print('6- RETOUR')
    
    while True:   
        choix = int(input('faites votre choix : '))    
        if choix == 1:
            ajoutEtudiant()
        elif choix == 5:
            afficherEtudiant()
        elif choix == 3:
            rechercheEtudiant()
        elif choix == 4:
            supprimerEtudiant()  
        elif choix == 2:
            modifierEtudiant()
        else:
            print("choix non pris en compte")    

menu_gestionEtudiant()

