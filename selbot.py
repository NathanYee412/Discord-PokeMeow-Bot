from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random



#Enter links and credentials
#username and pw  
email = ""
password = ""

#Link to discord channel with bot
discordLink = "https://discord.com/login?redirect_to=%2Fchannels%2F755173566605164615%2F755245005802700862"


#download chromedriver.exe and extract to the .exe to the C drive 
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


#login to discord 
def discordLogin(email, password):
    driver.get(discordLink)

    elemEmail = driver.find_element_by_name("email")
    elemEmail.send_keys(email)

    elemPw = driver.find_element_by_name("password")
    elemPw.send_keys(password)
    elemPw.send_keys(Keys.RETURN)
    time.sleep(10)

#check rarity 
#WIP
def checkRarity():
    rarity = driver.find_element_by_css_selector("span.embedFooterText-28V_Wb")

#shop buy
def shopBuy():
    p = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
    p.send_keys(";shop buy 1 10")
    p.send_keys(Keys.RETURN) 
    

#catch function 
def catchP():
    p = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
    p.send_keys(";p")
    p.send_keys(Keys.RETURN)
    time.sleep(random.randint(3,5))
    p.send_keys("pb")
    p.send_keys(Keys.RETURN)
    time.sleep(random.randint(9,12))


#login to discord
discordLogin(email, password)


#catch pokemon in infinite loop
temp = True
count = 1
while(temp):
    
    #catch pokemon
    catchP()
    count = count + 1
    print(count)

    #buy pokeballs every 10 uses
    if count % 10 == 0:
        shopBuy()
