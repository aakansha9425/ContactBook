from tkinter import *
from tkinter.messagebox import *
import sqlite3

def splash():
    s=Tk()
    s.configure(background='#f4f5f6')
    Label(s,text='Aakansha Singh',font='Arial 30 bold',width=40,bg='#f4f5f6',fg='#2b2b3a').grid(row=0,column=0,columnspan=2)
    Label(s,text='',bg='#f4f5f6').grid(row=1,column=0)
    Label(s,text='Enrollment Number',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=2,column=0)
    Label(s,text='181B002',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=2,column=1)

    Label(s,text='Batch',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=3,column=0)
    Label(s,text='BX(B1)',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=3,column=1)

    Label(s,text='Gmail Address',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=4,column=0)
    Label(s,text='aakanshasingh9425@gmail.com',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=4,column=1)

    Label(s,text='Contact No',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=5,column=0)
    Label(s,text='8962739432',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=5,column=1)

    Label(s,text='',bg='#f4f5f6').grid(row=6,column=0)
    
    def close(e=1):
        s.destroy()
    s.bind('<Motion>',close)
    s.mainloop()

splash()
    

con=sqlite3.Connection('phonebook2')
cur=con.cursor()
cur.execute("create table if not exists maindb(contactid integer primary key autoincrement,fname varchar(20),mname varchar(20),lname varchar(20),cname varchar(30),address varchar(40),city varchar(20),pincode varchar(6),websiteurl varchar(50),dob date)")
cur.execute("create table if not exists phonedb(contactid integer ,ctype varchar(10),pno integer ,primary key(contactid,pno),foreign key (contactid) REFERENCES maindb(contactid))")
cur.execute("create table if not exists emaildb(contactid integer ,etype varchar(10),email varchar(40),primary key(contactid,email),foreign key (contactid) REFERENCES maindb(contactid))")
con.commit()
#Gui
root=Tk()
root.title("PhoneBook ")
root.geometry("650x700")
img=PhotoImage(file='phonelogo.gif')
Label(root,image=img).place(x=220,y=0)
Label(root,text="First Name",font="Arial 12 ").place(x=70,y=200)
Label(root,text="Middle  Name",font="Arial 12 ").place(x=70,y=225)
Label(root,text="Last Name",font="Arial 12 ").place(x=70,y=250)
Label(root,text="Company Name",font="Arial 12 ").place(x=70,y=275)
Label(root,text="Address",font="Arial 12 ").place(x=70,y=300)
Label(root,text="city",font="Arial 12 ").place(x=70,y=325)
Label(root,text="Pincode",font="Arial 12 ").place(x=70,y=350)
Label(root,text="Website URL",font="Arial 12 ").place(x=70,y=375)
Label(root,text="Date of Birth",font="Arial 12 ").place(x=70,y=400)
e1=Entry(root,font="Arial 12 ")
e1.place(x=240,y=200)
e2=Entry(root,font="Arial 12 ")
e2.place(x=240,y=225)
e3=Entry(root,font="Arial 12 ")
e3.place(x=240,y=250)
e4=Entry(root,font="Arial 12 ")
e4.place(x=240,y=275)
e5=Entry(root,font="Arial 12 ")
e5.place(x=240,y=300)
e6=Entry(root,font="Arial 12 ")
e6.place(x=240,y=325)
e7=Entry(root,font="Arial 12 ")
e7.place(x=240,y=350)
e8=Entry(root,font="Arial 12 ")
e8.place(x=240,y=375)
e9=Entry(root,font="Arial 12 ")
e9.place(x=240,y=400)
Label(root,text='Select Phone Type :',font='Aerial 14',foreground='blue').place(x=1,y=430)
v1=IntVar()
r1=Radiobutton(root,text='Office',variable=v1,value=1).place(x=300,y=430)
r2=Radiobutton(root,text='Home',variable=v1,value=2).place(x=360,y=430)
r3=Radiobutton(root,text='Mobile',variable=v1,value=3).place(x=420,y=430)
Label(root,text="Phone Number",font="Aerial 12").place(x=70,y=460)
e10=Entry(root,font="Arial 12")
e10.place(x=240,y=460)
Label(root,text='Select Email Type :',font='Aerial 14',foreground='blue').place(x=1,y=490)
v2=IntVar()
r4=Radiobutton(root,text='Office',variable=v2,value=4).place(x=290,y=490)
r5=Radiobutton(root,text='Personal',variable=v2,value=5).place(x=360,y=490)
Label(root,text="Email Id",font="Aerial 12").place(x=70,y=520)
e11=Entry(root,font="Arial 12")
e11.place(x=240,y=520)
k=240
q=300
w=330
e=350
l=240
v=290
n=360
def addpno():
    global k,q,w,e
    
    k+=250
    q+=200
    w+=230
    e+=290
    r7=Radiobutton(root,text='Office',variable=v1,value=12).place(x=q,y=430)
    r8=Radiobutton(root,text='Home',variable=v1,value=10).place(x=w,y=430)
    r9=Radiobutton(root,text='Mobile',variable=v1,value=11).place(x=e,y=430)
    newpno=Entry(root,font="Arial 10 ").place(x=k,y=460)
def addemail():
    global l
    global v
    global n
    l+=250
    v+=200
    n+=230
    r11=Radiobutton(root,text='Office',variable=v2,value=44).place(x=v,y=490)
    r15=Radiobutton(root,text='Personal',variable=v2,value=55).place(x=n,y=490)
    newpno=Entry(root,font="Arial 10 ").place(x=l,y=520)
    
    
Button(root,text='+',font='Aerial 12 bold',command=addpno).place(x=450,y=450)
Button(root,text='+',font='Aerial 12 bold',command=addemail).place(x=450,y=520)


###############################save function################
def savedata():
    print ((e10.get()).isdigit()==False, (len(e10.get())!=10))
    if len(e1.get()) == 0:
        showinfo('warning','Your name is blank !!')
    elif(e1.get()==e2.get() and len(e1.get())!=0 and len(e2.get())!=0):
        showinfo('warning','Your first name and middle name is same !!')
    elif(e3.get()==e2.get() and len(e3.get())!=0 and len(e2.get())!=0):
        showinfo('warning','Your middle name and last name is same !!')
    elif(e3.get()==e1.get() and len(e1.get())!=0 and len(e3.get())!=0):
        showinfo('warning','Your middle name and last name is same !!')
    elif(len(e10.get())==0):
        showinfo('warning','Your phone number is blank !!')
    elif((e10.get()).isdigit()==False or (len(e10.get())!=10) ):
             showinfo('warning','Your phone number is invalid!!')
    elif (len(e11.get())!=0 and e11.get().find("@gmail.com")==-1):
        if(e11.get().find("@gmail.com")==-1):
            print (len(e11.get()))
            showinfo('warning','Your email is invalid')
            e11.delete(0,END)
        else:
            print ('hello')
            
    else:
        cur.execute("insert into maindb(fname,mname,lname,cname,address,city,pincode,websiteurl,dob) values (?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()))
        cur.execute("insert into phonedb(contactid,ctype,pno)values((select max(contactid)from maindb),?,?)",(v1.get(),e10.get()))
        cur.execute("insert into emaildb(contactid,etype,email)values((select max(contactid)from maindb),?,?)",(v2.get(),e11.get()))
        con.commit()
        print ("Data Inserted")
        showinfo('saved','Data Saved successfully')
        a=e11.get().find("@gmail.com")
        print (a)
##        r1.deselect()
##        r2.deselect()
##        r3.deselect()
##        r4.deselect()
##        r5.deselect()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)

#############################search function##################
def search():
    
    root1=Tk()
    def ser(e=0):
        
        cur.execute("select fname,mname,lname from maindb where fname like ? or mname like ? or lname like ?",(('%'+e12.get()+'%'),('%'+e12.get()+'%'),('%'+e12.get()+'%')))
        o=cur.fetchall()
        lb.delete(0,END)
        for i in range(len(o)):
            k=o[i][0]+' '+o[i][1]+' '+o[i][2]
            lb.insert(END,k)
        
    def close1():
        root1.destroy()
        
    root1.geometry("650x700")
    root1.title("Search")
    Label(root1,text="Searching PhoneBook",font="Aerial 20",bg='sky blue').place(x=150,y=0)
    Label(root1,text="Enter name : ",font="Aerial 10 ").place(x=50,y=50)
    Button(root1,text="Close",font="Aerial 10",command=close1).place(x=250,y=670)
    e12=Entry(root1,font="Aerial 10")
    e12.place(x=220,y=50)
    lb=Listbox(root1,font='Aerial 14',height=25,width=100,selectmode= SINGLE)
    lb.place(x=1,y=79)
    x=cur.execute("select contactid,fname,mname,lname from maindb order by fname").fetchall()
    for i in x:
        lb.insert(END,i[1]+' '+i[2]+' '+i[3])
    
        
    lb2=Listbox(root1,font='Aerial 14',height=25,width=100)
    def selectitem(e=1):
        
        s=(lb.get(lb.curselection()))
        v= s.split(),'spli'
        #print v
        k=str(v[0][0])
        #print k
        cid=cur.execute("select contactid from maindb where fname=?",(k,)).fetchall()
        #print x[k]
        #print 'cid ', cid[0][0]
##        idd=cid[0]
##        print idd,'idd',type(idd)
        def delete():
            cur.execute("delete from maindb where contactid=?",(cid[0][0],))
            cur.execute('delete from phonedb where contactid=?',(cid[0][0],))
            cur.execute('delete from emaildb where contactid=?',(cid[0][0],))
            con.commit()
            showinfo('delete','Data deleted successfully')
            
        Button(root1,text="Delete",font="Aerial 10",command=delete).place(x=550,y=670)
        cur.execute('select * from maindb where contactid=?',(cid[0][0],))
        M=cur.fetchall()
        print (M)
        cur.execute('select * from phonedb where contactid=?',(cid[0][0],))
        P=cur.fetchall()
        cur.execute('select * from emaildb where contactid=?',(cid[0][0],))
        E=cur.fetchall()
        #print P[0][1]
        
        lb2.place(x=1,y=79)
        lb2.insert(END,"First Name : "+M[0][1])
        lb2.insert(END,"Middle Name : "+M[0][2])
        lb2.insert(END,"Last Name : "+M[0][3])
        lb2.insert(END,"Company Name : "+M[0][4])
        lb2.insert(END,"Address : "+M[0][5])
        lb2.insert(END,"City : "+M[0][6])
        lb2.insert(END,"Pincode : "+M[0][7])
        lb2.insert(END,"Website URL : "+M[0][8])
        lb2.insert(END,"Date of Birth : "+M[0][9])
        lb2.insert(END,"Phone details.....")
        #print v1.get()
        if(v1.get()==1):
            val='office'
        elif (v1.get()==2):
            val='Home'
        else:
            val='Mobile'
        lb2.insert(END,val+' : '+P[0][2])
        lb2.insert(END,"Email  details.....")
        #print v2.get()
        if(v2.get()==4):
            val='office'
        else :
            val='Personal'
        lb2.insert(END,val+' : '+E[0][2])

        
        
        
        
##        for i in range(len(M)):
##            for j in range(1,len(M[i])):
##                lb2.insert(END,M[i][j])
##        for i in range(len(P)):
##            for j in range(1,len(P[i])):
##                if (P[i][1]==2):
##                    lb2.insert(END,"home")
##                else:
##                    lb2.insert(END,P[i][j])
##        
##        
##        for i in range(len(E)):
##            for j in range(1,len(E[i])):
##                lb2.insert(END,N[E][j])

    
    e12.bind("<KeyRelease>",ser)
    root1.bind("<<ListboxSelect>>",selectitem)
    
    root1.mainloop()
######################edit function####################
def edit():
    root2=Tk()
    def ser(e=0):
        lb.delete(0,END)
        cur.execute("select fname,mname,lname from maindb where fname like ? or mname like ? or lname like ?",(('%'+e13.get()+'%'),('%'+e13.get()+'%'),('%'+e13.get()+'%')))
        o=cur.fetchall()
        for i in range(len(o)):
            k=o[i][0]+' '+o[i][1]+' '+o[i][2]
            lb.insert(END,k)
    def close1():
        root2.destroy()
    root2.geometry("650x700")
    root2.title("Search")
    Label(root2,text="Updating PhoneBook",font="Aerial 20",bg='sky blue').place(x=150,y=0)
    Label(root2,text="Enter name for updating : ",font="Aerial 10 ").place(x=50,y=50)
    Button(root2,text="Close",font="Aerial 10",command=close1).place(x=250,y=670)
    e13=Entry(root2,font="Aerial 10")
    e13.place(x=220,y=50)
    lb=Listbox(root2,font='Aerial 14',height=25,width=100,selectmode= BROWSE)
    lb.place(x=1,y=79)
    x=cur.execute("select contactid,fname,mname,lname from maindb order by fname").fetchall()
 #   print x
 
    for i in x:
        lb.insert(END,i[1]+' '+i[2]+' '+i[3])
    def selectitem(event):
        s=(lb.get(lb.curselection()))
        v= s.split(),'spli'
        #print v
        k=str(v[0][0])
        #print k
        cid=cur.execute("select contactid from maindb where fname=?",(k,)).fetchall()
        root3=Tk()
        root3.title("Updating PHONEBOOK ")
        root3.geometry("650x700")
        print (cid[0])
        cur.execute('select * from maindb where contactid=?',(cid[0][0],))
        M=cur.fetchall()
        cur.execute('select * from phonedb where contactid=?',(cid[0][0],))
        P=cur.fetchall()
        cur.execute('select * from emaildb where contactid=?',(cid[0][0],))
        E=cur.fetchall()
        print (M[0][1],'printing the details')
        Label(root3,text="UPDATING",font="Aerial 25 bold",bg='sky blue').place(x=200,y=100)
        Label(root3,text="First Name",font="Arial 12 ").place(x=70,y=200)
        Label(root3,text="Middle  Name",font="Arial 12 ").place(x=70,y=225)
        Label(root3,text="Last Name",font="Arial 12 ").place(x=70,y=250)
        Label(root3,text="Company Name",font="Arial 12 ").place(x=70,y=275)
        Label(root3,text="Address",font="Arial 12 ").place(x=70,y=300)
        Label(root3,text="city",font="Arial 12 ").place(x=70,y=325)
        Label(root3,text="Pincode",font="Arial 12 ").place(x=70,y=350)
        Label(root3,text="Website URL",font="Arial 12 ").place(x=70,y=375)
        Label(root3,text="Date of Birth",font="Arial 12 ").place(x=70,y=400)
        Label(root3,text="Phone number",font="Aerial 12 ").place(x=70,y=425)
        Label(root3,text="Email id ",font="Aerial 12 ").place(x=70,y=450)
        
##        x=cur.execute("select fname,mname,lname,cname,address,city,pincode,websiteurl,dob from maindb").fetchall()
##        print x
        e11=Entry(root3,font="Arial 12 ")
        e11.place(x=240,y=200)
        e11.insert(END,M[0][1])
        e22=Entry(root3,font="Arial 12 ")
        e22.place(x=240,y=225)
        e22.insert(END,M[0][2])
        e33=Entry(root3,font="Arial 12 ")
        e33.place(x=240,y=250)
        e33.insert(END,M[0][3])
        e44=Entry(root3,font="Arial 12 ")
        e44.place(x=240,y=275)
        e44.insert(END,M[0][4])
        e55=Entry(root3,font="Arial 12 ")
        e55.place(x=240,y=300)
        e55.insert(END,M[0][5])
        e66=Entry(root3,font="Arial 12 ")
        e66.place(x=240,y=325)
        e66.insert(END,M[0][6])
        e77=Entry(root3,font="Arial 12 ")
        e77.place(x=240,y=350)
        e77.insert(END,M[0][7])
        e88=Entry(root3,font="Arial 12 ")
        e88.place(x=240,y=375)
        e88.insert(END,M[0][8])
        e99=Entry(root3,font="Arial 12 ")
        e99.place(x=240,y=400)
        e99.insert(END,M[0][9])
        e1010=Entry(root3,font="Arial 12 ")
        e1010.place(x=240,y=420)
        pno=cur.execute("select pno from phonedb where contactid=?",(cid[0][0],)).fetchall()
        print (pno[0][0],'pno')
        email=cur.execute("select email from emaildb where contactid=?",(cid[0][0],)).fetchall()

        #print v2.get()

        e1010.insert(END,pno[0][0])
        e1111=Entry(root3,font="Arial 12 ")
        e1111.place(x=240,y=450)
        e1111.insert(END,email[0][0])
        print ('e',e9.get())
        def close():
            root3.destroy()
        def update():
            a=e11.get()
            print (cid[0])
            cur.execute("update maindb set fname=? where contactid=?",(e11.get(),cid[0][0]))
            cur.execute("update maindb set mname=? where contactid=?",(e22.get(),cid[0][0]))
            cur.execute("update maindb set lname=? where contactid=?",(e33.get(),cid[0][0]))
            cur.execute("update maindb set cname=? where contactid=?",(e44.get(),cid[0][0]))
            cur.execute("update maindb set address=? where contactid=?",(e55.get(),cid[0][0]))
            cur.execute("update maindb set city=? where contactid=?",(e66.get(),cid[0][0]))
            cur.execute("update maindb set pincode=? where contactid=?",(e77.get(),cid[0][0]))
            cur.execute("update maindb set websiteurl=? where contactid=?",(e88.get(),cid[0][0]))
            cur.execute("update maindb set dob=? where contactid=?",(e99.get(),cid[0][0]))
            cur.execute("update phonedb set pno=? where contactid=?",(e1010.get(),cid[0][0]))
            cur.execute("update emaildb set email=? where contactid=?",(e1111.get(),cid[0][0]))
            con.commit()
            print ("Data Updated")
            showinfo('updated','Data updated successfully')
            root3.destroy()
            root2.destroy()
            
            
        Button(root3,text="Update",font="Arial 12 ",command=update).place(x=200,y=600)
        Button(root3,text="Close",font="Arial 12 ",command=close).place(x=400,y=600)
        root3.mainloop()


    lb.bind("<<ListboxSelect>>",selectitem)
    e13.bind("<KeyRelease>",ser)
    root2.mainloop()
    
    

######################close function####################
def close():
    askyesno('oops','You are closing the app')
    root.destroy()
            

Button(root,text="Save",font="Arial 12 ",command=savedata).place(x=80,y=550)
Button(root,text="Search",font="Arial 12 ",command=search).place(x=220,y=550)
Button(root,text="Close",font="Arial 12 ",command=close).place(x=340,y=550)
Button(root,text="Edit",font="Arial 12 ",command=edit).place(x=460,y=550)


root.mainloop()

