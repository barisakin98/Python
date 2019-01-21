import requests
from bs4 import BeautifulSoup

url="http://www.sanalhekim.com/blog"
response=requests.get(url)
icerik=response.content
kaynak=BeautifulSoup(icerik,"html.parser")
for i in kaynak.find_all("div",{"class":"card-content center-align"}):
    print(i.text)
    print("****")
