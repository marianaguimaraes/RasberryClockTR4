#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import locale , requests
from   PIL    import Image, ImageTk, ImageDraw
import time
import numpy as np
import os

locales = ['pt_BR.utf-8']
for loc in locales:
    locale.setlocale(locale.LC_ALL, loc)
root = tk.Tk()
root.attributes("-fullscreen", True) 


#image=ImageTk.PhotoImage(Image.open("C:\\Users\\MGuimaraes\\Pictures\\mitr4tran2.png"))
image=ImageTk.PhotoImage(Image.open("mitr4tran.png"))
color = ["white", "misty rose", "gray", "cornflower blue", "medium blue",
         "light sky blue", "cyan", "lime green", "gold", 'indian red','salmon','tomato', 'pale violet red'
        , 'light pink','dark orchid', 'SlateBlue1', 'LightBlue1']
cnt = 0
colour = 'white'
canvas = tk.Canvas(root,width=480,height=320,bd=0, highlightthickness=0,background=colour)
canvas.create_image(0,0,anchor='nw',image=image)
clock_date = canvas.create_text(310, 80, fill=color[0], font=("arial", 22, 'bold'),anchor='center')
clock_dateweek = canvas.create_text(310, 120, fill=color[0], font=("arial", 32, 'bold'),anchor='center')
clock_datetime = canvas.create_text(240, 200, fill="white", font=("arial", 90, "bold"),anchor='center')
clock_second = canvas.create_text(420, 225, fill="white", font=("arial", 32, "bold"),anchor='center')
clock_temperature = canvas.create_text(250, 270, fill=color[0], font=("arial", 22, "bold"),anchor='center')
clock_clima = canvas.create_text(250, 300, fill=color[0], font=("arial", 22, "bold"),anchor='center')

canvas.pack()

import socket

confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
temperatura = "Aguardando Conexão"
report_wea = "Aguardando Conexão"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Fortaleza"
API_KEY = "58b2429114c594ec347babf9a1212c9d"
# upadting the URL
URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&lang=pt"
# HTTP request

def check_host():
    global confiaveis
    for host in confiaveis:
        a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.settimeout(.5)
        try:
            b=a.connect_ex((host, 80))
            if b==0: #ok, conectado
                return True
        except:
            pass
        a.close()
        return False


def getweather():
    result_conn = check_host()
    if result_conn == True:
        response = requests.get(URL)
        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            global temperature, temperatura
            temperature = format(main['temp'] - 273.15,'.1f') + "°C"   
            temperatura = temperature
            # weather report
            global report , report_wea
            report = data['weather']
            report_wea = report[0]['description'].title()
            os.system ("sudo /home/pi/disconn.sh")
    else:
        # showing the error message
        os.system ("sudo /home/pi/conn.sh")
        time.sleep(2)
        result_conn = check_host()
        if result_conn == False:
            os.system ("sudo /home/pi/connSu.sh")
            temperatura = "Pesquisando..."
            report = "Pesquisando..."
    

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
        colour = color[cnt]
        date = "%s" % (time.strftime('%A').title())
        week = "%s" % (time.strftime('%d/%m/%Y'))
        hora = time.strftime('%H:%M') # local
        segundo = time.strftime('.%S') # local
        temperaturas = "Clima: %s" % (temperatura)
        clima = "%s" % (report_wea)
        canvas.itemconfigure(clock_date, text=date, fill=colour)
        canvas.itemconfigure(clock_dateweek, text=week, fill=colour)
        canvas.itemconfigure(clock_datetime, text=hora)
        canvas.itemconfigure(clock_second, text=segundo)
        canvas.itemconfigure(clock_temperature, text=temperaturas, fill=colour)
        canvas.itemconfigure(clock_clima, text=clima, fill=colour)
        canvas.update()
        getcolor()
        root.after(1000, update)
        
    except StopIteration:
        pass

update()
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:



