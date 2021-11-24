import tkinter as tk
from tkinter import ttk
import numpy as np


win=tk.Tk()
win.title("moment")

win.resizable(True,True) 

ttk.Label(win,text="Span length:").grid(row=0,column=0,padx=5,pady=5,sticky="E")
SP=tk.StringVar()
ttk.Entry(win,width=4,textvariable=SP).grid(row=0,column=1,padx=5,pady=5, sticky='E')


ttk.Label(win,text="Load intensity:").grid(row=2,column=0,padx=5,pady=5,sticky="E")
LI=tk.StringVar()
ttk.Entry(win,width=4,textvariable=LI).grid(row=2,column=1,padx=5,pady=5)

ttk.Label(win,text="Identify distance from left support:").grid(row=4,column=0,padx=5,pady=5,sticky="E")
DL=tk.StringVar()
ttk.Entry(win,width=4,textvariable=DL).grid(row=4,column=1,padx=5,pady=5)


ttk.Label(win,text="Identify distance from right support:").grid(row=6,column=0,padx=5,pady=5,sticky="E")
DR=tk.StringVar()
ttk.Entry(win,width=4,textvariable=DR).grid(row=6,column=1,padx=5,pady=5)

def clickSolve():
    L=eval(SP.get())
    w=eval(LI.get())
    x1=eval(DL.get())
    x2=eval(DR.get())
    BENDING_MOMENT_FROM_LEFT_SUPPORT=w*(((-6))*(x1**2)+(6*L*x1)-(L**2))/12
    BENDING_MOMENT_FROM_RIGHT_SUPPORT=(w*((-6*(x2**2)+(6*L*x2)-(L**2))))/12
    ttk.Label(win,text=str( BENDING_MOMENT_FROM_LEFT_SUPPORT)).grid(row=8,column=1)
    ttk.Label(win,text=str( BENDING_MOMENT_FROM_RIGHT_SUPPORT)).grid(row=10,column=1)
    SHEAR_FORCE_AT_LEFT_SUPPORT=w*((L/2)-(x1))
    SHEAR_FORCE_AT_RIGHT_SUPPORT=w*((L/2)-(x2))
    ttk.Label(win,text=str( SHEAR_FORCE_AT_LEFT_SUPPORT)).grid(row=12,column=1)
    ttk.Label(win,text=str( SHEAR_FORCE_AT_RIGHT_SUPPORT)).grid(row=14,column=1)
solveButton=ttk.Button(win,text="Solve",command=clickSolve)
solveButton.grid(row=1,column=0,columnspan=4)






 

ttk.Label(win,text="Bending moment from left support:").grid(row=8,column=0,padx=5,pady=5,sticky="E")
ttk.Label(win,text="Bending moment from right support:").grid(row=10,column=0,padx=5,pady=5,sticky="E")
ttk.Label(win,text="Shear force from left support:").grid(row=12,column=0,padx=5,pady=5,sticky="E")
ttk.Label(win,text="Shear force from from support:").grid(row=14,column=0,padx=5,pady=5,sticky="E")









win.mainloop() 