#les bibliotheques
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector

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

def bulletin():
    nom = combonom.get()
    maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
    sql ="SELECT idetudiants from etudiants where Nom=%s"
    val =(nom,)
    meconnect.execute(sql, val)
    maBase.close()
    call(["python", "BDD.py"])


def afficher_bulletin():
    nom = combonom.get()
    #TABLE_BULLETIN
    tablbul = ttk.Treeview(root, columns = (1, 2, 3, 4,5), height = 2, show = "headings")
    tablbul.place(x=50,y=250, height=200)
    #Entete
    tablbul.heading(1, text = "MATIERES")
    tablbul.heading(2, text = "DEVOIR")
    tablbul.heading(3, text = "EXAMEN")
    tablbul.heading(4, text = "PROJET")
    tablbul.heading(5, text = "MOYENNE")
    #dimentions pour colonnes
    tablbul.column(1,width = 200)
    tablbul.column(2,width = 100)
    tablbul.column(3,width = 100)
    tablbul.column(4,width = 100)
    tablbul.column(5,width = 100)

    maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
    meconnect = maBase.cursor()
    sql ="SELECT idetudiants from etudiants where Nom=%s"
    val =(nom,)
    meconnect.execute(sql, val)
    liste_result = meconnect.fetchall()
    liste_premier_result = liste_result[0]
    result = liste_premier_result[0]#idetudiants
    maBase.close()

    maBase = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
    meconnect = maBase.cursor()
    meconnect.execute("SELECT * from evaluations")
    liste_result = meconnect.fetchall()
    plao=len(liste_result)
    maBase.close()


    Base = mysql.connector.connect(
    host="localhost",
    user="root", #en production autres comptes
    password="", #en production changer de mot de passe
    database="ecole" )#une base en particulier
    meconect = Base.cursor()
    sqll="SELECT idmatieres, idevaluation, note from composer where idetudiants=%s order by idmatieres ASC,idevaluation ASC"
    vall =(result,)
    meconect.execute(sqll, vall)
    list_result = meconect.fetchall()
    lon = len(list_result)
    resulte =""
    donne = [0, 0, 0]
    z=0    
    taille=0
    topo=0
    for i in range(lon):
        list_premier_result = list_result[i]
        if resulte!=list_premier_result[0]:
            resulte = list_premier_result[0]#idmatieres
            Base.close()
            
            maBase = mysql.connector.connect(
            host="localhost",
            user="root", #en production autres comptes
            password="", #en production changer de mot de passe
            database="ecole" )#une base en particulier
            meconneect = maBase.cursor()
            sqlll="SELECT NomMat from matieres where idmatieres=%s"
            valll =(resulte,)
            meconneect.execute(sqlll, valll)
            list_resulte = meconneect.fetchall()
            list_premiere_result = list_resulte[0]
            resultee = list_premiere_result[0]
            maBase.close()
            moy=0
            for j in range(plao):
                list_premiere_result = list_result[j]
                resulteee = list_premiere_result[1]#idevaluation
                maBase = mysql.connector.connect(
                host="localhost",
                user="root", #en production autres comptes
                password="", #en production changer de mot de passe
                database="ecole" )#une base en particulier
                meeconnect = maBase.cursor()
                slq = "SELECT note from composer where idetudiants=%s and idmatieres=%s and idevaluation=%s"
                vla = (result,resulte,resulteee)
                meeconnect.execute(slq, vla)
                answer=meeconnect.fetchall()
                
                if answer!=[]:
                    donne[j] = answer
                    Donne=donne[j]
                    donnee=Donne[0]
                    donnnee=donnee[0]
                    z+=1
                    if z==2:
                        moy=moy+donnnee*2
                    else:
                        moy=moy+donnnee
                else:
                    donne[j] = 0
                    z+=1
                maBase.close()
                mog=0
                mog=moy/4
                topo+=mog
            tablbul.insert('', END, value = (resultee,donne[0],donne[1],donne[2],mog))
            taille+=1
    #TABLE_MOYENNE
    tablnom = ttk.Treeview(root, columns = (1), height = 2, show = "headings")
    tablnom.place(x=650,y=450, height=25)
    tablnom.column(1,width = 200)
    topo=topo/taille
    print(topo)
    tablnom.insert('', END, value = (2,))
    return tablbul,tablnom



#Ma fenetre
root = Tk()
root.title("PROGITUDES")
root.geometry("1375x768+0+0")
root.resizable()
root.configure(background="silver")


#nom
lblnom = Label (root, text="Nom", font=("Arial", 10),bg="#000", fg="white")
lblnom.place(x=70, y=200,width=150)
combonom = ttk.Combobox(root,font=("Arial", 9))
combonom['values'] = cmb_nom()
combonom.place(x=225,y=200,width=300)

#AJOUt_grand_titre
lbltitre = Label(root,
    borderwidth = 1,
    relief = GROOVE,
    text = "BULLETIN DE NOTES",
    font = ("sans serif", 25), 
    background = "blue",
    fg="#fffafa")
lbltitre.place(x=0,y=0,width= 1375, height=75)

#MOYENNE_NOM
lblnom = Label (root, text="Moyenne", font=("Arial", 10),bg="#000", fg="white")
lblnom.place(x=480, y=453,width=150)

#BOUTON_CALCUL_GENERER
btnmoyenne = Button(root, text="GENERER", font=("Arial", 10), bg="#00cc00",fg="white",command= afficher_bulletin)
btnmoyenne.place(x=550, y=200, width=85)

#execution
root.mainloop()