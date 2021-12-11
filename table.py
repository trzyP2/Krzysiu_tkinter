from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import json
from pymongo import MongoClient

from operator import attrgetter

def jsonFile():
    jsonArray = []
    for x in mycol.find():
        jsonArray.append({"name" : x['name'] ,"lastName": x['lastName'] , "city": x['city'] , "password" : x['password'] })
    jsonFilePath = "data2.json"

    with open(jsonFilePath , 'w' , encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(jsonArray , indent=4))

def NameSort(k):
    return k['name']
def lNameSort(k):
    return k['lastName']
def citySort(k):
    return k['city']

def update(rows):
    for i in rows:
        trv.insert('','end',values=i)

def addUser():
    name = varName.get()
    Lname = varLName.get()
    city = varCity.get()
    password = varPass.get()

    print(name , Lname , city , password)

    myObj = {"name" : name , "lastName" : Lname , "city" : city , "password" : password}
    x = mycol.insert_one(myObj)

    for item in trv.get_children():
       trv.delete(item)

    for x in mycol.find():
      update([x['name'] + " " + x['lastName'] + " " + x['city'] + " " + x['password']])

def searchUser():
    tablica = []
    name = varNameS.get()

    
    
    for item in trv.get_children():
           trv.delete(item)
    for x in mycol.find():
          if x['name'] == name or x['lastName']==name or x['city']==name or x['password']==name:
              tablica.append(x)
    for x in tablica:
        update([x['name'] + " " + x['lastName'] + " " + x['city'] + " " + x['password']])

    


    

def sortByName():
    tablica = []
    for x in mycol.find():
        tablica.append(x)
    
    tablica.sort(key=NameSort)
    

    for item in trv.get_children():
        trv.delete(item)

    for x in tablica:
        update([x['name'] + " " + x['lastName'] + " " + x['city'] + " " + x['password']])

def sortByLName():
    tablica = []
    for x in mycol.find():
        tablica.append(x)
    
    tablica.sort(key=lNameSort)
    

    for item in trv.get_children():
        trv.delete(item)

    for x in tablica:
        update([x['name'] + " " + x['lastName'] + " " + x['city'] + " " + x['password']])
    
def sortByCity():
    tablica = []
    for x in mycol.find():
        tablica.append(x)
   
    tablica.sort(key=citySort)
    

    for item in trv.get_children():
        trv.delete(item)

    for x in tablica:
        update([x['name'] + " " + x['lastName'] + " " + x['city'] + " " + x['password']])

def showAll():
    for item in trv.get_children():
        trv.delete(item)

    for x in mycol.find():
      update([x['name'] + " " + x['lastName'] + " " + x['city'] + " " + x['password']])


root = Tk()

varName = tk.StringVar()
varLName = tk.StringVar()
varCity = tk.StringVar()
varPass = tk.StringVar()

varNameS = tk.StringVar()


myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]





wrapper1 = LabelFrame(root,text="USERS")
wrapper2 = LabelFrame(root,text="SEARCH USER")
wrapper3 = LabelFrame(root,text="ADD NEW USER")

wrapper1.pack(fill="both",expand="yes",padx=20,pady=10)
wrapper2.pack(fill="both",expand="yes",padx=20,pady=10)
wrapper3.pack(fill="both",expand="yes",padx=20,pady=10)

trv = Treeview(wrapper1,columns=(1,2,3,4),show="headings",height="6")
trv.pack()

trv.heading(1,text="colA")
trv.heading(2,text="colB")
trv.heading(3,text="colC")
trv.heading(4,text="colD")

btnNameSort = Button(wrapper1 , text="Sort by name" , command=sortByName)
btnNameSort.place(x=20 , y=150)


btnLNameSort = Button(wrapper1 , text="Sort by Lastname" , command=sortByLName)
btnLNameSort.place(x=350 , y=150)

btnCitySort = Button(wrapper1 , text="Sort by city" , command=sortByCity)
btnCitySort.place(x=680 , y=150)

lAdd =Label(wrapper3 , text="Name:")
lAdd.pack(side = LEFT , pady=10)
entryAdd = Entry(wrapper3 , textvariable=varName ,  width=20)
entryAdd.pack(side = LEFT)
llast =Label(wrapper3 , text="Last Name:")
llast.pack(side = LEFT)
entrylast = Entry(wrapper3 , textvariable=varLName , width=20)
entrylast.pack(side = LEFT)
lCity =Label(wrapper3 , text="City:")
lCity.pack(side = LEFT)
entryCity = Entry(wrapper3 , textvariable=varCity , width=20)
entryCity.pack(side = LEFT)
lpassword =Label(wrapper3 , text="Password:")
lpassword.pack(side = LEFT)
entryPassword = Entry(wrapper3 , textvariable=varPass ,  width=20)
entryPassword.pack(side = LEFT)

btnAdd = Button(wrapper3 ,  text="ADD" , command=addUser  )
btnAdd.place( x=350 , y=70)


lAddS =Label(wrapper2 , text="Find:")
lAddS.pack()
entryAddS = Entry(wrapper2 , textvariable=varNameS ,  width=30)
entryAddS.pack()


btnAddS = Button(wrapper2 ,  text="Search" , command=searchUser  )
btnAddS.pack()
btnAddShow = Button(wrapper2 ,  text="Show All" , command=showAll  )
btnAddShow.pack()

btnSave = Button(wrapper2 ,  text="Save" , command=jsonFile  )
btnSave.pack()

for x in mycol.find():
      update([x['name'] + " " + x['lastName'] + " " + x['city'] + " " + x['password']])


root.title("my app")
root.geometry("800x600")
root.mainloop()