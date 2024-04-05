
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



    


