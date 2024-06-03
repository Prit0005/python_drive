from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host="127.0.0.1",
        username="root",
        password="asdfghjkl",
        database="python_crud"
        )

def add_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_mobile.get()=="" or e_email.get()=="":
        msg.showinfo("Insert Status","All fields are requird")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,mobile,email) values (%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_mobile.get(),e_email.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_mobile.delete(0,"end")
        e_email.delete(0,"end")
        e_id.delete(0,"end")
        msg.showinfo("Insert Status","Data Inserted Successfully")

        
def search_data():
    if e_id.get() == "":
        msg.showinfo("search info", "id is mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from student where idstudent=%s"
        args = (e_id.get(),)
        cursor.execute(query, args)
        row = cursor.fetchall()
        if row:
            e_fname.delete(0, "end")
            e_lname.delete(0, "end")
            e_mobile.delete(0, "end")
            e_email.delete(0, "end")
            e_fname.insert(0, row[0][1])
            e_lname.insert(0, row[0][2])
            e_mobile.insert(0, row[0][3])
            e_email.insert(0, row[0][4])
        else:
            msg.showinfo("search status", "id not found")
        conn.close()

        
    
def update_data():
    if e_fname.get() == "" or e_lname.get() == "" or e_mobile.get() == "" or e_email.get() == "" or e_id.get() == "":
        msg.showinfo("update Status", "All fields are required")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "update student set fname=%s, lname=%s, mobile=%s, email=%s where idstudent=%s"
        args = (e_fname.get(), e_lname.get(), e_mobile.get(), e_email.get(), e_id.get())
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        
        e_fname.delete(0, "end")
        e_lname.delete(0, "end")
        e_mobile.delete(0, "end")
        e_email.delete(0, "end")
        e_id.delete(0, "end")
        msg.showinfo("update status", "data updated successfully")

def delete_data():
    if e_id.get() == "":
        msg.showinfo("delete Status", "id is required")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "delete from student where idstudent=%s"
        args = (e_id.get(),)
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        
        e_fname.delete(0, "end")
        e_lname.delete(0, "end")
        e_mobile.delete(0, "end")
        e_email.delete(0, "end")
        e_id.delete(0, "end")
        msg.showinfo("delete status", "data deleted successfully")

def clear_data():
    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_mobile.delete(0,"end")
    e_email.delete(0,"end")
    e_id.delete(0,"end")
    msg.showinfo("clear status","clear sucessfully")
        

root=Tk()
root.geometry("350x370")
root.title("CRUD operation")
root.resizable(width=False,height=False)


#label
l_id=Label(root,text="ID")
l_id.place(x=50,y=50)


l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)


l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)


l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=200)



l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=250)

#text box

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_mobile=Entry(root)
e_mobile.place(x=150,y=200)

e_email=Entry(root)
e_email.place(x=150,y=250)

#button

add=Button(root,text="ADD",bg="black",fg="white",font=("Arial",12),command=add_data)
add.place(x=20,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial",12),command=search_data)
search.place(x=70,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial",12),command=update_data)
update.place(x=152,y=300)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial",12),command=delete_data)
delete.place(x=232,y=300)

clear=Button(root,text="CLEAR",bg="black",fg="white",font=("Arial",12),command=clear_data)
clear.place(x=130,y=335)

root.mainloop()




