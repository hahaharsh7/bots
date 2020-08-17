from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import random
import numpy as np
import pandas as pd
import smtplib

result= []
k = '/users/harsh/downloads/chromedriver'
driver = webdriver.Chrome(k)
driver.get('https://www.cryptofeesaver.com/exchanges/fees/binance')
driver.maximize_window()
BeautifulSoup(driver.page_source)
data = BeautifulSoup(driver.page_source)
name_box = data.findAll('td', attrs={'class': 'align-middle align-right'})
result.append(name_box)
driver.close()

result = result[0]

new = result[1::2]

final = [nigga.text.strip() for nigga in new]

newfinal = [float(h.split()[0]) for h in final]

while True: 
    if 1 - newfinal[33] < 0:
        content = ('update the withdrawal fees of REP')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 0.005 - newfinal[12] < 0:
        content = ('update the withdrawal fees of XMR')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 0.06 - newfinal[16] < 0:
        content = ('update the withdrawal fees of ETC')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 10 - newfinal[17] < 0:
        content = ('update the withdrawal fees of XEM')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 80 - newfinal[54] < 0:
        content = ('update the withdrawal fees of GNT')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 150 - newfinal[89] < 0:
        content = ('update the withdrawal fees of CVC')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 25 - newfinal[23] < 0:
        content = ('update the withdrawal fees of BAT')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 0.01 - newfinal[18] < 0:
        content = ('update the withdrawal fees of ZEC')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 1 - newfinal[30] < 0:
        content = ('update the withdrawal fees of LSK')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 5 - newfinal[60] < 0:
        content = ('update the withdrawal fees of PIVX')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 5 - newfinal[47] < 0:
        content = ('update the withdrawal fees of STRAT')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 50 - newfinal[45] < 0:
        content = ('update the withdrawal fees of SC')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 5 - newfinal[55] < 0:
        content = ('update the withdrawal fees of ARK')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 2 - newfinal[9] < 0:
        content = ('update the withdrawal fees of TRX')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 0.001 - newfinal[0] < 0:
        content = ('update the withdrawal fees of BTC')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 0.05 - newfinal[1] < 0:
        content = ('update the withdrawal fees of ETH')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 5 - newfinal[6] < 0:
        content = ('update the withdrawal fees of USDT')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 0.006 - newfinal[4] < 0:
        content = ('update the withdrawal fees of LTC')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 0.005 - newfinal[5] < 0:
        content = ('update the withdrawal fees of BCH')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 1 - newfinal[2] < 0:
        content = ('update the withdrawal fees of XRP')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 0.01 - newfinal[14] < 0:
        content = ('update the withdrawal fees of DASH')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 0.05 - newfinal[26] < 0:
        content = ('update the withdrawal fees of QTUM')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 5 - newfinal[27] < 0:
        content = ('update the withdrawal fees of OMG')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass

    if 50 - newfinal[38] < 0:
        content = ('update the withdrawal fees of BTS')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('buyuc.notification@gmail.com','buyuc@123')
        mail.sendmail('buyuc.notification@gmail.com','geemax.harsh@gmail.com',content)
    else:
        pass
    
    time.sleep(28800)