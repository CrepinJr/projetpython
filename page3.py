#les bibliotheques
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector





#EVALUATIONS_AJOUT_MODIFIER_SUPPRIMER
def ajouter_eva():
    typ = txttype.get()
    coef = combocoef.get()
    
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        sql ="INSERT INTO evaluations (Nomevaluation,Coefficient) VALUES(%s, %s)"
        val =(typ,coef)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "bien ajoutée")
        root.destroy()
        call(["python", "page3.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()
        


def modifier_eva():
    typ = txttype.get()
    coef = combocoef.get()
    num = txtideval.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        sql ="update evaluations set Nomevaluation=%s, Coefficient=%s where idevaluation= %s"
        val =(typ,coef,num)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "modifiée")
        root.destroy()
        call(["python", "page3.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()    

def supprimer_eva():
    num = txtideval.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ecole")
    meconnect = maBase.cursor()
    
    try:
        sql ="delete from evaluations where idevaluation=%s"
        val =(num,)
        meconnect.execute(sql, val)
        maBase.commit()
        dernierNom = meconnect.lastrowid
        messagebox.showinfo("Information", "supprimée")
        root.destroy()
        call(["python", "page3.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close() 
        
        

def nouveaute():
    
    try:
        call(["python", "page3.py"])
        
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close() 
        

#Ma fenetre
root = Tk()
root.title("PROGITUDES")
root.geometry("560x400+0+0")
root.resizable(False, False)
root.configure(background="#53868B")




#Ajouter le titre
lbltitre = Label(root,borderwidth = 3,relief = GROOVE,text = "ENREGISTREMENT DES EVALUATIONS",
font = ("sans serif", 15), background = "#53868B",fg="#FFF8DC")
lbltitre.place(x=0,y=0,width= 600, height=100)

#details des inscriptions


#AJOUT_EVALUATIONS


#idevaluation
lblideval = Label (root, text="IDEVALUATION", font=("Arial", 10),bg="#53868B", fg="black")
lblideval.place(x=70, y=120,width=150)
txtideval = Entry(root, bd=4, font=("Arial", 10))
txtideval.place(x=250,y=120,width=300)

#typt_evaluation
lbltype = Label (root, text="TYPE", font=("Arial", 10),bg="#53868B", fg="black")
lbltype.place(x=70, y=150,width=150)
txttype = Entry(root, bd=4, font=("Arial", 10))
txttype.place(x=250,y=150,width=300)

#COEFFICIENT
lblcoef = Label(root,text="COEFFICIENT", font=("Arial", 10),bg="#53868B",fg="black")  
lblcoef.place(x=70, y=180,width=150)
combocoef = ttk.Combobox(root,font=("Arial", 12))
combocoef['values'] = [1,2,3,4,5,6]
combocoef.place(x=250,y=180,width=100)

#AJOUTER_evaluations
btnajouter = Button(root, text="AJOUTER", font=("Arial", 10),bg="#53868B",fg="#FFF8DC",command=ajouter_eva)
btnajouter.place(x=70,y=240,width=85)  
#modifier_matiere
btnmodifier = Button(root, text="MODIFIER", font=("Arial", 10), bg="#53868B",fg="#FFF8DC",command=modifier_eva)
btnmodifier.place(x=160, y=240, width=85)

#SUPPRIMER_matiere
btnsupprimer = Button(root, text="SUPPRIMER", font=("Arial", 10), bg="#53868B",fg="#8B3E2F",command=supprimer_eva)
btnsupprimer.place(x=110, y=270, width=85) 




#TABLE_EVALUATIONS
tableev = ttk.Treeview(root, columns = (1, 2, 3), height = 5, show = "headings")
tableev.place(x=300,y=240, height=150)

#Entete
tableev.heading(1, text = "IDEVA")
tableev.heading(2, text = "TYPE")
tableev.heading(3, text = "COEF")

#dimentions pour colonnes
tableev.column(1,width = 50)
tableev.column(2,width = 150)
tableev.column(3,width = 50)

#Connexion_evaluations
maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
meconnect = maBase.cursor()
meconnect.execute("select * from evaluations")
for row in meconnect:
    tableev.insert('', END, value = row)
maBase.close()

#execution
root.mainloop()
