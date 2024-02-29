## Cylindrical 


#import libraries
import numpy as np

#link lengths in mm
a1=float(input("a1 ="))
a2=float(input("a2 ="))
a3=float(input("a3 ="))

#joint variablest3=(t3/180)*np.pi5
t1=float(input("t1 ="))
d2=float(input("d2 ="))
d3=float(input("d3 ="))


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
    
