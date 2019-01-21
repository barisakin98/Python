class Personel:
    liste = []
    def __init__(self,adi,soyadi,bolum):
        self.adi=adi
        self.soyadi=soyadi
        self.bolum=bolum
    def eleman_ekleme(self):
        Personel.liste.append((self.adi,self.soyadi,self.bolum))
        print("Kayıt tamamlandı.")
        print(Personel.liste)
    def eleman_cikarma(self):
        try:
            Personel.liste.remove((self.adi, self.soyadi, self.bolum))
            print("Kayıt silme işlemi tamamlandı.")
            print(Personel.liste)
        except ValueError:
            print("Böyle biri sistemde yok!!!")

nesne1=Personel("ahmet","burak","tıp")
nesne1.eleman_ekleme()
nesne2=Personel("BARİS","AKİN","TIP")
nesne2.eleman_ekleme()
nesne2.eleman_cikarma()
nesne3=Personel("xx","yy","zz")
nesne3.eleman_cikarma()


while True:
    print("PERSONEL KAYIT SİSTEMİNE HOŞGELDİNİZ.")
    islem=input("YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ:\nPERSONEL KAYDI(1)\nKAYIT SİLME(2)\nSistemden çıkmak için(3)")
    if islem=="1":
        kisi_adi=input("Kayıt yapılacak kişinin adını girin.")
        kisi_soyadi=input("Kayıt yapılacak kişinin soyadını girin.")
        kisi_bolumu=input("Kayıt yapılacak kişinin bölümünü girin.")
        nesne=Personel(kisi_adi,kisi_soyadi,kisi_bolumu)
        nesne.eleman_ekleme()
        print(Personel.liste)
    elif islem=="2":
        kisi_adi = input("Kayıt yapılacak kişinin adını girin.")
        kisi_soyadi = input("Kayıt yapılacak kişinin soyadını girin.")
        kisi_bolumu = input("Kayıt yapılacak kişinin bölümünü girin.")
        nesne = Personel(kisi_adi, kisi_soyadi, kisi_bolumu)
        nesne.eleman_cikarma()
        print(Personel.liste)
