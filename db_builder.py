#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
c.execute("CREATE TABLE peopl('age' TEXT,'name' TEXT,'id' TEXT);")
with open ('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for ele in reader:
        c.execute("INSERT INTO peopl("+ ele['age'] +", "+ ele['name'] +"," + ele['id'] + ");")
#command = "CREATE TABLE  peeps(age )"          #build SQL stmt, save as string
#c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


