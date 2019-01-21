import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

receiver=input("Write your receiver.")
subject_title=input("Write the title.")
message=input("Write your message here.")


parolamız="your password"
kendi_adresimiz="your gmail"
gönderi=MIMEMultipart()gönderi["From"]=kendi_adresimiz
gönderi["To"]=receiver
gönderi_yazı=MIMEText(message,"plain") 
gönderi.attach(gönderi_yazı)
gönderi["Subject"]=subject_title


i=0
while i<25:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(kendi_adresimiz, parolamız)
    mail.sendmail(kendi_adresimiz, receiver, gönderi.as_string())
    print("İleti gönderildi..")
    mail.close()
    i+=1
