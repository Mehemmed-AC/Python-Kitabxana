#Bu Kod Esasen Korona Virusu Melumat Alma Uycun Yazilib
#Bu Koda Ilk Once https://www.worldometers.info/coronavirus/ Bu Saayta Baglanaraq Bu Sayitan 
#Melumat Alir Ama Saytin adini daxil ederken www. ve diger https:// yazmaq lazim deyil
#ve sonda .com Ehdiyac yoxdur.
#Bu Bir sinifdir Birde Asaqida yazacaqim kodu Main Olaraq 
#Isdiafde Ede Bilersiniz

#Bu Koda Ilk Sizden melumat Saytini Ideyecey Ve Sonra Olkenin Adini Daxil Etmeyinizi 
#Isdeyecey

#import MelumatAlici
#
#Stun  = MelumatAlici.MelumatSayitiDaxilEt()
#    
#while True:
#        Oxunan_Olke = input("Olkeni Daxil Eidin :")
#        if Oxunan_Olke == "Cix":
#            print("Programnan Cixldi #EvdeQalin")
#            break
#        else:
#            Baglanti = MelumatAlici.Melumat_Oxuyucu()
#            Baglanti.OlkelerAl(Stun)
#            Baglanti.Olke_Sayari
#            Baglanti.XesdelerAl(Stun)
#            Baglanti.SecilenOlke(Oxunan_Olke)
#            Baglanti.SecilenXesdeSayi()
#            Baglanti.Secilenler
#            Baglanti.MelumatiYazdir()3


import requests
import lxml.html as lh
import pandas as pd

#Bu Fonksiyon Ilk Cagrilan Fonksiyondur ve Bu fonksiyon Geriye Bir List Dondurur
def MelumatSayitiDaxilEt():
    Baglanti_Sayti = "https://"+input("Melumat Saytini Daxil Edin : ")
    Oxunan_Seyfe = requests.get(Baglanti_Sayti)
    Alici = lh.fromstring(Oxunan_Seyfe.content)
    Cedvel_Melumatlari = Alici.xpath('//tr')
    [len(Cedvel) for Cedvel in Cedvel_Melumatlari[:12]]
    Cedvel_Melumatlari = Alici.xpath('//tr')
        
    Stun=[]
    Sayac=0

    for cedvel in Cedvel_Melumatlari[0]:
        Sayac+=1
        name=cedvel.text_content()
        Stun.append((name,[]))
        
    for melumat in range(1,len(Cedvel_Melumatlari)):
        Cedvel=Cedvel_Melumatlari[melumat]
    
        if len(Cedvel) != 10:
            break
    
        Sayac_ic = 0
        for cedvel in Cedvel.iterchildren():
            data=cedvel.text_content() 
            if Sayac_ic > 0:
                try:
                    data=int(data)
                except:
                    pass
            Stun[Sayac_ic][1].append(data)
            Sayac_ic += 1
        
    return Stun

#Bu Sinif Den Bir Obje Yaradaraq O Objeyi Olke Hesab Edmey Olar Bu olkenin Melumatlarini ALmaq Uycun
class Melumat_Oxuyucu():

    def __init__(self):
        self.Olke_Sayari = 0
        self.Olkeler = []
        self.Secilenler = []
        self.Xesdeler = []
        self.Olke_Indexi = 0
        self.Xesde_Indexi = 0
    
    #Burada Olke Al Fonksiyonuna Olke Objesini Baglayirsiniz Ve Listi Daxil Edilirsniz
    def OlkelerAl(self, Stun):
        for olkeler in Stun[0]:
            for SecilenOlkeler in olkeler:
                if olkeler != "Country,Other" and olkeler != "Total:":
                    self.Olke_Sayari += 1
                    self.Olkeler.append(SecilenOlkeler)
            
    #Burda Xesde Al fonksiyonuna Olke Objesini Baglayirsiniz Ve Listi Daxil Edirsiniz 
    def XesdelerAl(self, Stun):
        for xesdeler in Stun[1]:
            for secilenXesdeler in xesdeler:
                if xesdeler != "TotalCases":
                    self.Xesdeler.append(secilenXesdeler)
                    
    #Burd Isdediyiniz Olkeni Daxil Ede Bilersiniz ilk Objeni Baglayin ve Sonra Olkenin Adini Ingilisce Daxil Edirsiniz 
    def SecilenOlke(self, Olke):
        for Secilen_Olke in self.Olkeler:
            self.Olke_Indexi += 1
            if Secilen_Olke == Olke:
                self.Secilenler.append(Secilen_Olke)
                break
                
    #Ve Birde Bu Fonksiyonu Cagirmaqi Unutmayin
    def SecilenXesdeSayi(self):            
        for Secilen_Xesde_Sayi in self.Xesdeler:
            self.Xesde_Indexi += 1
            if self.Olke_Indexi == self.Xesde_Indexi:
                self.Secilenler.append(Secilen_Xesde_Sayi)
    
    #En Sonda Iyse Bu Fonksiyonu Cagiraraq Melumatlari Ekrana Yazdira Bilersiniz
    def MelumatiYazdir(self):
        print("%s'da Corona Virus Sebebiyle Xesde Olan Insan Sayi : %s :<<< %s "%(self.Secilenler[0], str(self.Secilenler[1]), self.OlkeyeGoreMesaj(self.Secilenler[0])))
        
    def OlkeyeGoreMesaj(self, Olke):
        if Olke == "USA":
            return "#Stay At Home"
        elif Olke == "China":
            return "待在家裡"
        elif Olke == "Turkey":
            return "#Evde Kal"
        elif Olke == "Azerbaijan":
            return "#Evde Qal"
        elif Olke == "Russia":
            return "#Ostavaysya Doma"
        elif Olke == "Germany":
            return "#Bleib Zu Hause"  
        elif Olke == "Italy":
            return "#Resta A Casa"
        elif Olke == "Spain":
            return "#Quedarse En Casa"    
        elif Olke == "France":
            return "#Restez a La Maison"   
        elif Olke == "Iran":
            return ""            
        else:
            return ""
           
