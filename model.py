"""
regroupement de tout les modules du programme
Tout les commentaires sont de deja fait dans les modules
pour ne pas trop occuper d'espace dans la ram et eviter la repetition, dans cette partie il ya peu de commentaire
"""
from datetime import datetime
now = datetime.now()
import sys
import os

"""
# ---------------------------------------------------------------------
# -------------------         GESTION ETUDIANT       ------------------
# -------------------         GESTION ETUDIANT       ------------------
# -------------------         GESTION ETUDIANT       ------------------
# ---------------------------------------------------------------------
"""
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
    matEtudiant = prenomEt[:3] + now.strftime("%H%M%S")
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
        elif choix == 6:
            menuMain()

"""
# ---------------------------------------------------------------------
# -------------------         GESTION MODULE         ------------------
# -------------------         GESTION MODULE         ------------------
# -------------------         GESTION MODULE         ------------------
# ---------------------------------------------------------------------
"""

#creation d'une liste pour contenir les données de tout les modules
dico_module = []
#liste pour les donnees a afficher
list_module = []

#creation de la fonction ajouter qui permet d'ajouter un module dans la liste dico_module
def ajouterModule():
    nom_Module = input("Saisir nom du module : ")
    volumeHoraire_Module = input("Saisir le volume horaire du module : ")
    coefficient_Module = input("Saisir le coefficient du module : ")
    #pour avoir l'id je fais une concatenation
    idModuleBrute = "mod" + now.strftime("%H%M%S") + nom_Module
    idModule = idModuleBrute.lower()
    dico_module.append([idModule,nom_Module,volumeHoraire_Module,coefficient_Module])
    list_module.append([nom_Module,volumeHoraire_Module])
    #je fais appel a la fonction menu_module() pour la continuité de l'execution du programme
    menu_module()

#cette fonction affiche tout le contenu de la liste
def affiModule():
    for i in range(len(dico_module)):
        print(dico_module[i])

#creation de la fonction afficher qui permet d'afficher les modules de la liste dico_module
def afficherModule():
    nomMod = "NOM_MODULE"
    volHoraire = "VOLUME_HORAIRE"

    print("------------------------------------------------------")
    print("--------------   AFFICHAGE DES DONNEES  --------------")
    print("------------------------------------------------------")
    print("=" * 60)
    print("{0:21s} {1:21s}".format(nomMod,volHoraire))
    for etudiant in list_module:
        nommod,heure = etudiant
        print(f"|{nommod:20}",f"|{heure:20}")
        print("-" * 60)
    menu_module() 

#creation de la fonction modifier qui permet de modifier les modules de la liste dico_module
def modifier_module():
    affiModule()
    idsaisie = input("Saisir id module: ")
    idrecherche = idsaisie.lower()
    #ici je parcours toutes les listes qui sont dans dico_module
    for i in range(len(dico_module)):
        #je parcours le contenu d'une liste qui se trouve dans dico_module
         for j in dico_module[i]:
            if idrecherche in dico_module[i]:
                #pour modifier je supprime cette liste puis j'ajoute une autre avec ajouterModule()
                del dico_module[i]
                ajouterModule()  
            else:
                 print("element introuvable")
                 menu_module()

#creation de la fonction supprimer qui permet de supprimer un module de la liste dico_module
def supprimer_module():
    
    #je fais appel a la fonction affiModule afin que l'on puisse voir les id 
    affiModule()
    bigiD = input("Saisir id module: ")
    
    #conversion en miniscule pour faire la comparaison
    idrecherche = bigiD.lower()
    for i in range(len(dico_module)):
        if idrecherche in dico_module[i]:
            del dico_module[i]
            menu_module()            
        else:
            print("element introuvable")
            menu_module()






#creation de la fonction rechercher qui permet de rechercher un module de la liste dico_module
def rechercher_module():
    
    #je fais appel a la fonction affiModule afin que l'on puisse voir les id 
    affiModule()
    idrecherche = input("Saisir id module: ")
    
    #ici je parcours toutes les listes qui sont dans dico_module
    for i in range(len(dico_module)):
        #je parcours le contenu d'une liste qui se trouve dans dico_module
        for j in range(len(dico_module[i])):
            #je verifie si l'id saisie est dans une liste
            if dico_module[i][j] == idrecherche:
                print(dico_module[i][j])
                menu_module() 
            else:
                print('element introuvable')
                menu_module() 
    






def menu_module():
    print('1-Ajouter un module')
    print('2-Modifier les données d’un module')
    print('3-Rechercher et afficher les informations d’un module')
    print("4-Supprimer un module")
    print('5-Afficher tous les modules (Nom et volume horaire)')
    print('6-Retour')
   
    while True:   
        choix = int(input('faites votre choix : '))    
        if choix == 1:
            ajouterModule()
        elif choix == 2:    
            modifier_module()
        elif choix == 3:
            rechercher_module()  
        elif choix == 4:
            supprimer_module()
        elif choix == 5:
            afficherModule()
        elif choix == 6:
            menuMain()
        else:
            print('choix non pris en compte')    
# menu_module()


"""
# ---------------------------------------------------------------------
# -------------------         GESTION SEANCE         ------------------
# -------------------         GESTION SEANCE         ------------------
# -------------------         GESTION SEANCE         ------------------
# ---------------------------------------------------------------------
"""



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







def menu_seance():
    print('1-Ajouter un seance')
    print('2-Modifier les données d’un seance')
    print('3-Rechercher et afficher les informations d’un seance')
    print("4-Supprimer un seance")
    print('5-Afficher toutes les seances')
    print('6-RETOUR')

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
        elif choix == 6:
            menuMain() 
        else:
            print("choix non pris en compte")       





"""
# ---------------------------------------------------------------------
# -------------------          GESTION NOTE          ------------------
# -------------------          GESTION NOTE          ------------------
# -------------------          GESTION NOTE          ------------------
# ---------------------------------------------------------------------
"""


#fonction qui permet d'ajouter une note
def ajouterNotes():
    afficherEtudiant()
    afficherModule()
    menu_gestionNote()

#menu principale de ce module
def menu_gestionNote():
    print('1-Ajouter une note')
    print('2-Modifier une note')
    print('3-Afficher la note d’un étudiant pour un module donné')
    print("4-Afficher les notes d’un étudiant pour tous les module")
    print('5-Afficher les notes de tous les étudiants pour tous les modules')
    
    while True:   
        choix = int(input('faites votre choix : '))
        if choix == 1:
            ajouterNotes()
        elif choix == 2:    
                print("a faire")
                menu_gestionNote()
        elif choix == 3:
                print("a faire")
                menu_gestionNote()  
        elif choix == 4:
                print("a faire")
                menu_gestionNote()
        elif choix == 5:
                print("a faire")
                menu_gestionNote()
        elif choix == 6:
            pass
        else:
            print("choix non pris en compte")








def menuMain():
    print("=======================================================")
    print('||  1. Gestion des étudiants du groupe PR214         ||')
    print("=======================================================")

    print('||  2. Gestion des modules de formations de PR214    ||')
    print("=======================================================")

    print('||  3. Gestion des séances de cours                  ||')
    print("=======================================================")

    print('||  4. Gestion de  notes des modules du groupe PR214 ||')
    print("=======================================================")

    print('||  5. Gestion des résultats académiques             ||')
    print("=======================================================")

    print("||  6. Quitter                                       ||")
    print("=======================================================")
    
    while True:   
        choix = int(input('faites votre choix : '))     
        if choix == 1:
            menu_gestionEtudiant()
        elif choix == 2:
            menu_module()
        elif choix == 3:
            menu_seance() 
        elif choix == 4:
            menu_gestionNote()
        elif choix == 6:
            sys.exit()           
        else:
            print("choix non pris en compte")


menuMain()
