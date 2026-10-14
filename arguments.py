#! /usr/bin/env python3

"""Programme affichant les arguments qui lui sont fournis ainsi que leur indice si la variable d'environnement `DEBUG` est définie sur le shell. 
- Ce programme doit afficher un message d'erreur et renvoyer le code d'erreur 1 si aucun argument n'est fourni.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""

import sys
import os


def arguments():
    if "DEBUG" in os.environ:
        L = sys.argv
        for i in range(len(L)):
            print(f"{i}: {L[i]}")
    else:
        print(sys.argv)
    

if __name__ == "__main__":
    arguments()         
