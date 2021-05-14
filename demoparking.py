import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hashamsql",
    database="rdbms"
    )
print(mydb)

mycursor=mydb.cursor()

#mysql-connector-python
#pillow

#mycursor.execute("create table parking3(first_name VARCHAR(20),last_name VARCHAR(20),mobile int,email VARCHAR(30),cnic_number VARCHAR(15),number_plate varchar(20),atm_number VARCHAR(15),amount_of_charge VARCHAR(5),vehicle VARCHAR(20),date_of_incident VARCHAR(15),location varchar(20)")
#mycursor.execute("create table parking17 (slip_number int NOT NULL AUTO_INCREMENT,first_name VARCHAR(20),last_name VARCHAR(20),mobile int(15),email VARCHAR(30),cnic_number VARCHAR(25),number_plate VARCHAR(15),atm_number varchar(20),amount_of_charge int(5),vehicle VARCHAR(20),date_of_incident varchar(20),location varchar(20),primary key(slip_number))")
#email,cnic_number,number_plate,atm_number,amount_of_charge,vehicle,date_of_incident,location

from tkinter import *
from PIL import ImageTk,Image
from time import *
root=Tk()
current_time=localtime()
c_day=current_time.tm_mday
d_month=current_time.tm_mon
e_year=current_time.tm_year
f_hour=current_time.tm_hour
g_min=current_time.tm_min
h_sec=current_time.tm_sec
#X AXIS,Y AXIS
root.minsize(1000,800)
root.maxsize(1000,800)
root.title("PARKING FORM")
my_image=PhotoImage(file="parking.png")
my_label=Label(image=my_image,width="1000",height="800")
my_label.place(x=0,y=0)

a=Label(root,text="WELCOME TO UBIT PARKING",bg="grey",width="500")
a.pack()


#z=Label(root,text="SLIP NUMBER")
#z.place(x=10,y=120)
b=Label(root,text="FIRST NAME")
b.place(x=10,y=120)
c=Label(root,text="LAST NAME")
c.place(x=10,y=160)
d=Label(root,text="MOBILE NUMBER")
d.place(x=10,y=200)
e=Label(root,text="EMAIL")
e.place(x=10,y=320)
f=Label(root,text="CNIC NUMBER")
f.place(x=10,y=360)

g=Label(root,text="NUMBER PLATE")
g.place(x=10,y=400)
l=Label(root,text="ACCOUNT NUMBER")
l.place(x=10,y=520)
m=Label(root,text="AMOUNT OF CHARGE")
#m.insert(0,"500")
m.place(x=10,y=560)
h=Label(root,text="DATE OF INCIDENT")
h.place(x=10,y=440)
i=Label(root,text="ADDRESS")
i.place(x=10,y=480)


b_entry=Entry(root)
b_entry.place(x=150,y=120)
c_entry=Entry(root)
c_entry.place(x=150,y=160)
d_entry=Entry(root)
d_entry.place(x=150,y=200)
e_entry=Entry(root)
e_entry.place(x=150,y=320)
f_entry=Entry(root)
f_entry.place(x=150,y=360)
g_entry=Entry(root)
g_entry.place(x=150,y=400)
h_entry=Entry(root)
h_entry.place(x=150,y=440)
i_entry=Entry(root)
i_entry.place(x=150,y=480)
l_entry=Entry(root)
l_entry.place(x=150,y=520)
m_entry=Entry(root)
#m_entry.insert(0,"500")
m_entry.place(x=150,y=560)

k=StringVar(root)
k.set("           SELECT THE VEHICLE")
j=OptionMenu(root,k,"CAR","BIKE","RIKSHAW","BUS","CYCLE")
j.pack()
j.place(x=80,y=240)

#x=mycursor.execute("select slip_number from parking12 ORDER BY slip_number DESC limit 1")
#sum=0
#while True:
#    sum+=1
#    break



#zz="SELECT slip_number FROM parking15 ORDER BY slip_number DESC LIMIT 1"
#zzz=mydb.cursor()
#zzz.execute(zz)
#row=zzz.fetchone()
        
#,d_entry.get(),e_entry.get(),f_entry.get(),g_entry.get(),l_entry.get(),m_entry.get(),k.get(),h_entry.get(),i_entry.get())
#,mobile,email,cnic_number,number_plate,atm_number,amount_of_charge,vehicle,date_of_incident,location) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
def save_info():
    try:
        sql = "INSERT INTO parking17(first_name, last_name,mobile,email,cnic_number,number_plate,atm_number,amount_of_charge,vehicle,date_of_incident,location) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (b_entry.get(),c_entry.get(),d_entry.get(),e_entry.get(),f_entry.get(),g_entry.get(),l_entry.get(),m_entry.get(),k.get(),h_entry.get(),i_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        p=Label(root,text=e)
        p.place(x=80,y=600)
        p.pack()
    aaa="SELECT slip_number from parking17 ORDER BY slip_number DESC LIMIT 1"
    row=mydb.cursor()
    row.execute(aaa)
    row1=row.fetchone()
    file=open("driver slip1","w")
    file.write(f"DATE : {c_day}/{d_month}/{e_year}\n")
    file.write(f"TIME : {f_hour}:{g_min}:{h_sec}\n")
    file.write(f"SLIP NUMBER : {row1}\nFIRST NAME : {b_entry.get()}\nSECOND NAME : {c_entry.get()}\nMOBILE : {d_entry.get()}\nEMAIL : {e_entry.get()}\nCNIC NUMBER : {f_entry.get()}\nNUMBER PLATE : {g_entry.get()}\nATM NUMBER : {l_entry.get()}\nAMOUNT OF CHARGE : {m_entry.get()}\nVEHICLE : {k.get()}\nDATE OF INCIDENT : {h_entry.get()}\nLOCATION : {i_entry.get()}")
    file.close()
    print(f"DATE : {c_day}/{d_month}/{e_year}\n")
    print(f"TIME : {f_hour}:{g_min}:{h_sec}\n")
    print(f"SLIP NUMBER : {row1}\nFIRST NAME : {b_entry.get()}\nSECOND NAME : {c_entry.get()}\nMOBILE : {d_entry.get()}\nEMAIL : {e_entry.get()}\nCNIC NUMBER : {f_entry.get()}\nNUMBER PLATE : {g_entry.get()}\nATM NUMBER : {l_entry.get()}\nAMOUNT OF CHARGE : {m_entry.get()}\nVEHICLE : {k.get()}\nDATE OF INCIDENT : {h_entry.get()}\nLOCATION : {i_entry.get()}")



    
q=Button(root,text="SUMBIT",width="25",command=save_info)
q.pack()
q.place(x=370,y=600)

#button_exit=Button(root,text="EXIT",command=root.quit)
#button_exit.pack()

root.mainloop()



