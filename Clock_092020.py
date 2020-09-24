#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
import locale , requests
from   PIL    import Image, ImageTk, ImageDraw
import time
import numpy as np
import os
import socket
import glob


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

locales = ['pt_BR.utf-8']
for loc in locales:
    locale.setlocale(locale.LC_ALL, loc)
root = tk.Tk()
root.attributes("-fullscreen", True) 

#Carrega a imagem de fundo
image=ImageTk.PhotoImage(Image.open("mitr4tran_092020.png"))

#Grupo de cores que irão variar
color = ["white", "misty rose", "gray", "cornflower blue", "medium blue",
         "light sky blue", "cyan", "lime green", "gold", 'indian red','salmon','tomato', 'pale violet red'
        , 'light pink','dark orchid', 'SlateBlue1', 'LightBlue1']
cnt = 0
colour = 'white'
canvas = tk.Canvas(root,width=480,height=320,bd=0, highlightthickness=0,background=colour)
#Posicionamento da imagem e palavras
canvas.create_image(0,0,anchor='nw',image=image)

clock_datetime = canvas.create_text(100, 30, fill="white", font=("arial", 60, "bold"),anchor='center')
clock_second = canvas.create_text(220, 20, fill="white", font=("arial", 22, "bold"),anchor='center')

clock_temperature = canvas.create_text(250, 80, fill=color[0], font=("arial", 22, "bold"),anchor='center')
clock_motor = canvas.create_text(85, 225, fill=color[0], font=("arial", 20, "bold"),anchor='center')

clock_tank = canvas.create_text(380, 80, fill=color[0], font=("arial", 22, "bold"),anchor='center')

clock_kmh = canvas.create_text(275, 200, fill=color[0], font=("arial", 110, "bold"),anchor='center')
clock_kmh_unit = canvas.create_text(420, 245, fill=color[0], font=("arial", 18, "bold"),anchor='center')

clock_date = canvas.create_text(165, 300, fill=color[0], font=("arial", 20, 'bold'),anchor='center')
clock_dateweek = canvas.create_text(320, 300, fill=color[0], font=("arial", 20, 'bold'),anchor='center')


canvas.pack()

mot = 100
gas = 20
vel = 61
temperatura = 28    

#Faz a troca da cor a cada minuto no segundo 1
def getcolor():
    if (int(time.strftime('%S')) == 1):
        if (int(time.strftime('%M'))%1) == 0:
            global cnt 
            cnt+=1
            if cnt > 16:
                cnt = 0
            colour = color[cnt] 
            canvas.configure(background=colour)
            

              
def update():
    try: 
        color_mot = color[3]
        color_temp = color[3]
        color_gas = color[0]
        color_vel = color[0]
        colour = color[cnt]
        
        temperatura = read_temp()
        if(mot > 95):
            color_mot = color[10]
        if(gas < 25):
            color_gas = color[10]
        if(vel > 60):
            color_vel = color[8]
        if(vel > 80):
            color_vel = color[10]
        if(temperatura > 35):
            color_temp = color[10]
        date = "%s" % (time.strftime('%A').title())
        week = "%s" % (time.strftime('%d/%m/%Y'))
        hora = time.strftime('%H:%M') # local
        segundo = time.strftime('.%S') # local
        temperaturas = "%.1f°C"  % (temperatura)
        motor = "%s°C" % mot
        percent = "%"
        fuel = "%s%s " % (gas,percent )
        
        canvas.itemconfigure(clock_date, text=date, fill=colour)
        canvas.itemconfigure(clock_dateweek, text=week, fill=colour)
        canvas.itemconfigure(clock_datetime, text=hora)
        canvas.itemconfigure(clock_second, text=segundo)
        canvas.itemconfigure(clock_temperature, text=temperaturas, fill=color_temp)
        canvas.itemconfigure(clock_motor, text=motor, fill=color_mot)
        canvas.itemconfigure(clock_tank, text=fuel, fill=color_gas)
        canvas.itemconfigure(clock_kmh, text=vel, fill=color_vel)
        canvas.itemconfigure(clock_kmh_unit, text="Km/h", fill=colour)
        canvas.update()
        getcolor()
        root.after(1000, update)
        
    except StopIteration:
        pass

update()
root.mainloop()


# In[ ]:



