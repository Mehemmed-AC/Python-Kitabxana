import requests
import lxml.html as lh
import pandas as pd

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

class Melumat_Oxuyucu():

    def __init__(self):
        self.Olke_Sayari = 0
        self.Olkeler = []
        self.Secilenler = []
        self.Xesdeler = []
        self.Olke_Indexi = 0
        self.Xesde_Indexi = 0

    def OlkelerAl(self, Stun):
        for olkeler in Stun[0]:
            for SecilenOlkeler in olkeler:
                if olkeler != "Country,Other" and olkeler != "Total:":
                    self.Olke_Sayari += 1
                    self.Olkeler.append(SecilenOlkeler)
            
    def XesdelerAl(self, Stun):
        for xesdeler in Stun[1]:
            for secilenXesdeler in xesdeler:
                if xesdeler != "TotalCases":
                    self.Xesdeler.append(secilenXesdeler)
               
    def SecilenOlke(self, Olke):
        for Secilen_Olke in self.Olkeler:
            self.Olke_Indexi += 1
            if Secilen_Olke == Olke:
                self.Secilenler.append(Secilen_Olke)
                break
    
    def SecilenXesdeSayi(self):            
        for Secilen_Xesde_Sayi in self.Xesdeler:
            self.Xesde_Indexi += 1
            if self.Olke_Indexi == self.Xesde_Indexi:
                self.Secilenler.append(Secilen_Xesde_Sayi)
                        
    def MelumatiYazdir(self):
        print("%s'da Corona Virus Sebebiyle Xesde Olan Insan Sayi : %s :<<< %s "%(self.Secilenler[0], str(self.Secilenler[1]), self.OlkeyeGoreMesaj(self.Secilenler[0])))
        
    def OlkeyeGoreMesaj(self, Olke):
        if Olke == "USA":
            return "#Stay At Home"
        elif Olke == "China":
            return "待在家裡 <<< Hamisi Bizim Isimizdi Yenede Evde Qalin ;)"
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
            return "#մնալ տանը <<< BUNU BILEREK ELEDIM ONSUZDA ELMENIDILER"            
        else:
            return ""
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    