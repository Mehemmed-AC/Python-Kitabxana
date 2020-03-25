import platform
import socket
import re
import uuid
import json
import psutil
import tkinter
import sys
import os

def SystemMelumatlari():
    return ["ayir", "SYSTEM MELUMATLARI", platform.machine(), platform.version(), platform.platform(), platform.uname(), platform.system(),  platform.processor(), 
       platform.release(), socket.gethostname(), socket.gethostbyname(socket.gethostname()), str(':'.join(re.findall('..', '%012x' % uuid.getnode()))),
       str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB" , "ayir", "PYTHON MELUMATLARI", platform.python_version(), 
       platform.python_version_tuple(), platform.python_compiler(), platform.python_build(), "ayir", "PLATFORM MELUMATLARI", platform.platform(), platform.platform(aliased=True), 
       platform.platform(terse=True), platform.architecture(), platform.architecture('/bin/ls')]

class Aplikasya():
    
    def __init__(self, Ad, Olcusu):
        self.root = tkinter.Tk()
        self.root.title(Ad)
        self.root.geometry(Olcusu)
        self.Ad = Ad

    def RootCagir(self):
        Root = self.root

        return Root
    
    def Baslad(self):
        self.root.mainloop()

    def Yerlesdir(self, Object):
        return Object.grid()  

    def YaziYarad(self, yazi, x, y, bayrag, reng='black'):
        Yazi = tkinter.Label(text = yazi, fg = reng)
        Yazi.pack()
        if bayrag == True:
            Yazi.place(x = x, y = y)

        return Yazi
    
    def DuymeYarad(self, Ad, x, y, bayrag, funct):
        Duyme = tkinter.Button(self.root, text = Ad, comman = funct)
        Duyme.pack()
        Duyme.place(x=x, y=y)

        return Duyme
    
    def ListYarad(self, Sayi, ListElaveEt, Olcusu):
        List = tkinter.Listbox(self.root)
        List.insert(Sayi, ListElaveEt)
        List.pack()
        
        return List

    def CanvasYarad(self, Reng, Hundurluk, eni):
        Canvas = tkinter.Canvas(self.root, bg = Reng, height = Hundurluk, width = eni) 
        
        return Canvas
    
    def CanvasYaz(self, Canvas, Reng):
        Yazilan = Canvas.create_arc((5,10,150,200),start = 0,extent = 150, fill = Reng)
        Canvas.pack()

        return Yazilan  

    def Deyisen(self):
        deyisen = tkinter.IntVar() 
        
        return deyisen

    def SecilenDuymeYarad(self, deyisen, yazi, eni):
        secilenduymeyarad = tkinter.Checkbutton(self.root, text = yazi, variable = deyisen, onvalue = 1, offvalue = 0, height = 2, width = eni)  
        secilenduymeyarad.pack()
        
        return secilenduymeyarad

    def GlobalDeyisenYarad(self):
        return tkinter.StringVar()

    def GlobalDeyiseniAlan(self, GlobalDeyisenYarad):
        return GlobalDeyisenYarad.get()

    def DaxilediciYarad(self, Global_Deyisen):
        Daxiledici = tkinter.Entry(self.root, textvariable=Global_Deyisen)
        Daxiledici.pack()
    
        return  Daxiledici
    
    def MenuDuymesiUycunMenuYarad(self, menubutton, Deyisen, yazi):
        menubutton.menu.add_checkbutton(label = yazi, variable=Deyisen)  
        menubutton.pack()

    def MenuDuymesiYarad(self, yazi):
        menubutton = tkinter.Menubutton(self.root, text = yazi)  
        menubutton.menu = tkinter.Menu(menubutton)  
        menubutton["menu"]=menubutton.menu  

        return menubutton
    
    def menubarmenusuyarad(self, menubar, menulist, bayrag, yazi, funct ):
        if bayrag == True:
            menubar.add_cascade(label=yazi, menu=menulist)  
        else:
            menubar.add_command(label=yazi, command=funct)
    
    def MenuBarYarad(self):
        menubar = tkinter.Menu(self.root)  

        return menubar

    def menubaryerllesidr(self, menubar):
        self.root.config(menu=menubar)  

    def menulistyarad(self, menubar ):
        return tkinter.Menu(menubar, tearoff=0)  

    def menulistelaveet(self, menulist, yazi, funct):
        menulist.add_command(label=yazi, command=funct)  

    def menulistkonfiqurasyaet(self, menulist):
        menulist.add_separator()  

    def mesaj(self, yazi):
        mesaj = tkinter.Message(self.root, text = yazi, padx = 10, pady=200)  
        mesaj.pack()  

        return mesaj
    
    def secilenduymeyarad(self, yazi, deyisen, deyer, secilen):
        secilenduyme = tkinter.Radiobutton(self.root, text=yazi, variable=deyisen, value=deyer, command=secilen) 
        secilenduyme.pack()

        return secilenduyme
    
    def secilenduymeucundeyisenyarad(self):
        return tkinter.IntVar()  
    
    def secilendeyericagir(self, deyisen):
        return deyisen.get()