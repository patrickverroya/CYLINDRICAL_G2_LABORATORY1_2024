
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import numpy as np
import math
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3
import matplotlib
matplotlib.use("TkAgg")
from ttkbootstrap.constants import*
import ttkbootstrap as tb

#from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH    

#Create GUI with title

mygui = tb.Window(themename="cyborg")
mygui.title("Cylindrical Manipulator Calculator")
mygui.geometry("550x450")

#Reset Function
def reset():
    a1_E.delete(0,END)
    a2_E.delete(0,END)
    a3_E.delete(0,END)

    t1_E.delete(0,END)
    d2_E.delete(0,END)
    d3_E.delete(0,END)

    X1_E.delete(0,END)
    Y1_E.delete(0,END)
    Z1_E.delete(0,END)

def i_k():

    #Inverse Kinematics Using Graphical Method

    #link lengths in cm
    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())

    #Position Vector in cm
    xe = float(X1_E.get())
    ye = float(Y1_E.get())
    ze = float(Z1_E.get())


    #Inverse Kinematics Solution using Graphical Method

    #Solution 1
    if xe == 0 and ye<0:
        t2=-90
        t1=(-90*np.pi)/180

    elif xe==0 and ye>0:
        t2=90
        t1=(90*np.pi)/180

    else:
        t1 = np.arctan(ye/xe)
        t2 = t1*180/np.pi


    #Solution 2
    d3=np.sqrt(ye**2+xe**2)-a3

    #Solution 3
    d2=ze-a2-a1

    t1_E.delete(0,END)
    t1_E.insert(0,np.around(t2,3))

    d2_E.delete(0,END)
    d2_E.insert(0,np.around(d2,3))

    d3_E.delete(0,END)
    d3_E.insert(0,np.around(d3,3))

    Cylindrical = DHRobot([
            RevoluteDH(a1/100,0,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
            PrismaticDH(0,0,(270/180.0)*np.pi,a2/100,qlim=[0,(30/100)]),
            PrismaticDH(0,0,(0.0/180.0)*np.pi,a3/100,qlim=[0,(30/100)]),

        ], name="Cylindrical")
    
        #plot joints
    q1 = np.array([t1,d2/100,d3/100])

    #plot scale
    x1 = -0.5
    x2 = 0.5
    y1 = -0.5
    y2 = 0.5
    z1 = 0.0
    z2 = 0.5     

    # Plot commands
    Cylindrical.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)



    

    
def f_k():
    #Link Lengths in cm
    a1=float(a1_E.get())
    a2=float(a2_E.get())
    a3=float(a3_E.get())

    #joint variables
    t1=float(t1_E.get())
    d2=float(d2_E.get())
    d3=float(d3_E.get())



    #convert rotation angles
    t1=(t1/180)*np.pi



    #Parametric Table
    PT=[[(0.0/180.0)*np.pi+t1,(0.0/180.0)*np.pi,0,a1],  
    [(270.0/180.0)*np.pi,(270.0/180.0)*np.pi,0,a2+d2],
    [(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,a3+d3]]   

    #HTM Formulae
    i = 0
    H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
            [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
            [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
            [0,0,0,1]]
    i = 1
    H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
            [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
            [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
            [0,0,0,1]]

    i = 2
    H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
            [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
            [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
            [0,0,0,1]]



    #print("H0_1 = ")
    #H0_1 = np.array(np.round(H0_1,3))
    #print(H0_1)

    #print("H1_2 = ")
    #H1_2 = np.array(np.round(H1_2,3))
    #print(H1_2)

    #print("H2_3 = ")
    #H2_3 = np.array(np.round(H2_3,3))
    #print(H2_3)


    H0_2=np.dot(H0_1,H1_2)
    H0_3=np.dot(H0_2,H2_3)  
    print("H0_3 = ")
    H0_3=(np.array(np.around(H0_3,3)))
    print(H0_3)
        

    H0_2=np.dot(H0_1,H1_2)
    H0_3=np.dot(H0_2,H2_3)  
    H0_3=np.array(H0_3)

    X0_3 = H0_3 [0,3]
    X1_E.delete(0,END)
    X1_E.insert(0,np.around(X0_3,3))

    X0_3 = H0_3 [1,3]
    Y1_E.delete(0,END)
    Y1_E.insert(0,np.around(X0_3,3))

    X0_3 = H0_3 [2,3]
    Z1_E.delete(0,END)
    Z1_E.insert(0,np.around(X0_3,3))

    Cylindrical = DHRobot([
            RevoluteDH(a1/100,0,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
            PrismaticDH(0,0,(270/180.0)*np.pi,a2/100,qlim=[0,(30/100)]),
            PrismaticDH(0,0,(0.0/180.0)*np.pi,a3/100,qlim=[0,(30/100)]),

        ], name="Cylindrical")
    
        #plot joints
    q1 = np.array([t1,d2/100,d3/100])

    #plot scale
    x1 = -0.5
    x2 = 0.5
    y1 = -0.5
    y2 = 0.5
    z1 = 0.0
    z2 = 0.5     

    # Plot commands
    Cylindrical.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)

#Link Length and Joint Variables frame
FI = tb.LabelFrame(mygui,text="Link Frames and Joint Variables",bootstyle="success",relief=tb.SUNKEN)
FI.grid(row=0,column=0)

#Link Lengths


a1=tb.Label(FI,text=" a1 ", font=(10),bootstyle="warning")
a1.grid(row=0,column=0)

a1_E=tb.Entry(FI,width=5, font=(10),bootstyle="default")   
a1_E.grid(row=0,column=1)

cm1=tb.Label(FI,text=("cm "),font=(10),bootstyle="warning")
cm1.grid(row=0,column=2)


a2=tb.Label(FI,text=" a2 ", font=(10),bootstyle="warning")
a2.grid(row=1,column=0)


a2_E=tb.Entry(FI,width=5, font=(10),)
a2_E.grid(row=1,column=1)

cm2=tb.Label(FI,text=("cm "),font=(10),bootstyle="warning")
cm2.grid(row=1,column=2)


a3=tb.Label(FI,text=" a3 ", font=(10),bootstyle="warning")
a3.grid(row=2,column=0)

a3_E=Entry(FI,width=6, font=(10))
a3_E.grid(row=2,column=1)

cm3=tb.Label(FI,text=("cm "),font=(10),bootstyle="warning")
cm3.grid(row=2,column=2)


t1=tb.Label(FI,text=" θ1 ", font=(10),bootstyle="primary")
t1.grid(row=0,column=3)

t1_E=Entry(FI,width=5, font=(10))
t1_E.grid(row=0,column=4)

deg1=tb.Label(FI,text=(" ° "),font=(10),bootstyle="primary")
deg1.grid(row=0,column=5)

d2=tb.Label(FI,text=" d2 ", font=(10),bootstyle="primary")
d2.grid(row=1,column=3)

d2_E=Entry(FI,width=5, font=(10))
d2_E.grid(row=1,column=4)

cm5=tb.Label(FI,text=("cm "),font=(10),bootstyle="primary")
cm5.grid(row=1,column=5)

d3=tb.Label(FI,text=" d3 ", font=(10),bootstyle="primary")
d3.grid(row=2,column=3)

d3_E=Entry(FI,width=5, font=(10))
d3_E.grid(row=2,column=4)

cm6=tb.Label(FI,text=("cm "),font=(10),bootstyle="primary")
cm6.grid(row=2,column=5)

#Buttons Frame

BF = tb.LabelFrame(mygui,text="Forward and Inverse",bootstyle="success",relief=tb.SUNKEN)
BF.grid(row=1,column=0)


FK=tb.Button(BF,text="Forward ↓ ",bootstyle="success",command=f_k)
rst = tb.Button(BF,text="RESET",command=reset)
IK = tb.Button(BF,text="Inverse ↑",bootstyle="danger",command=i_k)

FK.grid(row=0, column=0,sticky="snew")
rst.grid(row=0, column=1,sticky="snew")
IK.grid(row=0, column=2,sticky="snew")

#Position Vector Frame
PV = tb.LabelFrame(mygui,text="Position Vector")
PV.grid(row=2,column=0)

X1=tb.Label(PV,text=" X1 = ")
X1_E=tb.Entry(PV,width=5)
cm9=tb.Label(PV,text=("cm "))

X1.grid(row=0,column=0)
X1_E.grid(row=0,column=1)
cm9.grid(row=0,column=2)


Y1=tb.Label(PV,text=" Y1 = ")
Y1_E=tb.Entry(PV,width=5, )
cm7=tb.Label(PV,text=("cm "))

Y1.grid(row=1,column=0)
Y1_E.grid(row=1,column=1)
cm7.grid(row=1,column=2)

Z1=tb.Label(PV,text=" Z1= ")
Z1_E=tb.Entry(PV,width=5, )
cm8=tb.Label(PV,text=("cm "))

Z1.grid(row=2,column=0)
Z1_E.grid(row=2,column=1)
cm8.grid(row=2,column=2)

img = PhotoImage(file="cylindrical.png")
img = img.subsample(1,2)
PI = Label(mygui,image=img)
PI.grid(row=1,column=3)

mygui.mainloop()








    


