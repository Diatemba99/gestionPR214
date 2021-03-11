"""
module pour la gestion des modules
"""

from datetime import datetime
import time

now = datetime.now()
#recuperation en conversion de la date et l'heure en chaine de caracteres
date = now.strftime("%Y-%m-%d")
heureActu_mat = now.strftime("%H%M%S")

#creation d'une liste pour contenir les données de tout les modules
dico_module = []

#liste pour les donnees a afficher
#liste
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
    print("{0:20s} {1:20s}".format(nomMod,volHoraire))
    for etudiant in list_module:
        nommod,heure = etudiant
        print(f"|{nommod:20}",f"|{heure:19}")
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
    
#menu principale de ce module
def menu_module():
    print('1-Ajouter un module')
    print('2-Modifier les données d’un module')
    print('3-Rechercher et afficher les informations d’un module')
    print("4-Supprimer un module")
    print('5-Afficher tous les modules')
    
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
            pass
        else:
            print("choix non pris en compte")
menu_module()
