from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton 
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog
from tkinter.filedialog import askopenfilename 

def clicked(): #при нажатии кнопки "клик" во 2-й вкладке
     messagebox.showinfo('Сообщение', 'Вы выбрали  '+str(selected.get())+'  вариант')
def clicked2():
    file = filedialog.askopenfilename()
   
    text = open(file).readlines()
    text = ''.join(text)
    textline.insert(1.0, text)
   
def clicked1():# при нажатии кнопки "равно" в калькуляторе
    
    r=combo.get()#получить знак операции
    if txt1.get()!='':
      if r=='+':
          res = int(txt1.get())+int(txt2.get())#вычисление результата
      elif r=='-':
          res = int(txt1.get())-int(txt2.get())
      elif r=='*':
          res = int(txt1.get())*int(txt2.get())
      else:
          res = int(txt1.get())/int(txt2.get())
    else:
        res=0
    lbl1.configure(text=str(res))#запись результата в поле
    
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
# контейнер для вкладок
tab_control = ttk.Notebook(window) 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
#3 вкладки
tab_control.add(tab1, text='    Первая                 ') 
tab_control.add(tab2, text='    Вторая                 ')
tab_control.add(tab3, text='    Третья                 ')
#заголовки вкладок
lbl1 = Label(tab1, text='Калькулятор') 
lbl1.grid(column=0, row=0) 
lbl2 = Label(tab2, text='Вкладка 2') 
lbl2.grid(column=0, row=0)
lbl3 = Label(tab3, text='Работа с текстом', ) 
lbl3.grid(column=0, row=0) 
tab_control.pack(expand=1, fill='both')
#длля первой вкладки-калькулятора
txt1 = Entry(tab1, width=10)
#поле ввода первого числа
txt1.grid(column=0, row=1)

txt2 = Entry(tab1, width=10)
#поле ввода второго числа
txt2.grid(column=2, row=1)

combo = Combobox(tab1, width=4) #поле выбора операции
combo['values'] = ('+', '-', '*', '/') 
combo.current(0) #  вариант по умолчанию 
combo.grid(column=1, row=1)
#кнопка равно
btn1 = Button(tab1, text=" = ", command=clicked1)
btn1.grid(column=3, row=1)
#поле для аывода результата
lbl1 = Label(tab1, text="") 
lbl1.grid(column=4, row=1)

#вторая вкладка- выбор из 3-х вариантов
selected = IntVar() 
rad1 = Radiobutton(tab2,text='Первый', value=1, 
variable=selected) 
rad2 = Radiobutton(tab2,text='Второй', value=2, 
variable=selected) 
rad3 = Radiobutton(tab2,text='Третий', value=3, 
variable=selected)
#по этой кнопке  вызывается диалоговое окно
btn = Button(tab2, text="Клик", command=clicked) 
 
rad1.grid(column=0, row=1) 
rad2.grid(column=1, row=1) 
rad3.grid(column=2, row=1) 
btn.grid(column=3, row=1) 

menu = Menu(window)
#menu.add_command(label='Файл')
new_item = Menu(menu)
new_item.add_command(label='Открыть',command=clicked2)
new_item.add_separator()
new_item.add_command(label='Изменить') 
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
textline = Text(tab3, bg="white",fg='blue', wrap=WORD)
#textline.insert(1.0, text)
textline.insert(1.0, 'text')
textline.grid(column=0, row=1)

window.mainloop()
