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
result= []
k = str(input("enter path to chromedriver")) 
driver = webdriver.Chrome(k)
driver.get("https://google.com")
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("crypto + inurl:submit-guest-post")
time.sleep(random.randint(1, 5)) 
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
time.sleep(2)
for i in range(7):
    BeautifulSoup(driver.page_source)
    data = BeautifulSoup(driver.page_source)
    name_box = data.findAll('cite', attrs={'class': 'iUh30 bc tjvcx'})
    result.append(name_box)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="pnnext"]').click()
    time.sleep(3)

result