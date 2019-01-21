import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

alıcı=input("E posta göndereceğiniz kişinin adresini yazınız..")
konu_basligi=input("Göndereceğiniz e postanın konu başlığını yazınız..")
mesaj=input("İletinizi yazınız..")


parolamız="dfjnsdjlflnsdfsd"
kendi_adresimiz="vsvsvsvsvvs@gmail.com"
gönderi=MIMEMultipart()gönderi["From"]=kendi_adresimiz
gönderi["To"]=alıcı
gönderi_yazı=MIMEText(mesaj,"plain") 
gönderi.attach(gönderi_yazı)
gönderi["Subject"]=konu_basligi


i=0
while i<25:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(kendi_adresimiz, parolamız)
    mail.sendmail(kendi_adresimiz, alıcı, gönderi.as_string())
    print("İleti gönderildi..")
    mail.close()
    i+=1
