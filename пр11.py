from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton 
from tkinter.ttk import Combobox
from tkinter import messagebox
import json
import requests
from pprint import pprint

def clicked1():            
    stro=txt1.get()         
    if stro!='':
        user_data = requests.get(stro).json() 
        pprint(user_data)
        us_data={'company':None,'created_at': None,'email': None,'id':0,'name':None,'url':None}
        for i in user_data:  
         if i=="company" or i=="id" or i=='created_at' or i=='email' or i=='name' or i=='url':
            us_data[i]=user_data[i]
        with open("data_file.json", "w") as write_file: 
           json.dump(us_data, write_file)  

#https://api.github.com/users/kubernetes - имя сайта для ввода в текстовое поле
    
window = Tk()
window.title(" приложение ")
window.geometry('400x250')

txt1 = Entry(window, width=50)
txt1.grid(column=0, row=1)

btn1 = Button(window, text=" Ok ", command=clicked1)
btn1.grid(column=1, row=1)

window.mainloop()
