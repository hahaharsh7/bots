from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import requests
import time
import random
import numpy as np
import pandas as pd
import smtplib
result  = []
def every12():   
    URL =" https://api.wazirx.com/api/v2/tickers"
    r = requests.get(url = URL) 
    data = r.json() 

    URL1 ="https://api.buyucoin.com/ticker/v1.0/liveData"
    r = requests.get(url = URL1) 
    time.sleep(2)
    dat = r.json() 
    arr1 = []
    for i in dat['data']:
        arr1.append((i['marketName'], i['LTRate']))
    arr1 = dict(arr1)

    check = ['USDT-BTC','INR-BTC','INR-ETH','USDT-ETH','USDT-XRP','INR-XRP','INR-USDT','INR-LTC','USDT-LTC']
    data1 = [arr1[bruh] for bruh in check]
    check2 = [''.join(i.lower().split('-')[::-1]) for i in check]
    data2 = [data[bruh]['buy'] for bruh in check2]

    final =  [(c, float(d1), float(d2)) for c, d1, d2 in zip(check, data1, data2)] 

    mail1 = '''
        Hello,
           BTC-USD price - on warzix is {} , on BuyUcoin is {} , diffrence is {}

           INR-BTC price - on warzix is {} , on BuyUcoin is {} , diffrence is {}

           INR-ETH price - on warzix is {} , on BuyUcoin is {} , diffrence is {}

           USDT-ETH price - on warzix is {} , on BuyUcoin is {} , diffrence is {}

           USDT-XRP price - on warzix is {} , on BuyUcoin is {} , diffrence is {}

           INR-XRP price - on warzix is {} , on BuyUcoin is {} , diffrence is {}

           INR-USDT price - on warzix is {} , on BuyUcoin is {} , diffrence is {}

           INR-LTC price - on warzix is {} , on BuyUcoin is {} , diffrence is {}

           USDT-LTC price - on warzix is {} , on BuyUcoin is {} , diffrence is {}


    '''.format(
               final[0][2], final[0][1],abs(round(final[0][2]- final[0][1])),
               final[1][2],final[1][1],abs(round(final[1][2]- final[1][1])),
               final[2][2],final[2][1],abs(round(final[2][2]- final[2][1])),
               final[3][2],final[3][1],abs(round(final[3][2]- final[3][1])),
               final[4][2],final[4][1],abs(round(final[4][2]- final[4][1])),
               final[5][2],final[5][1],abs(round(final[5][2]- final[5][1])),
               final[6][2],final[6][1],abs(round(final[6][2]- final[6][1])),
               final[7][2],final[7][1],abs(round(final[7][2]- final[7][1])),
               final[8][2],final[8][1],abs(round(final[8][2]- final[8][1]))
                                                                            )

    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('buyuc.notification@gmail.com','buyuc@123')
    mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',mail1)
    time.sleep(28000)


def checkevery():
    URL =" https://api.wazirx.com/api/v2/tickers"
    r = requests.get(url = URL) 
    data = r.json() 

    URL1 ="https://api.buyucoin.com/ticker/v1.0/liveData"
    r = requests.get(url = URL1) 
    time.sleep(2)
    dat = r.json() 
    arr1 = []
    for i in dat['data']:
        arr1.append((i['marketName'], i['LTRate']))
    arr1 = dict(arr1)

    check = ['USDT-BTC','INR-BTC','INR-ETH','USDT-ETH','USDT-XRP','INR-XRP','INR-USDT','INR-LTC','USDT-LTC']
    data1 = [arr1[bruh] for bruh in check]
    check2 = [''.join(i.lower().split('-')[::-1]) for i in check]
    data2 = [data[bruh]['buy'] for bruh in check2]

    final =  [(c, float(d1), float(d2)) for c, d1, d2 in zip(check, data1, data2)] 

    if abs(round(final[0][2]- final[0][1]))>500:
        content = "Please Update the price of USD-bitcoin ASAP , diffrence is"+str(abs(round(final[0][2]- final[0][1])))
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass


    if abs(round(final[1][2]- final[1][1]))>500*80:
        content = "Please Update the price of INR-bitcoin ASAP , diffrence is"+str(abs(round(final[1][2]- final[1][1])))
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass



    if abs(round(final[2][2]- final[2][1]))>80*80:
        content = "Please Update the price of INR-ETH ASAP , diffrence is"+str(abs(round(final[2][2]- final[2][1])))
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass



    if abs(round(final[3][2]- final[3][1]))>80:
        content = "Please Update the price of USD-ETH ASAP , diffrence is"+str(abs(round(final[3][2]- final[3][1])))
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass



    if abs(round(final[4][2]- final[4][1]))>0.1:
        content = "Please Update the price of USDT-XRP ASAP , diffrence is"+str(abs(round(final[4][2]- final[4][1])))
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass



    if abs(round(final[5][2]- final[5][1]))>0.1*80:
        content = "Please Update the price of INR-XRP ASAP , diffrence is"+str(abs(round(final[5][2]- final[5][1])))
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass


    if abs(round(final[7][2]- final[7][1]))>4*80:
        content = "Please Update the price of LTC-INR ASAP , diffrence is"+str(abs(round(final[7][2]- final[7][1])))
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass


    if abs(round(final[7][2]- final[7][1]))>4*80:
        content = "Please Update the price of LTC-USD ASAP , diffrence is"+str(abs(round(final[8][2]- final[8][1])))
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass
    
while True:
    for i in range(96):
        time.sleep(300)
        checkevery()
    every12()