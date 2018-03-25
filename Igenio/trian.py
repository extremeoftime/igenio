from tkinter import Tk,Canvas,Text
root = Tk()
root.geometry('1000x400')



c = Canvas(width=460,height=460,bg='grey100')
c.pack()
oval = c.create_oval(30,10,130,80,fill='grey60',outline="black")
rect = c.create_rectangle(180,10,280,80,fill='grey50',outline="black")
trian = c.create_polygon(330,80,380,10,430,80,fill='grey80',outline="black")

def trian_but(event):
    b_trian = c.create_polygon(350,70,380,20,410,70,fill='grey1',outline="black")

def oval_but(event):
    c.delete(oval)
    c.create_text(70,40,fill="darkblue",font="Times 10",
                        text="Here was oval.")
                        

def rect_but(event):
    c.delete(rect)
    c.create_text(230,40,fill="darkblue",font="Times 10",
                        text="Here was rectangle.")

c.tag_bind(trian,"<Button-1>",trian_but)
c.tag_bind(oval,"<Button-1>",oval_but)
c.tag_bind(rect,"<Button-1>",rect_but)


root.mainloop()
