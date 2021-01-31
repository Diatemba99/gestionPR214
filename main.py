"""
ceci est le module principale du programme
"""
import sys
from view import affichage
from menu import menuMain
from model import menu_gestionEtudiant,menu_seance,menu_module

def main():
    menuMain()
    
if __name__=="__main__":
    main()
