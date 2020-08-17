from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome("/Users/harsh/downloads/chromedriver")

    def Login(self):
        bot = self.bot
        bot.get("https://www.twitter.com/login")
        time.sleep(3)
        username = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        password =  bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(3)
        bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
        time.sleep(2)
        
    def like(self):
        bot = self.bot
        bot.get("https://twitter.com/search?q=%23bruh&src=typed_query")
        time.sleep(3)
        bot.execute_script("window.scrollBy(0,500)","")
        time.sleep(2)
    def really_like(self, xpath):
        self.bot.find_element_by_xpath(xpath).click()
        time.sleep(2)
        
go = InstaBot("username" , "password") #change the username and password here 
go.Login()
go.like()
for j in range(10):
    print("Cycle", j)
    for i in range(1,30):
        try:
            xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div[{}]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/span/span'.format(i)
            go.really_like(xpath)
            print(i, "works")
        except:
            print(i, "don't work")
    go.bot.execute_script("window.scrollBy(0,500)","")
    time.sleep(2)