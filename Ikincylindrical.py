## CYLINDRICAL-V3


#import libraries
import numpy as np

#link lengths in mm
a1=float(input("a1 = "))
a2=float(input("a2 = "))
a3=float(input("a3 = "))


#Position Vectors in mm
x0_3=float(input("x0_3 = "))
y0_3=float(input("y0_3 = "))
z0_3=float(input("z0_3 = "))


#Inverse Kinematics Solution using Graphical Method

#Solution 1
t1 = np.arctan(y0_3/x0_3)
t1 = t1*180/np.pi

#Solution 2
d3=np.sqrt(y0_3**2+x0_3**2)-a3

#Solution 3
d2=z0_3-a1-a2

print("theta 1 = ", np.around(t1,3))
print("d2 = ", np.around(d2,3))
print("d3 = ", np.around(d3,3))

