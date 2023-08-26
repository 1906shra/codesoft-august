from tkinter import*
def click(eve):
    global scvalue
    text=eve.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=float(scvalue.get())
        else:
            try:
                value=eval(e1.get())
            except Exception as e:
                print(e)
                value="Error"
                
        scvalue.set(value)
        e1.update()
    elif text =="C":
        scvalue.set("")
        e1.update()
    
    else:
        scvalue.set(scvalue.get()+text)
        e1.update()
        
qwe=Tk()
qwe.title("Calculator")
qwe.geometry("500x700")

###

scvalue=StringVar()
scvalue.set("")
e1=Entry(qwe,textvar=scvalue,font="lucida 30 bold")
e1.pack(fill=X,pady=10,padx=10)
f1=Frame(qwe,bg="grey")
b1=Button(f1,text="9",font="lucida 25",width=5,borderwidth=5)
b1.pack(side=LEFT,padx=20,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="8",font="lucida 25",width=5,borderwidth=5)
b2.pack(side=LEFT,padx=20,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="7",font="lucida 25",width=5,borderwidth=5)
b3.pack(side=LEFT,padx=20,pady=10)
b3.bind("<Button-1>",click)


f1.pack()
##


f2=Frame(qwe,bg="grey")
b1=Button(f2,text="6",font="lucida 25",width=5,borderwidth=5)
b1.pack(side=LEFT,padx=20,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f2,text="5",font="lucida 25",width=5,borderwidth=5)
b2.pack(side=LEFT,padx=20,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f2,text="4",font="lucida 25",width=5,borderwidth=5)
b3.pack(side=LEFT,padx=20,pady=10)
b3.bind("<Button-1>",click)

f2.pack()
###


f3=Frame(qwe,bg="grey")
b1=Button(f3,text="3",font="lucida 25",width=5,borderwidth=5)
b1.pack(side=LEFT,padx=20,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f3,text="2",font="lucida 25",width=5,borderwidth=5)
b2.pack(side=LEFT,padx=20,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f3,text="1",font="lucida 25",width=5,borderwidth=5)
b3.pack(side=LEFT,padx=20,pady=10)
b3.bind("<Button-1>",click)
f3.pack()
##

f4=Frame(qwe,bg="grey")
b1=Button(f4,text="-",font="lucida 25",width=5,borderwidth=5)
b1.pack(side=LEFT,padx=20,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f4,text="0",font="lucida 25",width=5,borderwidth=5)
b2.pack(side=LEFT,padx=20,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f4,text="*",font="lucida 25",width=5,borderwidth=5)
b3.pack(side=LEFT,padx=20,pady=10)
b3.bind("<Button-1>",click)
f4.pack()


###
f5=Frame(qwe,bg="grey")
b1=Button(f5,text="/",font="lucida 25",width=5,borderwidth=5)
b1.pack(side=LEFT,padx=20,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f5,text="%",font="lucida 25",width=5,borderwidth=5)
b2.pack(side=LEFT,padx=20,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f5,text="+",font="lucida 25",width=5,borderwidth=5)
b3.pack(side=LEFT,padx=20,pady=10)
b3.bind("<Button-1>",click)
f5.pack()
##


f6=Frame(qwe,bg="grey")
b1=Button(f6,text="C",font="lucida 25",width=5,borderwidth=5)
b1.pack(side=LEFT,padx=20,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f6,text="=",font="lucida 25",width=5,borderwidth=5)
b2.pack(side=LEFT,padx=20,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f6,text=".",font="lucida 25",width=5,borderwidth=5)
b3.pack(side=LEFT,padx=20,pady=10)
b3.bind("<Button-1>",click)
f6.pack()

qwe.mainloop()
