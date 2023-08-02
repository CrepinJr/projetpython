#les bibliotheques
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector

#Fonction pour remplir les valeurs du combo box matieres
def cmb_matiere():
    maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
    meconnect = maBase.cursor()
    meconnect.execute("select NomMat from matieres")
    data = []
    for row in meconnect.fetchall():
        data.append(row[0])
    return data

#Fonction pour remplir les valeurs du combo box composition
def cmb_compo():
    maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
    meconnect = maBase.cursor()
    meconnect.execute("select Nomevaluation from evaluations")
    data = []
    for row in meconnect.fetchall():
        data.append(row[0])
    return data

#Fonction pour remplir les valeurs du combo box nom
def cmb_nom():
    maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
    meconnect = maBase.cursor()
    meconnect.execute("select Nom from etudiants")
    data = []
    for row in meconnect.fetchall():
        data.append(row[0])
    return data
    
    
def etuajouter():
    nom = combonom.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor(buffered=True)
    
    try:
        pretusql = "SELECT idetudiants FROM etudiants WHERE Nom = %s"
        pretuval =(nom,)
        meconnect.execute(pretusql, pretuval)
        liste_result = meconnect.fetchall()
        liste_premier_result = liste_result[0]
        result = liste_premier_result[0]
        return result
        maBase.close()
    except Exception as e:
       print(e)
       #retour
       maBase.close()
       

def matajouter():
    mat = combomat.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor(buffered=True)
    
    try:
       prematsql = "SELECT idmatieres FROM matieres WHERE NomMat = %s"
       prematval = (mat,)
       meconnect.execute(prematsql, prematval)
       liste_result = meconnect.fetchall()
       liste_premier_result = liste_result[0]
       result = liste_premier_result[0]
       return result
       maBase.close()
    except Exception as e:
        print(e)
        maBase.close()
       
       

def compajouter():
    comp = combocomp.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor(buffered=True)
    
    try:
       preevalsql = "SELECT idevaluation FROM evaluations WHERE Nomevaluation = %s"
       preevalval = (comp,)
       meconnect.execute(preevalsql, preevalval)
       liste_result = meconnect.fetchall()
       liste_premier_result = liste_result[0]
       result = liste_premier_result[0]
       return result
       maBase.close()
    except Exception as e:
       print(e)
       #retour
       maBase.close()



def ajouter():
    notes = txtnotes.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor(buffered=True)
    
    try:
        resultprim = etuajouter()
        resultdeux = matajouter()
        resulttrois = compajouter()
        sql ="INSERT INTO composer (idetudiants,idmatieres,idevaluation,note) VALUES(%s,%s,%s,%s)"
        val =(resultprim,resultdeux,resulttrois,notes)
        meconnect.execute(sql, val)
        dernierNom = meconnect.lastrowid
        maBase.commit()
        maBase.close()
        messagebox.showinfo("Information", "Information bien ajouté")
        root.destroy()
        call(["python", "page4.py"])
        
    except Exception as e:
        messagebox.showinfo("Information", e)
        #retour
        maBase.rollback()
        maBase.close()



def modifier():
    notes = txtnotes.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        resultprim = etuajouter()
        resultdeux = matajouter()
        resulttrois = compajouter()
        sql ="update composer set note=%s where idetudiants= %s and idmatieres= %s and idevaluation= %s"
        val =(notes,resultprim,resultdeux,resulttrois)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "Information modifiée")
        root.destroy()
        call(["python", "page4.py"])
        
    except Exception as e:
        messagebox.showinfo("Erreur", e)
        #retour
        maBase.rollback()
        maBase.close()



def supprimer():
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        resultprim = etuajouter()
        resultdeux = matajouter()
        resulttrois = compajouter()
        sql ="delete from composer where idetudiants= %s and idmatieres= %s and idevaluation= %s"
        val =(resultprim,resultdeux,resulttrois)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "Note supprimé")
        root.destroy()
        call(["python", "page4.py"])
        
    except Exception as e:
        messagebox.showinfo("Erreur", e)
        #retour
        maBase.rollback()
        maBase.close()



def mat(boss):
    Base = mysql.connector.connect(
        host="localhost",
        user="root", #en production autres comptes
        password="", #en production changer de mot de passe
        database="ecole" )#une base en particulier
    meconnect = Base.cursor(buffered=True)
    presql = ("select Nom from etudiants where idetudiants=%s")
    val = (boss,)
    meconnect.execute(presql,val)
    liste_result = meconnect.fetchall()
    liste_premier_result = liste_result[0]
    result = liste_premier_result[0]
    return result
    Base.close()

def matmat(boss):
    Base = mysql.connector.connect(
        host="localhost",
        user="root", #en production autres comptes
        password="", #en production changer de mot de passe
        database="ecole" )#une base en particulier
    meconnect = Base.cursor(buffered=True)
    presql = ("select NomMat from matieres where idmatieres=%s")
    val = (boss,)
    meconnect.execute(presql,val)
    liste_result = meconnect.fetchall()
    liste_premier_result = liste_result[0]
    result = liste_premier_result[0]
    return result
    Base.close()
    
    
def mateva(boss):
    Base = mysql.connector.connect(
        host="localhost",
        user="root", #en production autres comptes
        password="", #en production changer de mot de passe
        database="ecole" )#une base en particulier
    meconnect = Base.cursor(buffered=True)
    presql = ("select Nomevaluation from evaluations where idevaluation=%s")
    val = (boss,)
    meconnect.execute(presql,val)
    liste_result = meconnect.fetchall()
    liste_premier_result = liste_result[0]
    result = liste_premier_result[0]
    return result
    Base.close()    



#Ma fenetre
root = Tk()
root.title("PROGITUDES")
root.geometry("1375x768+0+0")
root.resizable()
root.configure(background="white")


#Ajouter le titre
lbltitre = Label(root,
    borderwidth = 1,
    relief = GROOVE,
    text = "ENREGISTREMENT DES NOTES",
    font = ("sans serif", 25), 
    background = "#FFFFFF",
    fg="#9932CC")
lbltitre.place(x=0,y=0,width= 1375, height=75)

#Nom étudiant
lblnom = Label (root, text="Nom", font=("Arial", 10),bg="#ffffff", fg="#000000")
lblnom.place(x=70, y=160,width=150)
combonom = ttk.Combobox(root,font=("Arial", 9))
combonom['values'] = cmb_nom()
combonom.place(x=70,y=190,width=300)


#Matiere
lblmat = Label(root,text="Matiere", font=("Arial", 10),bg="#ffffff",fg="#000000")  
lblmat.place(x=70, y=240,width=150)
combomat = ttk.Combobox(root,font=("Arial", 9))
combomat['values'] = cmb_matiere()
combomat.place(x=70,y=270,width=300)

#Composition
lblcomp = Label(root,text="Composition", font=("Arial", 10),bg="#ffffff",fg="#000000")  
lblcomp.place(x=70, y=330,width=150)
combocomp = ttk.Combobox(root,font=("Arial", 9))
combocomp['values'] = cmb_compo()
combocomp.place(x=70,y=360,width=300)

#Notes
lblnotes = Label (root, text="Notes", font=("Arial", 10),bg="#FFFFFF", fg="#000000")
lblnotes.place(x=70, y=410,width=150)
txtnotes = Entry(root, bd=3, font=("Arial", 10))
txtnotes.place(x=70,y=440,width=300)

#AJOUTER
btnajouter = Button(root, text="AJOUTER", font=("Arial", 10),bg="#FFFFFF",fg="#7FFF00", command=ajouter)
btnajouter.place(x=90,y=550,width=85)

#MODIFIER
btnmodifier = Button(root, text="MODIFIER", font=("Arial", 10),bg="#FFFFFF",fg="#9932CC", command=modifier)
btnmodifier.place(x=180,y=550,width=85)

#SUPPRIMER
btnsupprimer = Button(root, text="SUPPRIMER", font=("Arial", 10),bg="#FFFFFF",fg="#A52A2A", command=supprimer)
btnsupprimer.place(x=280,y=550,width=85)

#RESET
# btnreset = Button(root, text="RESET", font=("Arial", 10),bg="#00cc00",fg="white")
# btnreset.place(x=450,y=350,width=85)

#TABLE_ETUDIANTS
table = ttk.Treeview(root, columns = (1, 2, 3, 4, 5), height = 2, show = "headings")
table.place(x=560,y=150, height=500)

#Entete
table.heading(1, text = "NOM")
table.heading(2, text = "MATIERE")
table.heading(3, text = "EVALUATION")
table.heading(4, text = "NOTES")

#dimentions pour colonnes
table.column(1,width = 150)
table.column(2,width = 150)
table.column(3,width = 150)
table.column(4,width = 50)

maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
meconnect = maBase.cursor()
meconnect.execute("select * from composer")
plo = meconnect.fetchall()
longueur = len(plo)
for i in range(longueur):
    pla = plo[i]
    long = len(pla)
    for j in range(long):
        if(j==0):
            pli=pla[j]
            toto=mat(pli)
        if(j==1):
            pli=pla[j]
            tete=matmat(pli)
        if(j==2):
            pli=pla[j]
            tyty=mateva(pli)
        if(j==3):
            pli=pla[j]
            note=pli
    table.insert('', END, value = (toto,tete,tyty,note))
maBase.close()

#execution
root.mainloop()