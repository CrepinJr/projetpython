#les bibliotheques
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector


#ETUDIANT_AJOUT_MODIFIER_SUPPRIMER
def ajouter():
    nom = txtnom.get()
    
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        sql ="INSERT INTO etudiants (Nom) VALUES(%s)"
        val =(nom,)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("information", "bien ajouter")
        root.destroy()
        call(["python", "page1.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

def modifier():
    nom = txtnom.get()
    numero = txtidetud.get()
    
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        sql ="update etudiants set Nom=%s where idetudiants= %s"
        val =(nom,numero)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "modifiée")
        root.destroy()
        call(["python", "page1.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()    

def supprimer():
    numero = txtidetud.get()
    
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        sql ="delete from etudiants where idetudiants=%s"
        val =(numero,)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "supprimée")
        root.destroy()
        call(["python", "page1.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()  

#Ma fenetre
root = Tk()
root.title("PROGITUDES")
root.geometry("1120x400+0+0")
root.resizable(False, False)
root.configure(background="silver")

#Ajouter le titre
lbltitre = Label(root,borderwidth = 3,relief = GROOVE,text = "ENREGISTREMENT DES ETUDIANTS",
font = ("sans serif", 25), background = "silver",fg="#fffafa")
lbltitre.place(x=0,y=0,width= 1350, height=100)

#details des inscriptions
#idetudiants
lblidetud = Label (root, text="IDETUDIANTS", font=("Arial", 10),bg="white", fg="#000")
lblidetud.place(x=70, y=110,width=150)
txtidetud = Entry(root, bd=4, font=("Arial", 10))
txtidetud.place(x=250,y=110,width=300)

#nom
lblnom = Label (root, text="NOM", font=("Arial", 10),bg="white", fg="#000")
lblnom.place(x=70, y=140,width=150)
txtnom = Entry(root, bd=4, font=("Arial", 10))
txtnom.place(x=250,y=140,width=300)

#AJOUTER
btnajouter = Button(root, text="AJOUTER", font=("Arial", 10),bg="#CDB79E",fg="white", command=ajouter)
btnajouter.place(x=250,y=230,width=85)

#modifier
btnmodifier = Button(root, text="MODIFIER", font=("Arial", 10), bg="#8A2BE2",fg="white", command=modifier)
btnmodifier.place(x=350, y=230, width=85)

#SUPPRIMER
btnsupprimer = Button(root, text="SUPPRIMER", font=("Arial", 10), bg="#DEB887",fg="white", command=supprimer)
btnsupprimer.place(x=450, y=230, width=85)

#TABLE_ETUDIANTS
table = ttk.Treeview(root, columns = (1, 2, 3), height = 5, show = "headings")
table.place(x=560,y=110, height=260)

#Entete
table.heading(1, text = "NUM")
table.heading(2, text = "NOM")
table.heading(3, text = "PRENOM")

#dimentions pour colonnes
table.column(1,width = 50)
table.column(2,width = 200)
table.column(3,width = 300)

#Connexion_etudiants
maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
meconnect = maBase.cursor()
meconnect.execute("select * from etudiants")
for row in meconnect:
    table.insert('', END, value = row)
maBase.close()


#execution
root.mainloop()
