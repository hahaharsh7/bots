from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import random
a = str(input("Enter path to chromedriver: "))
for i in range(20):
    driver = webdriver.Chrome(a)
    driver.get("https://google.com")
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("Buy bitcoin in india")
    time.sleep(random.randint(1, 5)) 
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').click()
    time.sleep(2)
    for i in range(45):
        driver.execute_script("window.scrollBy(0,40)","")
        time.sleep(0.4)
    try:
        driver.find_element_by_partial_link_text('BuyUcoin | Global Cryptocurrency Exchange & Wallet in India').click()
        time.sleep(2)
        for i in range(45):
            driver.execute_script("window.scrollBy(0,40)","")
            time.sleep(0.4)
        driver.close()
    except:
        driver.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[3]/a').click()
        time.sleep(3)
        driver.find_element_by_partial_link_text('BuyUcoin | Global Cryptocurrency Exchange & Wallet in India').click()
        time.sleep(2)
        for i in range(45):
            driver.execute_script("window.scrollBy(0,40)","")
            time.sleep(0.4)
        driver.close()
    else:
        driver.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[4]/a').click()
        time.sleep(2)
        driver.find_element_by_partial_link_text('BuyUcoin | Global Cryptocurrency Exchange & Wallet in India').click()
        time.sleep(2)
        for i in range(45):
            driver.execute_script("window.scrollBy(0,40)","")
            time.sleep(0.4)
        driver.close()
