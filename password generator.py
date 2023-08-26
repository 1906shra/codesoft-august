from tkinter import*
from random import randint

qwe=Tk()
qwe.title("Random Paassword Generator")
qwe.geometry("600x400")


def click():
    password_entry.delete(0,END)
    password_length=int(entry.get())
    my_password=''
    for x in range(password_length):
        my_password += chr(randint(33,126))

    password_entry.insert(0,my_password)

def change():
    password_entry.delete(0,END)
        
    
labelframe=LabelFrame(qwe, text="Random Password Generator",font="Calibri,35,bold")
labelframe.pack(pady=20)

entry=Entry(labelframe,font="Calibri,20")
entry.pack(padx=20,pady=20)

password_entry=Entry(qwe,text="",font="Calibri,24,italic")
password_entry.pack(pady=20)

frame=Frame(qwe)
frame.pack(pady=20)

btn1=Button(frame,text="Generate",command=click)
btn1.grid(row=0,column=0,padx=10)

btn2=Button(frame,text="Reset",command=change)
btn2.grid(row=6,column=0,padx=10)


qwe.mainloop()
