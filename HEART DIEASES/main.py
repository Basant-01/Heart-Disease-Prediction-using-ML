from tkinter import*
from datetime import date
from tkinter.ttk import Combobox
import datetime 
import tkinter as tk
import os
from webbrowser import BackgroundBrowser


import matplotlib

matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
backgrounds='#f0ddd5'
framebg="#62a7ff"
framebg="#fefbfb"

root=Tk()
root.title("Heart Attack Predication Syatem")
root.geometry("1450x730+60+80")
root.resizable(False,False)
root.config(bg=backgrounds)
root.mainloop()




#icon1
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)


# # # Header section2
logo=PhotoImage(file="Images/header.png")
myimage=Label(image=logo,bg=backgrounds)
myimage.place(x=0,y=0)

#frame 3
Heading_entry=Frame(root,width=80,height=190,bg="df2d4b")
Heading_entry.place(x=600,y=20)

Label(Heading_entry,text="Registration No.",font="arial 13",bg="#df2d4b",fg=framebg).place(x=30,y=0)
Label(Heading_entry,text="Date",font="arial 13",bg="#df2d4b",fg=framebg).place(x=430,y=0)

Label(Heading_entry,text="Patient Name",font="arial 13",bg="#df2d4b",fg=framebg).place(x=30,y=90)
Label(Heading_entry,text="Birth Year.",font="arial 13",bg="#df2d4b",fg=framebg).place(x=430,y=90)





