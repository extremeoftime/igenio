from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Калькулятор")
root.geometry("300x500")

def calc(key):
    global memory
    if key == "=":
        str = "-+0123456789.*/"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END,"Первый символ не число!")
            messagebox.showerror("Ошибка!","Вы ввели не число!")
        try:
            result =eval(calc_entry.get())
            calc_entry.insert(END,"="+str(result))
        except:
            calc_entry.insert(END,"Ошибка!")
            messagebox.showerror("Ошибка!","Проверь правильность данных")
    elif key == "C":
        calc_entry.delete(0,END)
    elif key == "+/-":
        if"=" in calc_entry.get():
            calc_entry.delete(0,END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0,"-")
            else:
                if "=" in calc_entry.get():
                    calc_entry.delete(0,END)
                calc_entry.insert(END,key)

bttn_list = [
    "7","8","9","+","-",
    "4","5","6","*","/",
    "1","2","3","+/-","=",
    "0",".","C","",""
]
r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root,text=i,command=cmd).grid(row=r,colum=c)
    c += 1
    if c>4:
        c=0
        r += 1

calc_entry = Entry(root,width=33)
calc_entry.grid(row=0,column=0,columnspan=5)

root.mainloop()
