# CYLINDRICAL MANIPULATOR

## Members:

#### PL : Naz, Jhann-rey L.
#### PE : Sunga, Jairus C.
#### PS : de Gracia, Terrance Mae C.
#### PQ : Blasco, Treaty Sherrizah L.
#### PR : Verroya, Patrick James C.

# **ABSTRACT**

A **CYLINDRICAL MANIPULATOR** is a type of robot arm that is designed to function in a cylindrical workspace. This type of manipulator consists of three links (one prismatics and two revolute) arranged in a cylindrical configuration (RPP). The circular work envelope of the robots is made possible via a rotating shaft and an extensible arm that slides and travels vertically. The cylindrical manipulator has several industrial uses, including pick-and-place operations, painting, and welding. Its workspace, however, is constrained to a cylindrical cylinder and it would not be appropriate for applications requiring great precision or substantial payloads.

# **INTRODUCTION**
![b-removebg-preview](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/1a0a72df-385f-462d-b5cb-e774d6771d76)  ![433589030_1095598608339301_3556433435437126138_n](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/a4f78d99-3eeb-4dca-bd88-b59a93c7b104)



The rapid development of technology has caused a surge in the need for automation within several sectors. The integration of robots in various industries has brought about a significant transformation, and the fundamental element of this evolution is the mechanical manipulator, also known as robotic arm. Mechanical manipulator has a significant ability on enhancing productivity, efficiency, and safety in a workplace. The demand for adaptable manipulators remains a key driver of innovation that keeps the robotics field to push on boundaries. A manipulator with distinctive design and functional attributes is a cylindrical manipulator, known for its vertical post and telescoping arm that provide a compact footprint and exceptional vertical reach. In this project, the members will focus on the world of cylindrical manipulator.

**CYLINDRICAL MANIPULATORS** are unique options for simple
applications that require a compact automation
solution. Their slender frame and compact design allow
for minimal workspace intrusion. Cylindrical robots are
found in a wide variety of industries. The common
application of it is packaging, material handling,
palletization, simple welding and dispensing.
There are three axes or degrees of freedom in the
cylindrical robot. They have a straightforward
mechanical design with a single rotational axis for
rotation at the base and two linear axes for height
control and arm extension with an end-effector. The
number of motors within a robot is correlated with each
axis of a cylindrical manipulator. This offers the
adaptability required to use robots to automate
numerous industrial operations. The cylindrical
manipulator is made up of rigid links joined together by
joints. The manipulator has one end that is attached to
a base and the other that is free to be employed for
various robotic tasks.

As we move forward, we will be exploring the full potential of its form and functions. Dissecting the cylindrical manipulator's characteristics such as the number of its joints, DOF, D-H Frames and more that will emphasize the unique advantages it offers.

# **DEGREES OF FREEDOM**
The number of independent variables used to
represent the various positions or motions of a
mechanical system in space is referred to as degrees
of freedom (DOF) in mechanics. The number of degrees
of freedom is equal to the total number of independent
displacements or motion characteristics.

**This will be the basis of the type of mechanical manipulator based on number of DOF of cylindrical manipulator.**
- **Under-actuated Manipulator**
     
  Either a Spatial Manipulator w/ less than 6-DOF or a
  Planar Manipulator w/ less than 3-DOF.
- **Ideal Manipulator**
  
   Either a Spatial Manipulator w/ exactly 6-DOF or a
   Planar Manipulator w/ exactly 3-DOF.
- **Redundant Manipulator**
  
    Either a Spatial Manipulator w/ more than 6-DOF or a
    Planar Manipulator w/ more than 3-DOF

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/bda9c1cf-8b6d-461e-9802-b345a1a24d04)
![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/6424960a-aae6-4119-a182-dc7e488c6155)

           SOLUTION OF DEGREES OF FREEDON FOR CYLINDRICAL MANIPULATOR

  ![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/9a61137a-4107-4720-8e92-8ab032a708b1)

  **SUPPLEMENTARY VIDEO DISCUSSION [CLICK HERE: https://www.youtube.com/watch?v=6bcpWGbW0z0]** 
  
  ![2](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157670284/05c9d249-3bb3-44c3-9e35-d948f7997cfd)

  # **KINEMATIC DIAGRAM AND D-H FRAME**

  **Denavit-Hartenberg Notation**

  Denavit-Hartenberg notation is widely used in the transformation of coordinate systems of linkages and robot mechanisms. This will be used to determine the position and orientation of cylindrical manipulator.

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/42d40388-938d-44d2-a32a-6065c987ff21)
____________________________________![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/635250ed-cc00-41a1-b648-f5d1581b0ccb) ______________________________________________


          ASSIGNING OF FRAMES TO A CYLINDRICAL MANIPULATOR

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/ca81b6a3-a2d8-4604-b92e-d7af45032c86)
![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/b394038e-b9e0-4216-80b0-51c6a1029a82)

  **SUPPLEMENRARY VIDEO DISCUSSION [CLICK HERE: https://www.youtube.com/watch?v=B_SrmvaQ9Lw]** 
  
![3](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157670284/74297091-42c1-4e4d-9353-382a8f93952a)



# D-H PARAMETRIC TABLE

In the documentation for cylindrical robots, it could quickly locate homogeneous transformation matrices using the dh parameter table.

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/e4628dcc-c56a-4388-80a6-86b23116c1c1)
![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/aa53777f-86ff-47f4-a303-eeccd84c6fae)

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/fa7b1c60-9a69-40cc-900e-d6bef6edf038)

  **SUPPLEMENRARY VIDEO DISCUSSION [CLICK HERE: https://www.youtube.com/watch?v=g8zGarD6TcI]** 
  
  ![4](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157670284/153d0f93-d6a4-4f2b-b60a-a5f479368672)


# **HOMOGENEOUS TRANSFORMATION MATRIX**

Homogeneous transformation matrices are a tool
used to describe the position and orientation of a
rigid body relative to a fixed reference frame.
They essentially combine rotation and translation
information into a single, convenient mathematical
structure.

Homogeneous transformation matrices combine both the rotation matrix and displacement vector intoto a single matrix. Homogeneous transformation matrix combines both the rotation matrix and the displacement vector into a single matrix. We can multiply two homogeneous matrices together just like we can with rotation matrices. We can combine rotation matrices and displacement vectors into a single matrix. It is the important concept of forward kinematics.

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/64123790-890e-46a8-a78a-267bdf14aa0d)
![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/93d77d1e-7677-4cf9-8889-6a72b3a0c731)

_________________________________________________________________________________________________________________________________________________

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/fbe5a5c8-d1d1-469b-8882-6e618818fa1c)

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/b09fca0f-058b-4044-bc01-b8f779cf7453)

  **SUPPLEMENTARY VIDEO DISCUSSION [CLICK HERE: https://www.youtube.com/watch?v=4LfBKG08URo]** 
  
  ![5](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157670284/bf8a7a91-6842-4534-9781-06eb2cba34a0)


# **INVERSE KINEMATICS** 
Inverse kinematics is the mathematical process
of calculating the variable joint parameters
needed to place the end of a kinematic chain, such
as a robot manipulator or animation character's
skeleton, in a given position and orientation
relative to the start of the chain.

In inverse kinematics, the given input is the position vector while the output is the joint variable. The method obtain the output depends on the design of difficulty of the mechanical manipulator.
![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/e5d01b4b-c9af-49a5-b01c-8f89d320d3b4)

In forward kinematics, the given inputs are the joints variables using the homogeneous transformation matrix, by that, we will obtain position vector.
![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/84001ee9-2638-43c4-90d1-741f6d2da9dd)

INVERSE KINEMATICS OF CYLINDRICAL MANIPULATOR

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/c156e7b5-aec3-4dc8-9440-d63a98e271de)

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157602175/9d37453a-8401-47f3-b10d-652f9559e821)

  **SUPPLEMENTRY VIDEO DISCUSSION [CLICK HERE: https://www.youtube.com/watch?v=qs-n-z8mm-g]** 
  
  ![6](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157670284/4f2f8068-84a4-4fc3-b504-4bf68d1fa871)


# **FORWARD AND INVERSE KINEMATICS (GUI CALCULATOR)**

  **Main Interface**

  
The picture below shows the main interface of the Cylindrical Manipulator Inverse and Forward Calculator. Take note that ttkbootstrap is added as library for the gui interface. This calculator can also take 0 cm as for X and Y which is not possible from the previous activities.

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157588949/136185ad-422c-487f-be86-870500981fbd)




**Link Lengths Interface**

This part of the GUI calculator is the input of the necessary link length that is required to calculate the forward kinematics and inverse kinematics.




![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157588949/75c11a1e-f59c-429c-835f-f39a7b82d19a)




  **Joint Variables**

This is the part where the joint variables are shown. This is also the part where you input the joint variable to calculate the inverse kinematics. It also where the joint variable is shows when computing for the Inverse Kinematics

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157588949/b5a13133-557f-463a-9423-52e31318903a)




**Function Buttons**
This is where the magic happens. This is responsible for the commands/controls of the calculator. The Forward Button is for calculating the Forward Kinematics, and the Inverse Button is for calculating the Inverese Kinematics. The reset button is for resetting everything in the input/output box.


![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157588949/3eb36521-3046-405b-8cac-bd0a1084e34e)




**Position Vector**
This part is where the Position Vector is shown when computing for the Forward Kinematics. This is also where you input the Position Vector when computing for the Inverse Kinematics

![image](https://github.com/patrickverroya/Cylindrical_Lab1/assets/157588949/cd59101f-963f-4be5-9e8e-714d36ec2c20)


# **REFERENCES**
- Chakraborty, E. (2024, January 20). What is a
cylindrical robot? 9 Answers You should
know - LAMBDAGEEKS. Lambda Geeks.
https://lambdageeks.com/cylindrical-robots/

- Wikipedia contributors. (2024, March 10).
Transformation matrix. Wikipedia.
https://en.wikipedia.org/wiki/Transformation
_matrix

- Lunia, A. (n.d.). Inverse kinematics. Pressbooks.
https://opentextbooks.clemson.edu/wangrob
otics/chapter/inverse-kinematics/








