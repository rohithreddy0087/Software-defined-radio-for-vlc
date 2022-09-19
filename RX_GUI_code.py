# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:52:43 2020

@author: sai narasimha
"""


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import FigureCanvasTk,FigureManagerTk,NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk,filedialog
from tkinter.scrolledtext import ScrolledText

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.fftpack import fft,fftshift
import numpy as np

from serial import Serial

global bit_rate,error_corr,M_ary,pluse_shape,f,file
global xList,yList,samples_data
global time_x_limit,time_y_limit,freq_x_limit,freq_y_limit
global situation,flag_data_type

import py_fi as py_fi

from importlib import reload

flag_data_type='none'
pause = False

LARGE_FONT= ("Verdana", 12)
plt.style.use('fivethirtyeight')

f = Figure(figsize=(6,6.8), dpi=100)
a = f.add_subplot(211)
a1 = f.add_subplot(212)
f.subplots_adjust(left=0.1,right=0.9,hspace=0.5,top=0.95)
a.set_xlabel("Time",fontsize = 10)
a.set_ylabel("Amplitude",fontsize = 10)
a.set_title("Time response",fontsize = 13)
a1.set_xlabel("Fequency",fontsize = 10)
a1.set_ylabel("Magnitude",fontsize = 10)
a1.set_title("Frequency response",fontsize = 13)
a.set(xlim=(0, 50), ylim=(0,50))
a1.set(xlim=(0, 50), ylim=(0,50))
    

xList = []
yList = []

t = 0
fr = 0
def animate(self):
    
    global t
    global fr
    
    tmax=time_x
    fmax=freq_x
    a1.clear()
    a.step(xList[t:t+time_x],yList[t:t+time_x],'b-',linewidth='1')
    fylist = fft(yList[t:t+time_x],time_x)
    fxlist = np.arange(time_x)
    
    
    #a1.plot(fxlist,fylist,'r-',linewidth='1')
    
    NFFT=1024 #NFFT-point DFT
    X=fftshift(fft(yList[t:t+time_x],NFFT)) #compute DFT using FFT
     
    #fig3, ax = plt.subplots(nrows=1, ncols=1) #create figure handle
    fVals=np.arange(start = 0,stop = NFFT) #DFT Sample points
    a1.plot(fVals,np.abs(X),'r-',linewidth='1')
    #print(max(np.abs(X)))
    #fig3.show()
    #plt.figure()
    #plt.plot(fVals,np.abs(X),'r-',linewidth='1')
    a1.set_xlim(0,NFFT)
    a1.set_ylim(0,30)
    f.canvas.draw()
    t=t+time_x
    fr=fr+freq_x
    #plt.figure()
    #plt.plot(fxlist,fylist,'r-',linewidth='1')
    if t >= tmax+1.00:
        a.set_xlim(t-tmax+1.0,t+1.0)
    #if fr >= fmax-1.00:
    #    a1.set_xlim(fr-fmax+1.0,fr+1.0)
    return a,a1
    

def stop():
    window.destroy()   

def reset():
    global t,fr,ani
    text = tk.Text(TAB1,width=30)
    text.insert(tk.INSERT, "Please load the File.")
    text.place(x=0,y=200)
    cb1.current(0)
    cb2.current(0)
    cb3.current(0)
    time_x_limit.delete(0, tk.END)
    time_x_limit.insert(0,"30")
    time_y_limit.delete(0, tk.END)
    time_y_limit.insert(0,"2")
    
    freq_x_limit.delete(0, tk.END)
    freq_x_limit.insert(0,"50")
    freq_y_limit.delete(0, tk.END)
    freq_y_limit.insert(0, "60")
    
    txt_date.delete(0, tk.END)
    txt_date.insert(0, "10")
    
    w.delete(0,"end")
    w.insert(0,2)
    ani.event_source.stop()
    a.cla()
    a1.cla()
    
    xList.clear()
    yList.clear()
    f.canvas.draw()
    a.set_xlabel("Time",fontsize = 10)
    a.set_ylabel("Amplitude",fontsize = 10)
    a.set_title("Time response",fontsize = 13)
    a1.set_xlabel("Feqrency",fontsize = 10)
    a1.set_ylabel("Magnitude",fontsize = 10)
    a1.set_title("Frequency response",fontsize = 13)
    a.set(xlim=(0, 50), ylim=(0,50))
    a1.set(xlim=(0, 50), ylim=(0,50))
    t=0
    fr=0
    check_loop=0
    f.canvas.draw()
    flag_data_type='none'
    


def pause():
    global ani
    ani.event_source.stop()
    btn_reset = ttk.Button(box2, text='Resume', command=resume)
    btn_reset.place(x=120,y=150)
    
def resume():
    global ani
    ani.event_source.start()
    btn_reset = ttk.Button(box2, text='Pause', command=pause)
    btn_reset.place(x=120,y=150)        


def save_time():
    """Generate a pop-up window for special messages."""
    extent = a.get_window_extent().transformed(f.dpi_scale_trans.inverted())
    f.savefig('Time_Response.png', bbox_inches=extent)
    root = tk.Tk()
    root.title("Save Time Response")
    w = 400    # popup window width
    h = 200    # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = "Saved Time Response:Time_Response.png"
    w = tk.Label(root, text=m, width=120, height=10)
    w.pack()      

def save_time1():
    extent = a.get_window_extent().transformed(f.dpi_scale_trans.inverted())
    f.savefig('Time_Response.png', bbox_inches=extent)
    text = tk.Text(window)
    text.insert(tk.INSERT, "Saved Time Response:Time_Response.png")
    text.place(x=0,y=650)

def save_freq():
    """Generate a pop-up window for special messages."""
    root = tk.Tk()
    extent = a1.get_window_extent().transformed(f.dpi_scale_trans.inverted())
    f.savefig('Frequency_Response.png', bbox_inches=extent)
    root.title("Save Frequency Response")
    w = 400    # popup window width
    h = 200    # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = "Saved Frequency Response:Frequency_Response.png"
    w = tk.Label(root, text=m, width=120, height=10)
    w.pack() 
    
def save_freq1():
    extent = a1.get_window_extent().transformed(f.dpi_scale_trans.inverted())
    f.savefig('Frequency_Response.png', bbox_inches=extent)
    text = tk.Text(window)
    text.insert(tk.INSERT, "Saved Frequency Response:Frequency_Response.png")
    text.place(x=0,y=650)
    
def run():
    global bit_rate,error_corr,M_ary,pluse_shape,time_x,freq_x,time_y
    global freq_y,ani,flag_code,samples_data,flag_data_type,xList,yList
    bit_rate=txt_date.get()
    error_corr=cb1.get()
    M_ary=w.get()
    modu=cb2.get()
    pluse_shape=cb3.get()
    time_x=int(time_x_limit.get())
    freq_x=int(freq_x_limit.get())
    time_y=int(time_y_limit.get())
    freq_y=int(freq_y_limit.get())
    a.set(xlim=(0, time_x), ylim=(0,time_y))
    a1.set(xlim=(0, freq_x), ylim=(0,freq_y))
    
    print(flag_data_type)
    
    ani =FuncAnimation(f, animate, blit=False, frames=int(len(xList)/time_x), interval=1, repeat=False)
    f.canvas.draw()
    
def abcd():
    
    reload(py_fi)
    d = py_fi.gen_samples()
    open('py_fi.py', 'w').close()
    return d

def browse_file():
    global file,samples_data,flag_data_type
    file = filedialog.askopenfile()
    text = tk.Text(TAB1,width=30)
    text.insert(tk.INSERT, "File Loaded:"+str(file.name.split('/')[-1]))
    text.place(x=0,y=200)
    global content
    if file is not None:
        content = file.read()
        dataList = content.split('\n')
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xList.append(int(x))
                yList.append(int(y))
    file.close()
    samples_data=yList[0:150]
    flag_data_type='numbers'
    
    
def browse_text():
    
    global popupwindow,text_file_name,var
    var = tk.IntVar()
    popupwindow = tk.Tk()
    popupwindow.wm_title("Text file")
    popupwindow.geometry("285x200")
    
    ttk.Label(popupwindow,text=" File name: ").place(x=10,y=10)
    text_file_name = ttk.Entry(popupwindow,width=20)
    text_file_name.place(x=100,y=10)
    text_file_name.insert(0," out.txt")
    
    ttk.Button(popupwindow, text="OK", command=lambda:save_exit()).place(x=95,y=155)
    ttk.Label(popupwindow,text = "Choose type of data to be in text file").place(x=10,y=60)
    R1=ttk.Radiobutton(popupwindow,text="ASCII",variable = var,value = 1,commmand=sel()).place(x=12,y=90)
    R2=ttk.Radiobutton(popupwindow,text="Text",variable = var,value = 2,commmand=sel()).place(x=12,y=120)
    
def sel():
    global var
    print("You selected the option " + str(var.get()))


def save_exit():
    global popupwindow,text_file_name,TAB2,var
    text_file_type = text_file_name.get()
    popupwindow.destroy()
    text = tk.Text(TAB2,width=30)
    text.insert(tk.INSERT, "Data will be saved in "+text_file_type)
    text.place(x=0,y=200)
    print(var.get())
 
def save_code():
    global st,popwindow,flag_code,flag_data_type
    global file_code,samples_data
    file_code = open("py_fi.py", "w")
    file_code.write(st.get(1.0, tk.END))
    file_code.close()
    text = tk.Text(TAB1,width=30)
    text.insert(tk.INSERT, "The code is loaded \nYou can view our code in code.py file")
    flag_data_type='code'
    d=abcd()
    print(d)
    samples_data = abcd()
    popwindow.destroy()
    
     
def serial_comm(data):
    import serial
    ser = Serial('/dev/ttyACM2', 9600)
    ser.write(data)
    
    
def python_code():
    global st,popwindow
    popwindow = tk.Tk()
    popwindow.wm_title("Code")
    popwindow.geometry("830x565")
    #st = ScrolledText(popwindow, height=25,width=60,ScrollMode=tk.dynamic);
    #st.place(x=0,y=0)
    
    xscrollbar = tk.Scrollbar(popwindow, orient=tk.HORIZONTAL)
    xscrollbar.grid(row=1, column=0,sticky=tk.N+tk.S+tk.E+tk.W)

    yscrollbar = tk.Scrollbar(popwindow)
    yscrollbar.grid(row=0, column=1,sticky=tk.N+tk.S+tk.E+tk.W)

    st = tk.Text(popwindow, wrap=tk.NONE,
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)
    st.grid(row=0, column=0)

    xscrollbar.config(command=st.xview)
    yscrollbar.config(command=st.yview)
    st.insert(tk.END,"#Import all the files here\n\n\n\n\n\ndef gen_samples():\
              \n\t#Write your function here\n\t#Don't forget to add indentation\n\n\n\n")
    st.insert(tk.END,"\tprint(\"Hello\")\n\treturn 3012")

    ttk.Button(popwindow, text="Upload", command=lambda:save_code()).place(x=300,y=515)
    popwindow.mainloop()
    
"""    
def browsefunc():
    file = filedialog.askopenfile()
    global content,int_data
    if file is not None:
        content = file.read()
        print(content)
        int_data = [ord(c) for c in content]
        print(int_data)
    file.close()
 """           
    

def donothing():
   filewin = tk.Toplevel(window)
   button = ttk.Button(filewin, text="Do nothing button")
   button.pack()
   

   
window = tk.Tk()

tk.Tk.wm_title(window, "Software Define Radio")
left = ttk.Frame(window, borderwidth=2)
right = ttk.Frame(window, borderwidth=2)
box1 = ttk.Frame(left, borderwidth=2)
box2 = ttk.Frame(left, borderwidth=2)


left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")
box1.pack(expand=True, fill="both", padx=10, pady=10)
box2.pack(expand=True, fill="both", padx=10, pady=10)

TAB_CONTROL = ttk.Notebook(box1)
#Tab1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text=' Rx Configuration ')
#Tab2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text=' Output type ')
#Tab3
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text=' Graph settings ')

TAB_CONTROL.pack(expand=1, fill="both")

##################################################################
label = tk.Label(TAB2, text=" \t\t\t\t   ", font=LARGE_FONT)
label.pack(side = tk.LEFT)

label1 = tk.Label(window, text=" Visible Light Communication", font=LARGE_FONT)
label1.pack(side=tk.TOP,ipady=20)
browsebutton = ttk.Button(TAB2, text="Text", command =lambda:browse_text()).place(x=250,y=10)

ttk.Label(TAB2,text="Text File Output: ").place(x=10,y=13)


browse_sample = ttk.Button(TAB2, text="Samples", command =lambda:browse_file()).place(x=250,y=50)
ttk.Label(TAB2,text="Sample File Output: ").place(x=10,y=53)

#browse_data = ttk.Button(window, text="Browse_data", command =lambda:browse_data()).place(x=95,y=10)
 
ttk.Label(TAB1,text="Bit rate:").place(x=10,y=10)
txt_date = ttk.Entry(TAB1,width=20)
txt_date.place(x=180,y=10)
txt_date.insert(0,"10")

data=("No code", "Hamming code")
cb1=ttk.Combobox(TAB1, values=data,state = "readonly", width=18,justify="center")
cb1.current(0)
cb1.place(x=180,y=60)

txt = ttk.Label(TAB1, text = "Error correcting code:")
txt.place(x=10,y=60)

data=("PAM", "ASK","PPM")
cb2=ttk.Combobox(TAB1, values=data,state = "readonly",width=18,justify="center")
cb2.current(0)
cb2.place(x=180,y=110)

txt = ttk.Label(TAB1, text = "Modulation:     ").place(x=10,y=110)
txt = ttk.Label(TAB1, text = "Word Length(M) :  ").place(x=10,y=160)

w = ttk.Spinbox( TAB1 , from_=0, to=10, justify="center", width = 3 )
w.place(x=180,y=160)
w.insert(0,2)

data=("Manchester","Polar NRZ","Polar RZ","Bipolar NRZ","Bipolar RZ")
cb3=ttk.Combobox(TAB1, values=data,state = "readonly", width=18,justify="center")
cb3.current(0)
cb3.place(x=180, y=210)

txt = ttk.Label(TAB1, text = "Pulse shaping:")
txt.place(x=10,y=210)

ttk.Label(TAB3,text="Time limit x-axis:").place(x=10,y=50)
time_x_limit = ttk.Entry(TAB3,width=20)
time_x_limit.place(x=180,y=50)
time_x_limit.insert(0,"30")

ttk.Label(TAB3,text="Time limit y-axis:").place(x=10,y=100)
time_y_limit = ttk.Entry(TAB3,width=20)
time_y_limit.place(x=180,y=100)
time_y_limit.insert(0,"2")

ttk.Label(TAB3,text="Frequnecy limit x-axis:").place(x=10,y=150)
freq_x_limit = ttk.Entry(TAB3,width=20)
freq_x_limit.place(x=180,y=150)
freq_x_limit.insert(0,"30")

ttk.Label(TAB3,text="Frequnecy limit y-axis:").place(x=10,y=200)
freq_y_limit = ttk.Entry(TAB3,width=20)
freq_y_limit.place(x=180,y=200)
freq_y_limit.insert(0,"2")

btn = ttk.Button(box2, text="Run",command=run)
btn.place(x=120,y=100)
btn_data = ttk.Button(box2, text="Save Time Response",command=save_time)
btn_data.place(x=20,y=50)

btn_fft = ttk.Button(box2, text="Save Frequency Reponse",command=save_freq)
btn_fft.place(x=190,y=50)
   
btn_reset = ttk.Button(box2, text='Pause', command=pause)
btn_reset.place(x=120,y=150)
btn_reset = ttk.Button(box2, text='Reset', command=reset)
btn_reset.place(x=120,y=200)

global check_loop 
check_loop = 0
def run_loop():
    global check_loop 
    check_loop=1
    btn1 = ttk.Button(box2, text='stop', command=reset)
    btn1.place(x=120,y=250)



#btn1 = ttk.Button(box2, text='loop', command=run_loop)
#btn1.place(x=120,y=250)

btn1 = ttk.Button(box2, text='Exit', command=stop)
btn1.place(x=120,y=250)

####################################################################
canvas = FigureCanvasTkAgg(f, window)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

########################################################################

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Run", command=lambda:run())
filemenu.add_separator()
filemenu.add_command(label="Text file", command=lambda:browse_text())
filemenu.add_command(label="samples file", command=lambda:browse_file())

filemenu.add_separator()

filemenu.add_command(label="Exit", command=stop)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
#########################################################################


window.mainloop()

