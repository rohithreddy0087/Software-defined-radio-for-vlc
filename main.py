# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 17:00:01 2020

@author: sai narasimha
"""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time

import matplotlib
#matplotlib.use("tk")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import FigureCanvasTk,FigureManagerTk,NavigationToolbar2Tk
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk


root = Tk()

canvas1 = Canvas(root, width = 900, height = 600)
canvas1.pack()

  
def clear_charts():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()
            



fil=""
strn=" "
file = StringVar()
# for getting the flie location.
def prtfil(file):
    print(file)

def browsefunc():
    global content 
    file = filedialog.askopenfile()
    if file is not None:
        content = file.read()
        print(content)
    file = open("sample.txt", "w")
    with file:
        pass
    file.close()
    content = content.split(" ")
    
    
linecode=IntVar()
browsebutton = Button(root, text="Browse", command =lambda:browsefunc())
canvas1.create_window(200, 50, window=browsebutton)

# Displaying the route
pathlabel = ttk.Label(root)
canvas1.create_window(400, 50, window=pathlabel)

# to get input bit rate
bit_rate = ttk.Label(root,text="Bit rate")
canvas1.create_window(200, 75, window=bit_rate)
txt_date = Entry(root,width=20)
canvas1.create_window(400, 75, window=txt_date)

# for drop box Error correcting code
data=("No code", "Hamming code")
cb1=ttk.Combobox(root, values=data,state = "readonly", width=18,justify="center")
cb1.current(0)
canvas1.create_window(400, 100, window=cb1)


txt = Label(root, text = "Error correcting code:       ")
canvas1.create_window(200, 100, window=txt)


# for drop box modulation
data=("PAM", "ASK","PPM")
cb2=ttk.Combobox(root, values=data,state = "readonly",width=18,justify="center")
cb2.current(0)
canvas1.create_window(400, 125, window=cb2)

txt = Label(root, text = "Modulation:       ")
canvas1.create_window(200, 125, window=txt)


w = Spinbox( root , from_=0, to=10, justify="center", width = 3 )
canvas1.create_window(600, 125, window=w)

txt = Label(root, text = "   M :  ")
canvas1.create_window(500, 125, window=txt)

def checkcmbo():
    global bit_rate,error_corr,M_ary,pluse_shape
    bit_rate=txt_date.get()
    error_corr=cb1.get()
    M_ary=w.get()
    modu=cb2.get()
    pluse_shape=cb3.get()
    print(bit_rate,error_corr,M_ary,modu)


# for drop box modulationget
data=("Manchester", "nBmB","Polar NRZ","Polar RZ","Bipolar NRZ","Bipolar RZ")
cb3=ttk.Combobox(root, values=data,state = "readonly", width=18,justify="center")
cb3.current(0)
canvas1.create_window(400, 150, window=cb3)


txt = Label(root, text = "Pulse shaping:       ")
canvas1.create_window(200, 150, window=txt)

btn = ttk.Button(root, text="Get Value",command=checkcmbo)
btn.place(relx="0.5",rely="0.1")
canvas1.create_window(600, 180, window=btn)


button1 = Button (root, text=' Create Charts ',command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 180, window=button1)
        
f = Figure(figsize=(5,5), dpi=100)


#now we create simple function to check what user select value from checkbox
canvas = FigureCanvasTkAgg(f,root)

toolbar = NavigationToolbar2Tk(canvas,root)
toolbar.update()
canvas._tkcanvas.place()



fig = Figure(figsize=(7,5), dpi=100)
ax1 = fig.add_subplot(1,1,1)



def animate(i):
    pullData = open("sample.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    print(xar)
    
    ax1.clear()
    a.plot([1,2,3,4,5,6,7,8,9], [5,6,3,2,4,5,6,4,3])
    #ax1.plot(xar,yar)

canvas1 = FigureCanvasTkAgg(f,root)
# change the x value to 100 and 200 check the bottom
canvas1._tkcanvas.place(x=500,y=300)
ani = animation.FuncAnimation(fig, animate, interval=1000)


root.mainloop()