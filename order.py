from tkinter import *
from tkinter import messagebox
import tkinter as tk


import time
import mysql.connector




windows = Tk()
windows.geometry("1600x1000+0+0")
windows.title("Store Managment System")
windows.configure(background="teal")


text_Input=StringVar()
operator =""
#IMAGE BUTTONS
txtdisplay = Entry(windows,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.place(x=1000,y=150)
photo1=PhotoImage(file="p6.png")
photo2=PhotoImage(file="p2.png")
photo3=PhotoImage(file="p3.png")
photo4=PhotoImage(file="p4.png")
photo5=PhotoImage(file="p5.png")
photo6=PhotoImage(file="p1.png")
photo7=PhotoImage(file="p7.png")




def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""
#GENARATION OF BILL
def total1(btext):
    
    btext.delete(0,END)
    
    global f1
    global f2
    global f3
    global f4
    global f5
    global f6
    global f7
    
    if(bt1.get()==""):
        f1=0
    else:
        f1=int(bt1.get())

    if(bt2.get()==""):
        f2=0
    else:
        f2=int(bt2.get())

    if(bt3.get()==""):
        f3=0
    else:
        f3=int(bt3.get())

    if(bt4.get()==""):
        f4=0
    else:
        f4=int(bt4.get())

    if(bt5.get()==""):
        f5=0
    else:
        f5=int(bt5.get())

    if(bt6.get()==""):
        f6=0
    else:
        f6=int(bt6.get())

    if(bt7.get()==""):
        f7=0
    else:
        f7=int(bt7.get())
        
    global tc1
    tc1=f1*25
    global tc2
    tc2=f2*12
    global tc3
    tc3=f3*445
    global tc4
    tc4=f4*37
    global tc5
    tc5=f5*25
    global tc6
    tc6=f6*30
    global tc7
    tc7=f7*50

    total= tc1+tc2+tc3+tc4+tc5+tc6+tc7
    btext.delete(0,END)
    btext.insert(0,total)
    curs = mysql.connector.connect(host='localhost',user='root',db='prachi')
    mycursor=curs.cursor()
    mycursor.execute("SELECT * FROM store")
    myresult = mycursor.fetchall()
    
    for x in range(0,len(myresult)):
        if(myresult[x][2]==text1.get()):
            repeatedno=True
    if(len(text.get())==0):
        messagebox.showinfo('Error!!','NAME is empty!')

    if(not text1.get().isnumeric()):
        messagebox.showinfo('Error!!','Please enter numbers')
        text1.delete('0',END)

    elif(len(text1.get())>10 or len(text1.get())<10):
        messagebox.showinfo('Error!!','Please check length of mobile number')
        text1.delete('0',END)

    elif(repeatedno):
        messagebox.showinfo('Error!!','Sorry! This Number is already in use')
        text1.delete('0',END)

    else:
        sql="INSERT INTO store (name,number) VALUES (%s,%s)"
        val=(text.get(),text1.get())
        mycursor.execute(sql, val)
        curs.commit()
            
        text.delete(0,END)
        text1.delete(0,END)
            
#BILL WINDOW
def create_window():
    global tc1
    global tc2
    global tc3
    global tc4
    global tc5
    global tc6
    global tc7
    repeatedno = False
    windows1= tk.Toplevel(windows)
    windows1.title("BIll")
    windows1.geometry("500x800+0+0")
    newl=Label(windows1,font=("Ariel",15,"bold","underline"),text="BILL",fg="black")
    newl.pack()
    l1=Label(windows1,text="NAME:",font=("Ariel",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2")
    l1.place(x=30,y=40)

    text0=Entry(windows1,width=15,font=("Ariel",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
    text0.place(x=150,y=40)
    l2=Label(windows1,font=("Ariel",15,"bold",),text="NUMBER:",fg="black")
    l2.place(x=30,y=100)
    text01=Entry(windows1,width=15,font=("Ariel",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2")
    text01.place(x=150,y=100)
    l3=Label(windows1,font=("Ariel",15,"bold",),text="Order no: ",fg="black")
    l3.place(x=30,y=160)
    l77=Label(windows1,font=("Ariel",15,"bold",),text="date : ",fg="black")
    l77.place(x=30,y=220)
    text77=Entry(windows1,width=15,font=("Ariel",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2")
    text77.place(x=150,y=220)
    text3=Entry(windows1,width=15,font=("Ariel",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2")
    text3.place(x=150,y=160)
    l4=Label(windows1,font=("Ariel",15,"bold",),text="Item: ",fg="black")
    l4.place(x=30,y=245)
    l5=Label(windows1,font=("Ariel",15,"bold",),text="Quantity: ",fg="black")
    l5.place(x=200,y=245)
    l7=Label(windows1,font=("Ariel",15,"bold"),text="Price: ",fg="black")
    l7.place(x=400,y=245)
    
    text0.insert(0,text.get())
    if(not text1.get().isnumeric()):
        messagebox.showinfo('Error!!','Please enter numbers')
        text1.delete(0,END)
        text.delete(0,END)
        text0.delete(0,END)

    elif(len(text1.get())>10 or len(text1.get())<10):
        messagebox.showinfo('Error!!','Please check length of mobile number')
        text1.delete(0,END)
        text.delete(0,END)
        text0.delete(0,END)
    else:
        text0.delete(0,END)
        text0.insert(0,text.get())

        text01.insert(0,text1.get())
    if(bt1.get()==""):
        la4=Label(windows1,font=("Ariel",15,"bold"),text="BISCUITS",fg="black")
        la4.place(x=30,y=280)
        la5=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        la5.place(x=240,y=280)
        la7=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        la7.place(x=400,y=280)
    else:
        la4=Label(windows1,font=("Ariel",15,"bold"),text="BISCUITS",fg="black")
        la4.place(x=30,y=280)
        la5=Label(windows1,font=("Ariel",15,"bold"),text=bt1.get(),fg="black")
        la5.place(x=240,y=280)
        la7=Label(windows1,font=("Ariel",15,"bold"),text=tc1,fg="black")
        la7.place(x=400,y=280)
    if(bt2.get()==""):
        lr4=Label(windows1,font=("Ariel",15,"bold"),text="MAGGIE",fg="black")
        lr4.place(x=30,y=320)
        lr5=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        lr5.place(x=240,y=320)
        lr7=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        lr7.place(x=400,y=320)
    else:
        lr4=Label(windows1,font=("Ariel",15,"bold"),text="MAGGIE",fg="black")
        lr4.place(x=30,y=320)
        lr5=Label(windows1,font=("Ariel",15,"bold"),text=bt2.get(),fg="black")
        lr5.place(x=240,y=320)
        lr7=Label(windows1,font=("Ariel",15,"bold"),text=tc2,fg="black")
        lr7.place(x=400,y=320)
    if(bt3.get()==""):
        lc4=Label(windows1,font=("Ariel",15,"bold"),text="ATTA",fg="black")
        lc4.place(x=30,y=360)
        lc5=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        lc5.place(x=240,y=360)
        lc7=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        lc7.place(x=400,y=360)
    else:
        lc4=Label(windows1,font=("Ariel",15,"bold"),text="ATTA",fg="black")
        lc4.place(x=30,y=360)
        lc5=Label(windows1,font=("Ariel",15,"bold"),text=bt3.get(),fg="black")
        lc5.place(x=240,y=360)
        lc7=Label(windows1,font=("Ariel",15,"bold"),text=tc3,fg="black")
        lc7.place(x=400,y=360)

    if(bt4.get()==""):
        ln4=Label(windows1,font=("Ariel",15,"bold"),text="MILK",fg="black")
        ln4.place(x=30,y=400)
        ln5=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        ln5.place(x=240,y=400)
        ln7=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        ln7.place(x=400,y=400)
    else:
        ln4=Label(windows1,font=("Ariel",15,"bold"),text="MILK",fg="black")
        ln4.place(x=30,y=400)
        ln5=Label(windows1,font=("Ariel",15,"bold"),text=bt4.get(),fg="black")
        ln5.place(x=240,y=400)
        ln7=Label(windows1,font=("Ariel",15,"bold"),text=tc4,fg="black")
        ln7.place(x=400,y=400)
    if(bt5.get()==""):
        ld4=Label(windows1,font=("Ariel",15,"bold"),text="BREAD",fg="black")
        ld4.place(x=30,y=440)
        ld5=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        ld5.place(x=240,y=440)
        ld7=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        ld7.place(x=400,y=440)
    else:
        ld4=Label(windows1,font=("Ariel",15,"bold"),text="BREAD",fg="black")
        ld4.place(x=30,y=440)
        ld5=Label(windows1,font=("Ariel",15,"bold"),text=bt5.get(),fg="black")
        ld5.place(x=240,y=440)
        ld7=Label(windows1,font=("Ariel",15,"bold"),text=tc5,fg="black")
        ld7.place(x=400,y=440)

    if(bt6.get()==""):
        lw4=Label(windows1,font=("Ariel",15,"bold"),text="SAANITIZER",fg="black")
        lw4.place(x=30,y=480)
        lw5=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        lw5.place(x=240,y=480)
        lw7=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        lw7.place(x=400,y=480)
    else:
        lw4=Label(windows1,font=("Ariel",15,"bold"),text="SAANITIZER",fg="black")
        lw4.place(x=30,y=480)
        lw5=Label(windows1,font=("Ariel",15,"bold"),text=bt6.get(),fg="black")
        lw5.place(x=240,y=480)
        lw7=Label(windows1,font=("Ariel",15,"bold"),text=tc6,fg="black")
        lw7.place(x=400,y=480)

    if(bt7.get()==""):
        ll4=Label(windows1,font=("Ariel",15,"bold"),text="LIQUID SOAPS",fg="black")
        ll4.place(x=30,y=520)
        ll5=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        ll5.place(x=240,y=520)
        ll7=Label(windows1,font=("Ariel",15,"bold"),text="----",fg="black")
        ll7.place(x=400,y=520)
    else:
        ll4=Label(windows1,font=("Ariel",15,"bold"),text="LIQUID SOAPS",fg="black")
        ll4.place(x=30,y=520)
        ll5=Label(windows1,font=("Ariel",15,"bold"),text=bt7.get(),fg="black")
        ll5.place(x=240,y=520)
        ll7=Label(windows1,font=("Ariel",15,"bold"),text=tc7,fg="black")
        ll7.place(x=400,y=520)

    bill=Label(windows1,font=("Ariel",15,"bold",),text="TOTAL AMOUNT: ",fg="black")
    bill.place(x=50,y=600)
    billt=Entry(windows1,width=15,font=("Ariel",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2")
    billt.place(x=280,y=600)
    billt.insert(0,bt8.get())
    thank=Label(windows1,font=("Ariel",15,"bold",),text="Thank you for shopping with us!!!! ",fg="black")
    thank.place(x=55,y=650)
    ca=Label(windows1,font=("Ariel",15,"bold",),text="COME AGAIN!! ",fg="black")
    ca.place(x=65,y=680)
    curs = mysql.connector.connect(host='localhost',user='root',db='prachi')
    mycursor=curs.cursor()
    mycursor.execute("SELECT * FROM store")
    myresult = mycursor.fetchall()
    
    for x in range(0,len(myresult)):
        if(myresult[x][2]==text1.get()):
            repeatedno=True
    if(len(text.get())==0):
        messagebox.showinfo('Error!!','NAME is empty!')

    if(not text1.get().isnumeric()):
        messagebox.showinfo('Error!!','Please enter numbers')
        text1.delete('0',END)

    elif(len(text1.get())>10 or len(text1.get())<10):
        messagebox.showinfo('Error!!','Please check length of mobile number')
        text1.delete('0',END)

    elif(repeatedno):
        messagebox.showinfo('Error!!','Sorry! This Number is already in use')
        text1.delete('0',END)
        

    else:
        sql="INSERT INTO store (name,number) VALUES (%s,%s)"
        val=(text.get(),text1.get())
        mycursor.execute(sql, val)
        curs.commit()
            
        text.delete(0,END)
        text1.delete(0,END)
        sql1="SELECT MAX(order_no) FROM store"
        
        mycursor.execute(sql1)
        last_id = mycursor.fetchone()
        curs.commit()
        text3.insert(0,last_id)


        sql1="SELECT MAX(date_time)FROM store"
        
        mycursor.execute(sql1)
        last_id = mycursor.fetchone()
        curs.commit()
        text77.insert(5,last_id)


        
        
        
        
        
       
    
     
def mouseClicks(ctext):
       if(ctext.get()==""):
           ctext.insert(0,1)
       else:
           count=int(ctext.get())
           ctext.delete(0,END)
           ctext.insert(0,count+1)
        
def dec(ctext):
       
       if(ctext.get()=='0'):
           messagebox.showinfo('ENTER!','ENTER VALUES')
       else:
           count=int(ctext.get())
           ctext.delete(0,END)
           ctext.insert(0,count-1)

#CALCULATOR
btn7=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="grey", command=lambda: btnclick(7) )
btn7.place(x=1000,y=200)

btn8=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="8",bg="grey", command=lambda: btnclick(8) )
btn8.place(x=1078,y=200)

btn9=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="9",bg="grey", command=lambda: btnclick(9) )
btn9.place(x=1156,y=200)

Addition=Button(windows,padx=14,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="+",bg="grey", command=lambda: btnclick("+") )
Addition.place(x=1234,y=200)

btn4=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="4",bg="grey", command=lambda: btnclick(4) )
btn4.place(x=1000,y=290)
btn5=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="5",bg="grey", command=lambda: btnclick(5) )
btn5.place(x=1078,y=290)

btn6=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text="6",bg="grey", command=lambda: btnclick(6) )
btn6.place(x=1156,y=290)

Substraction=Button(windows,padx=18,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text="-",bg="grey", command=lambda: btnclick("-") )
Substraction.place(x=1234,y=290)

btn1=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text="1",bg="grey", command=lambda: btnclick(1) )
btn1.place(x=1000,y=380)
btn2=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text="2",bg="grey", command=lambda: btnclick(2) )
btn2.place(x=1078,y=380)

btn3=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text="3",bg="grey", command=lambda: btnclick(3) )
btn3.place(x=1156,y=380)

multiply=Button(windows,padx=17,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text="*",bg="grey", command=lambda: btnclick("*") )
multiply.place(x=1234,y=380)

btn0=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text="0",bg="grey", command=lambda: btnclick(0) )
btn0.place(x=1000,y=470)

btnc=Button(windows,padx=16,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text="c",bg="grey", command=clrdisplay)
btnc.place(x=1078,y=470)

btnequal=Button(windows,padx=16,pady=16,bd=4,width = 16, fg="black", font=('Helvetica', 20 ,'bold'),text="=",bg="grey",command=eqals)
btnequal.place(x=994,y=560)

Decimal=Button(windows,padx=19,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text=".",bg="grey", command=lambda: btnclick(".") )
Decimal.place(x=1156,y=470)

Division=Button(windows,padx=18,pady=16,bd=4, fg="black", font=('Helvetica', 20 ,'bold'),text="/",bg="grey", command=lambda: btnclick("/") )
Division.place(x=1234,y=470)

l6=Label(windows,font=("Helvetica",20,"bold","underline"),text="GENERAL STORE",fg="black",bg='teal')
l6.pack()
l1=Label(windows,text="NAME:",font=("Helvetica",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2",bg='teal')
l1.place(x=60,y=80)
#MAIN SCREEN
text=Entry(windows,width=15,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
text.place(x=200,y=80)
l2=Label(windows,font=("Helvetica",15,"bold",),text="NUMBER:",fg="black",bg='teal')
l2.place(x=550,y=80)
text1=Entry(windows,width=15,font=("Helvetica",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2")
text1.place(x=700,y=80)
b1=Button(windows,text="BISCUITS",width=100,height=46,font=("Helvetica",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2",bg="white",image=photo1,command=lambda: mouseClicks(bt1))
b1.place(x=30,y=200)
bt1=Entry(windows,width=7,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
bt1.place(x=200,y=200)
bd1=Button(windows,text="-",width=4,height=1,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2",command=lambda: dec(bt1))
bd1.place(x=300,y=200)
b2=Button(windows,text="MAGGIE",width=100,height=46,font=("Helvetica",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2",bg="white",image=photo2,command=lambda: mouseClicks(bt2),)
b2.place(x=30,y=300)
bt2=Entry(windows,width=7,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
bt2.place(x=200,y=300)
bd2=Button(windows,text="-",width=4,height=1,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2",command=lambda: dec(bt2))
bd2.place(x=300,y=300)
b3=Button(windows,text="ATTA",width=100,height=46,font=("Helvetica",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2",bg="white",image=photo3,command=lambda: mouseClicks(bt3))
b3.place(x=30,y=400)
bt3=Entry(windows,width=7,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
bt3.place(x=200,y=400)
bd3=Button(windows,text="-",width=4,height=1,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2",command=lambda: dec(bt3))
bd3.place(x=300,y=400)
b4=Button(windows,text="MILK",width=100,height=46,font=("Helvetica",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2",bg="white",image=photo4,command=lambda: mouseClicks(bt4))
b4.place(x=30,y=500)
bt4=Entry(windows,width=7,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
bt4.place(x=200,y=500)
bd4=Button(windows,text="-",width=4,height=1,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2",command=lambda: dec(bt4))
bd4.place(x=300,y=500)
b5=Button(windows,width=100,height=46,text="BREAD",font=("Helvetica",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2",bg="white",command=lambda: mouseClicks(bt5),image=photo5)
b5.place(x=30,y=600)
bt5=Entry(windows,width=7,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
bt5.place(x=200,y=600)
bd5=Button(windows,text="-",width=4,height=1,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2",command=lambda: dec(bt5))
bd5.place(x=300,y=600)
b6=Button(windows,width=40,height=50,text="SAANITIZER",font=("Helvetica",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2",bg="white",command=lambda: mouseClicks(bt6),image=photo6)
b6.place(x=550,y=200)
bt6=Entry(windows,width=7,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
bt6.place(x=680,y=200)
bd6=Button(windows,text="-",width=4,height=1,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2",command=lambda: dec(bt6))
bd6.place(x=780,y=200)
b7=Button(windows,width=40,height=50,text="LIQUID SOAP",font=("Helvetica",15,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2",bg="white",command=lambda: mouseClicks(bt7),image=photo7)
b7.place(x=550,y=300)
bt7=Entry(windows,width=7,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
bt7.place(x=680,y=300)
bd7=Button(windows,text="-",width=4,height=1,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2",command=lambda: dec(bt7))
bd7.place(x=780,y=300)
global bt8
b8=Button(windows,text="Total: ",width=10,font=("Helvetica",13,"bold"),fg="black",highlightbackground="black",highlightcolor="black",highlightthickness="2",command= lambda:total1(bt8))
b8.place(x=550,y=600)

bt8=Entry(windows,width=15,font=("Helvetica",15,"bold"),highlightbackground="black",highlightcolor="black",highlightthickness="2")
bt8.place(x=700,y=600)
b9=Button(windows,text="Bill",font=("Helvetica",15,"bold"),fg="black",width=30,highlightbackground="black",highlightcolor="black",highlightthickness="2",command=create_window)
b9.place(x=550,y=550)





          

windows.mainloop()
