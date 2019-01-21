import random
class Oyun:
    def __init__(self,isim,can,mermi_hasari,mermi_sayisi):
        self.isim=isim
        self.can=can
        self.mermi_hasari=mermi_hasari
        self.mermi_sayisi=mermi_sayisi
    def kalan_can(self,isabet_sayisi,mermi_gucu):
        alinan_hasar = isabet_sayisi * mermi_gucu
        self.can -= alinan_hasar

terrorist=[]
komandolar=[]
i=0
while i<10:
    isim="terror"+str(i)
    r_can=random.randrange(20,80)
    r_mermi_hasari=random.randrange(1,10)
    r_mermi_sayisi=random.randrange(1,10)
    terrorists=Oyun(isim,r_can,r_mermi_hasari,r_mermi_sayisi)
    terrorist.append(terrorists)
    i+=1
i=0
while i<5:
    isim="komando"+str(i)
    r_can=150
    r_mermi_sayisi=random.randrange(5,10)
    r_mermi_hasari=random.randrange(1,10)
    komandos=Oyun(isim,r_can,r_mermi_hasari,r_mermi_sayisi)
    komandolar.append(komandos)
    i+=1

while True:
    if len(komandolar)==0:
        print("Teröristler kazandı.")
        print("Komandolar yenildi.")
        print(len(terrorist),"terörist yaşıyor.!")
        break
    elif len(terrorist)==0:
        print("KOMANDOLAR KAZANDI.")
        print("Teröristler kaybetti")
        print(len(komandolar),"komando yaşıyor.!")
        break

    for x in komandolar:
        try:
            hedef = random.choice(terrorist)
            hedef.kalan_can(random.randrange(x.mermi_sayisi), x.mermi_hasari)
            if hedef.can <= 0:
                terrorist.remove(hedef)
            print("Komandolar: ",len(komandolar))
            print("Teröristler: ",len(terrorist))
        except IndexError:
            print("Komandolar kazandı.")
            print("Teröristler yenildi.")
            print(len(komandolar),"komando yaşıyor.")
            break

    for m in terrorist:
        try:
            hedef_a = random.choice(komandolar)
            hedef_a.kalan_can(random.randrange(m.mermi_sayisi), m.mermi_hasari)
            if hedef_a.can <= 0:
                komandolar.remove(hedef_a)
            print("Komandolar: ", len(komandolar))
            print("Teröristler: ", len(terrorist))
        except IndexError:
            print("Teröristler kazandı.")
            print("Komandolar yenildi.")
            print(len(terrorist)," terörist yaşıyor ")
            break
