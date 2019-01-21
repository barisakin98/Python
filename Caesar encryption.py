ilk=list("abcçdefghıijklmnoöprsştuüvyz ")
ikinci=list("çdefghıijklmnoöprsştuüvyzabc ")
a=list(ilk)
def kriptolama(mesaj):
    mesaj=mesaj.lower()
    mesaj=list(mesaj)
    yeni_mesaj=""
    for i in mesaj:
        index=ilk.index(i)
        yeni_mesaj+=ikinci[index]

    print("KRİPTOLANDI: ",yeni_mesaj)
def dekritoplama(mesaj):
    mesaj=mesaj.lower()
    mesaj=list(mesaj)
    gercek_mesaj=""
    for i in mesaj:
        index=ikinci.index(i)
        gercek_mesaj+=ilk[index]
    print("KRİPTO ÇÖZÜLDÜ: ",gercek_mesaj)
while True:
    islem=input("KİRPTOALAMAK İÇİN 1 E DEKRİPTOLAMAK İÇİN 2 YE BASINIZ.")
    mesaj = input("MESAJI GİRİNİZ.")
    if islem=="1":

        kriptolama(mesaj)
        print("-------------")
    elif islem=="2":
        dekritoplama(mesaj)
        print("-----------------")
    else:
        print("GEÇERLİ BİR İŞLEM SEÇİN!")
