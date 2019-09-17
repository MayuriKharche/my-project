from tkinter import *
from tkinter import messagebox
import mysql.connector
            
root=Tk()                               
root.title("Insert Records")                                #To give title to the root window
root.geometry('1200x1000')

def valid_digit(inp):                                       #Function to ensure that the 'inp' is a digit
    if inp.isdigit():
        return True
    elif inp=='':
        return True
    else:
        return False
    return  
    
reg1 = root.register(valid_digit)

def submit():
    ac = e1.get()
    nm = e2.get()
    if ac=='':
        messagebox.showwarning("Please enter your Account Number")
    elif nm=='':
        messagebox.showwarning("Alert", "Please enter your Name")
    else:
        cursor.execute("INSERT INTO dimpal(num, name, pass) VALUES(%s, %s, %s)", (ac, nm, e3.get()))
        conn.commit()
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    return

def delete():
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    return
    

l1 = Label(root, text="Account No:-")
l1.pack(padx =30)
l2 = Label(root, text="Name:-")
l2.pack()
l3 = Label(root, text="Amount:-")
l3.pack()
l4 = Label(root, text="Record Details")
l4.pack()

e1 = Entry(root)
e1.pack()
e1.config(validate = "key", validatecommand = (reg1,'%P'))
e2 = Entry(root)
e2.pack()
e2.config(validate = "key")
e3 = Entry(root)
e3.pack()
e3.config(validate = "key", validatecommand = (reg1,'%P'))

b1=Button(root, text= "INSERT", fg= "blue", command=submit)
b1.pack()
b2=Button(root,text="CLEAR", fg="blue", command=delete)
b2.pack()

l1.place(x=500, y=300)
l2.place(x=500, y=330)
l3.place(x=500, y=360)
l4.place(x=550, y=280)

e1.place(x=600, y=300)
e2.place(x=600, y=330)
e3.place(x=600, y=360)

b1.place(x=540, y=390)
b2.place(x=650, y=390)

if e1.get().isdigit()=="True":
    print("dhf")

conn = mysql.connector.connect(host="localhost",username="root",passwd="root",database="python_DB")
cursor = conn.cursor()


root.mainloop()
