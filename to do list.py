from tkinter import * 
root=Tk()
root.title("TO-DO LIST")
root.geometry("500x500")
task_list=[]

def taskaddition():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        task_list.append(task)
        listbox.insert(END,task)

def complete():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        listbox.delete(ANCHOR)
        

label1=Label(root,text="TO-DO LIST",fg="black",bg="plum",font="Calibri 20 bold")
label1.place(x=200,y=20)

frame=Frame(root,width=400,height=40,bg="black")
frame.place(x=0,y=100)

task=StringVar()
task_entry=Entry(frame,width=18,font="Calibri,30,bold",bd=0)
task_entry.place(x=25,y=7)
task_entry.focus()

button=Button(frame,text="+ Add task",font="ariel,5,bold",bg="aqua",fg="black",width=10,command=taskaddition,borderwidth=5)
button.place(x=260,y=0)

listframe=Frame(root,bd=3,width=700,height=280,bg="coral")
listframe.pack(padx=0,pady=160)

listbox=Listbox(listframe,font="calibari,60,bold ",width=40,height=16,bg="coral",fg="black")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

btn2=Button(root,text="DONE",bd=0,bg="maroon",fg="white",command=complete,font='Calibri 15 bold',borderwidth=5)
btn2.place(x=220,y=400) 
root.mainloop()

