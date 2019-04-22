import MySQLdb
from tabulate import tabulate 
from tkinter import *
def About():
    print("This is admin menu to various operation on database ")
def changepass():
    login=Tk()
    def data():
        try:
            uname=ee1.get()
            op=ee2.get()
            cp=ee3.get()
            np=ee4.get()
            db=MySQLdb.connect("localhost","root","root","class")
            cur=db.cursor()
            sql="select * from data where user_name=%s"
            cur.execute(sql,[uname])
        except Exception:
            print("Not Found")
        else:
            res=cur.fetchall()
            for i in res:
                if(i[3]==op):
                    if(op==cp):
                        
                        sql2="update data set password=%s where user_name =%s"
                        cur.execute(sql2,[np,uname])
                        db.commit()
                        sql3="update data set confirm_pass=%s where user_name =%s"
                        cur.execute(sql3,[np,uname])
                        db.commit()
                    else:
                        print("Confirm password and old password doesnot match")
                else:
                    print("Wrong Password...")
        db.close()
    login.title("Change Password")
    login.geometry('500x400')
    label1=Label(login, text='Username', font=('bold',12))
    label1.place(x=40,y=30)
    ee1=Entry(login)
    ee1.place(x=200,y=30)
    label2=Label(login, text='Original Password', font=('bold',12))
    label2.place(x=40,y=80)
    ee2=Entry(login)
    ee2.place(x=200,y=80)
    label3=Label(login, text='Confirm Password', font=('bold',12))
    label3.place(x=40,y=130)
    ee3=Entry(login)
    ee3.place(x=200,y=130)
    label4=Label(login, text='New Password', font=('bold',12))
    label4.place(x=40,y=180)
    ee4=Entry(login)
    ee4.place(x=200,y=180)
    Button(login,width=15, text="Change Password",bg="green",fg="white",command=data,font=("bold",12)).place(x=30 , y=230)
    Button(login,width=15, text="Quit",bg="green",fg="white",command=login.destroy,font=("bold",12)).place(x=200 , y=230)
def display():
    dis=Tk()
    dis.geometry('500x400')
    def data():
        try:
            db=MySQLdb.connect("localhost","root","root","class")
            cur=db.cursor()
            sql="select * from data"
            cur.execute(sql)
        except Exception:
            print("Not Found")
        else:
            res=cur.fetchall()
            rows=[]
            for i in res:
                cols=[]
                for j in range(0,10):
                    cols.append(i[j])
                rows.append(cols)
            print(tabulate(rows,tablefmt="grid"))  
        finally:
            db.close()
    dis.title("Display Data")
    Button(dis,width=15, text="Display",bg="green",fg="white",command=data,font=("bold",12)).place(x=30 , y=230)
    Button(dis,width=15, text="Quit",bg="green",fg="white",command=dis.destroy,font=("bold",12)).place(x=200 , y=230)
def display_id():
    login=Tk()
    def data():
        idd=int(ee1.get())
        try:
            db=MySQLdb.connect("localhost","root","root","class")
            cur=db.cursor()
            sql="select * from data where id='%s'"
            cur.execute(sql,[idd])
        except Exception:
            print("Not Found")
           
        else:
            res=cur.fetchall()
            rows=[]
            for i in res:
                cols=[]
                for j in range(0,10):
                    cols.append(i[j])
                rows.append(cols)
            print(tabulate(rows,tablefmt="grid"))  
        finally:
            db.close()
    login.title("Display Data")
    login.geometry('500x400')
    label1=Label(login, text='ID', font=('bold',12))
    label1.place(x=40,y=30)
    ee1=Entry(login)
    ee1.place(x=200,y=30)
    Button(login,width=15, text="Display",bg="green",fg="white",command=data,font=("bold",12)).place(x=30 , y=230)
    Button(login,width=15, text="Quit",bg="green",fg="white",command=login.destroy,font=("bold",12)).place(x=200 , y=230)
def Update():
    login=Tk()
    def data():
        iid=int(ee1.get())
        uname=ee2.get()
        np=ee3.get()
        try:
            db=MySQLdb.connect("localhost","root","root","class")
            cur=db.cursor()
            if(uname=="user_name"):
                sql2="update data set user_name=%s where id='%s'"
                cur.execute(sql2,[np,iid])
            elif(uname=="name"):
                sql2="update data set name=%s where id='%s'"
                cur.execute(sql2,[np,iid])
            elif(uname=="email_id"):
                sql2="update data set email_id=%s where id='%s'"
                cur.execute(sql2,[np,iid])
            elif(uname=="mobile_num"):
                sql2="update data set mobile_num=%s where id='%s'"
                cur.execute(sql2,[np,iid])
            elif(uname=="gender"):
                sql2="update data set gender=%s where id='%s'"
                cur.execute(sql2,[np,iid])
            elif(uname=="state"):
                sql2="update data set state=%s where id='%s'"
                cur.execute(sql2,[np,iid])
            elif(uname=="address"):
                sql2="update data set address=%s where id='%s'"   
                cur.execute(sql2,[np,iid])
            elif(uname=="confirm_pass"):
                sql2="update data set confirm_pass=%s where id='%s'"
                cur.execute(sql2,[np,iid])    
        except Exception:
                print("Not Found")
        else:
                db.commit()
    login.title("Update")
    login.geometry('500x400')
    label1=Label(login, text='ID', font=('bold',12))
    label1.place(x=40,y=30)
    ee1=Entry(login)
    ee1.place(x=200,y=30)
    label2=Label(login, text='Field', font=('bold',12))
    label2.place(x=40,y=80)
    ee2=Entry(login)
    ee2.place(x=200,y=80)
    label3=Label(login, text='New Value', font=('bold',12))
    label3.place(x=40,y=130)
    ee3=Entry(login)
    ee3.place(x=200,y=130)
    Button(login,width=15, text="UPDATE",bg="green",fg="white",command=data,font=("bold",12)).place(x=30 , y=230)
    Button(login,width=15, text="Quit",bg="green",fg="white",command=login.destroy,font=("bold",12)).place(x=200 , y=230)
def delete():
    def data():
         iid=int(ee1.get())
         db=MySQLdb.connect("localhost","root","root","class")
         cur=db.cursor()
         try:
            sql="Delete from data where id='%s'"
            cur.execute(sql,[iid])
            db.commit()
         except:
            db.rollback()
         finally:
            db.close()
    login = Tk()
    login.title("Delete Data")
    login.geometry('500x400')
    label1=Label(login, text='ID', font=('bold',12))
    label1.place(x=40,y=30)
    ee1=Entry(login)
    ee1.place(x=200,y=30)
    Button(login,width=15, text="Delete",bg="green",fg="white",command=data,font=("bold",12)).place(x=30 , y=230)
    Button(login,width=15, text="Quit",bg="green",fg="white",command=login.destroy,font=("bold",12)).place(x=200 , y=230)
def forgetpass():
    def data():
        uname=ee1.get()
        eid=ee2.get()
        mno=int(ee3.get())
        try:
            db=MySQLdb.connect("localhost","root","root","class")
            cur=db.cursor()
            sql="select * from data where user_name=%s"
            cur.execute(sql,[uname])
        except Exception:
            print("Not Found")
        else:
            res=cur.fetchall()
            for i in res:
                if(i[5]==eid and i[6]==mno):
                        
                    sql2="select password from data where user_name=%s"
                    cur.execute(sql2,[uname])
                    res2=cur.fetchall()
                    print("Password is ",i[3])
                else:
                    print("Either email or mobile no is wrong...")
        finally:
            db.close()
    login=Tk()
    login.title("Forget password")
    login.geometry('500x400')
    label1=Label(login, text='Username', font=('bold',12))
    label1.place(x=40,y=30)
    ee1=Entry(login)
    ee1.place(x=200,y=30)
    label2=Label(login, text='Email Id', font=('bold',12))
    label2.place(x=40,y=80)
    ee2=Entry(login)
    ee2.place(x=200,y=80)
    label3=Label(login, text='Mobile No.', font=('bold',12))
    label3.place(x=40,y=130)
    ee3=Entry(login)
    ee3.place(x=200,y=130)
    Button(login,width=15, text="ForgetPass?",bg="green",fg="white",command=data,font=("bold",12)).place(x=30 , y=230)
    Button(login,width=15, text="Quit",bg="green",fg="white",command=login.destroy,font=("bold",12)).place(x=200 , y=230)
def men():
    root = Tk()
    root.title("Admin Page")
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="Menu For Admin", menu=filemenu)
    filemenu.add_command(label="Change Password", command=changepass)
    filemenu.add_command(label="Show complete Table", command=display)
    filemenu.add_command(label="Show Table By ID", command=display_id)
    filemenu.add_command(label="Update", command=Update)
    filemenu.add_command(label="Delete", command=delete)
    filemenu.add_command(label="Forget Password", command=forgetpass)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About", command=About)
    root.geometry('300x200')
    label1=Label(root, text='Admin', font=('bold',12))
    label1.place(x=60,y=80)
    label2=Label(root, text='Page', font=('bold',12))
    label2.place(x=140,y=80)

master=Tk()
master.title('SnapStore Login')
def register():
                master.destroy()
                win = Tk()
                win.title('User Login')
                win.geometry("500x600")
                Label(win,text="Name:").grid(row=0,column=1)
                Label(win,text="               ").grid(row=1,column=2)
                Label(win,text="User Name:").grid(row=2,column=1)
                Label(win,text="               ").grid(row=3,column=2)
                Label(win,text="Password:").grid(row=4,column=1)
                Label(win,text="               ").grid(row=5,column=2)
                Label(win,text="Confirm Pass:").grid(row=6,column=1)
                Label(win,text="               ").grid(row=7,column=2)
                Label(win,text="Email Id:").grid(row=8,column=1)
                Label(win,text="               ").grid(row=9,column=2)
                Label(win,text="Mobile Number:").grid(row=10,column=1)
                Label(win,text="               ").grid(row=11,column=2)
                Label(win,text="Gender:").grid(row=12,column=1)
                Label(win,text="               ").grid(row=13,column=2)
                Label(win,text="State:").grid(row=14,column=1)
                Label(win,text="               ").grid(row=15,column=2)
                Label(win,text="Address:").grid(row=16,column=1)
                Label(win,text="               ").grid(row=17,column=2)



                e1=Entry(win)
                e2=Entry(win)
                e3=Entry(win)
                e4=Entry(win)
                e5=Entry(win)
                e6=Entry(win)
                e7=Entry(win)
                e8=Entry(win)
                e9=Entry(win)

                e1.grid(row=0,column=4)
                e2.grid(row=2,column=4)
                e3.grid(row=4,column=4)
                e4.grid(row=6,column=4)
                e5.grid(row=8,column=4)
                e6.grid(row=10,column=4)
                e7.grid(row=12,column=4)
                e8.grid(row=14,column=4)
                e9.grid(row=16,column=4)
                def run():
                    name=e1.get()
                    un=e2.get()
                    pas=e3.get()
                    cpass=e4.get()
                    eid=e5.get()
                    gen=e7.get()
                    state=e8.get()
                    mno=int(e6.get())
                    add=e9.get()
        
                    try:
                            db=MySQLdb.connect("localhost","root","root","class")
                            cur=db.cursor()
                            sql="insert into data(name,user_name,password,confirm_pass,email_id,mobile_num,gender,state,address) values(%s,%s,%s,%s,%s,'%s',%s,%s,%s)"
                            cur.execute(sql,[name, un, pas, cpass, eid, mno, gen, state, add])
                            db.commit()
                    except Exception:
                            print("Not Found")
                    finally:
                            db.close()
                Button(win, text="Register", command=run).grid(row=20,column=1)
                Button(win, text="Quit", command= win.destroy).grid(row=20,column=4)
def admin():
    username=ee1.get()
    password=ee2.get()
    try:
        db=MySQLdb.connect("localhost","root","root","class")
        spl="select * from data"
        cur=db.cursor()
        cur.execute(spl)
    except Exception:
        print("Not Found")
    else:
        result=cur.fetchall()
        for i in result:
            if(username==i[2] and password==i[3]):
                men()    
            else:
                print("Username or Password is incorrect")
                break
    finally:
        db.close()
        master.destroy()
logo=PhotoImage(file="Capture.png")
w1=Label(master,image=logo,padx=100).grid(row=0,columnspan=3)
Label(master,text="Username").grid(row=1)
Label(master,text="Password").grid(row=2)
ee1=Entry(master)
ee2=Entry(master)
ee1.grid(row=1,column=1)
ee2.grid(row=2,column=1)
Button(master,text="SIGN IN",command=admin).grid(row=3,column=1)
Button(master,text="Register",command=register).grid(row=4,column=0)
Button(master,text="Forget Password?",command=forgetpass).grid(row=4,column=2)
master.mainloop()
