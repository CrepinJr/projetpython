#les bibliotheques
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector

        



#MATIERES_AJOUT_MODIFIER_SUPPRIMER
def ajouter_ma():
    nom = txtnomm.get()
    coefficient = combocoefmat.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        sql ="INSERT INTO matieres (NomMat,CoefMat) VALUES(%s,%s)"
        val =(nom,coefficient)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "bien ajoutée")
        root.destroy()
        call(["python", "page2.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

def modifier_ma():
    nom = txtnomm.get()
    numero = txtidmat.get()
    coefficient = combocoefmat.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        sql ="update matieres set NomMat=%s,CoefMat=%s where idmatieres= %s"
        val =(nom,coefficient,numero)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "modifiée")
        root.destroy()
        call(["python", "page2.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()    

def supprimer_ma():
    numero = txtidmat.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        sql ="delete from matieres where idmatieres=%s"
        val =(numero,)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "supprimée")
        root.destroy()
        call(["python", "page2.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close() 



        

#Ma fenetre
root = Tk()
root.title("PROGITUDES")
root.geometry("570x420+0+0")
root.resizable(False, False)
root.configure(background="#474747")




#Ajouter le titre
lbltitre = Label(root,borderwidth = 3,relief = GROOVE,text = "ENREGISTREMENT DES MATIERES",
font = ("sans serif", 18), background = "#8B7500",fg="#fffafa")
lbltitre.place(x=0,y=0,width= 600, height=60)

#details des inscriptions

#id_matiere
lblidmat = Label (root, text="IDMATIERES", font=("Arial", 10),bg="#474747",fg="#fffafa")
lblidmat.place(x=70, y=100,width=150)
txtidmat = Entry(root, bd=4, font=("Arial", 10))
txtidmat.place(x=250,y=100,width=300)

#nom_matiere
lblnomm = Label (root, text="NOM MATIERE", font=("Arial", 10),bg="#474747",fg="#fffafa")
lblnomm.place(x=70, y=130,width=150)
txtnomm = Entry(root, bd=4, font=("Arial", 10))
txtnomm.place(x=250,y=130,width=300)

#Coefficient matieres
lblcoefmat = Label(root,text="COEFFICIENT MATIERE", font=("Arial", 10),bg="#474747",fg="#fffafa")  
lblcoefmat.place(x=70, y=160,width=150)
combocoefmat = ttk.Combobox(root,font=("Arial", 12))
combocoefmat['values'] = [1,2,3,4,5,6]
combocoefmat.place(x=250,y=160,width=300)

#AJOUTER_matiere

btnajouter = Button(root, text="AJOUTER", font=("Arial", 10),bg="#CDB79E",fg="white",command=ajouter_ma)
btnajouter.place(x=250,y=210,width=85)
#modifier_matiere
btnmodifier = Button(root, text="MODIFIER", font=("Arial", 10), bg="#8A2BE2",fg="white",command=modifier_ma)
btnmodifier.place(x=350, y=210, width=85)

#SUPPRIMER_matiere
btnsupprimer = Button(root, text="SUPPRIMER", font=("Arial", 10), bg="#DEB887",fg="white",command=supprimer_ma)
btnsupprimer.place(x=460, y=210, width=85)  


#TABLE_MATIERES
tablem = ttk.Treeview(root, columns = (1, 2), height = 2, show = "headings")
tablem.place(x=250,y=250, height=160)

#Entete
tablem.heading(1, text = "ID")
tablem.heading(2, text = "NOM")


#dimentions pour colonnes
tablem.column(1,width = 100)
tablem.column(2,width = 200)
 
   

#Connexion_matieres
maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
meconnect = maBase.cursor()
meconnect.execute("select * from matieres")
for row in meconnect:
    tablem.insert('', END, value = row)
maBase.close()

#execution
root.mainloop()
