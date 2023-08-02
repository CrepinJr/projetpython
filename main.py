# les bibliotheques
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox

# import mysql.connector


# Cette page permet de naviguer entre les différentes pages de l'application


# Ma fenetre
root = Tk()
root.title("PROGITUDES")
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.configure(background="#CDC8B1")


def add_etudiant():
    try:
        call(["python", "page1.py"])

    except Exception as e:
        print(e)
        # retour


#       maBase.rollback()
#      maBase.close()
def add_matieres():
    try:
        call(["python", "page2.py"])

    except Exception as e:
        print(e)
        # retour


#        maBase.rollback()
#       maBase.close()
def add_evaluations():
    try:
        call(["python", "page3.py"])

    except Exception as e:
        print(e)
        # retour


#       maBase.rollback()
#      maBase.close()
def add_notes():
    try:
        call(["python", "page4.py"])

    except Exception as e:
        print(e)
        # retour


#     maBase.rollback()
#    maBase.close()
def add_bul():
    try:
        call(["python", "page5.py"])

    except Exception as e:
        print(e)
        # retour
    #  maBase.rollback()
    #   maBase.close()


# creation d'une barre de menu
menu_bar = Menu(root)

# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ajout des etudiants", menu=file_menu)
file_menu.add_command(label="ajouter", command=add_etudiant)

# creer un deuxieme menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ajout des matieres", menu=file_menu)
file_menu.add_command(label="ajouter", command=add_matieres)

# creer un troisieme menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ajout des evaluations", menu=file_menu)
file_menu.add_command(label="ajouter", command=add_evaluations)

# creer un quatrieme menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ajout des notes", menu=file_menu)
file_menu.add_command(label="ajouter", command=add_notes)

# creer un cinquieme menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Bulletin", menu=file_menu)

file_menu.add_command(label="ajouter", command=add_bul)

# configurer notre fenetre pour ajouter cette menu bar
root.config(menu=menu_bar)

# execution
root.mainloop()
