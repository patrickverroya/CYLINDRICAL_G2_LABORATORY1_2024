
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
