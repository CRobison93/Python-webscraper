from bs4 import BeautifulSoup
import requests
import smtplib
import datetime
import time

#connect to website and pull data#

URL = "https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'\n"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"}
 
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

print(soup1)




