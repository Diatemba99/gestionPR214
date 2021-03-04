import colorama
import time
import random
import os

#setting randow color 
couleur = list(vars(colorama.Fore).values())

def pr214():
    print('11111111111111         111111111111111111           11111111111111111111      1111111      11111111                  ')
    print('1111111111111111       11111111111111111111         11111111111111111111      1111111      11111111                  ')
    print('11111111111111111      111111111111111111111        11111111111111111111      1111111      11111111                  ')
    print('111111     111111      111111          11111                      111111      1111111      11111111                  ')
    print('111111     111111      111111          11111                      111111      1111111      11111111                  ')
    print('111111     111111      111111          11111                      111111      1111111      11111111         111111   ')
    print('1111111111111111       11111111111111111111         11111111111111111111      1111111      11111111         111111   ')
    print('111111111111111        1111111111111111111          11111111111111111111      1111111      11111111111111111111111   ')
    print('1111111111111          11111111111111111            11111111111111111111      1111111      11111111111111111111111   ')
    print('111111                 111111   1111111             111111                    1111111      11111111111111111111111   ')
    print('111111                 111111     111111            111111                    1111111                      1111111   ')
    print('111111                 111111       111111          111111                    1111111                      1111111   ')
    print('111111                 111111         111111        11111111111111111111      1111111                      1111111   ')
    print('111111                 111111           111111      11111111111111111111      1111111                      1111111   ')

#function permettant d'afficher le contenu de cette 
def affichage():
    for i in range(300):   
        time.sleep(0.001)
        #j'affiche et je change la couleur du contenu
        print(random.choice(couleur),"11"*65)
    #le systeme
    #le systeme patiente 3 secondes avant d'effacer l'écran avec cls
    time.sleep(3)    
    os.system('cls')

    for i in range(20):
        #j'affiche et je change la couleur du contenu de la fonction pr214
        print(random.choice(couleur),pr214())   
        time.sleep(0.1)
        os.system('cls')

affichage()
