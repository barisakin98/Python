import time,random
liste=[]
while len(liste)<100:
    a=random.randrange(0,10)
    b=random.randrange(0,10)
    t=(a,b)
    liste.append(t) #rastgele nokta seçimini bu şekilde de yapabiliriz.
referans=[2,1]
karsilastirma=[]
sira=[]
alinan_yol=0
def mesafe_bulma(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
while len(liste)!=0:
    for i in liste:
        karsilastirma.append(mesafe_bulma(referans,i))
    
    x=liste[karsilastirma.index(min(karsilastirma))]
    sira.append(x)
    liste.remove(x)
    karsilastirma = []
    referans=x
print("ROTA BELİRLENİYOR..")
time.sleep(2)
print("ROTANIZ: ",sira)
def printf(s):
    print(s)
