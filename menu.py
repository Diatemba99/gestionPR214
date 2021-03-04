"""
module pour l'affiche du programme
"""
import sys
import colorama
import time
import random
import os
from view import *
from model import menu_gestionEtudiant,menu_seance,menu_module

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
    valeur = input("Faites votre choix : ")
    choice = int(valeur)
    if choice == 1:
        menu_gestionEtudiant()
    elif choice == 2:
        menu_module()
    elif choice == 3:
        menu_seance() 
    elif choice == 4:
        print("A faire")
        menuMain()  
    elif choice == 5:
        print("A faire")
        menuMain()               
    elif choice == 6:
        pass
    else:
        print("Ce choix n'existe pas ")
        menuMain()

if __name__=="__main__":
    affichage()
    menuMain()
