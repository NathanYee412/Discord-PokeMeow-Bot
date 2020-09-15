from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time
import random



#download chromedriver.exe and extract to the .exe to the C drive
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#email and pw
email = ""
password = ""

# your discord @
DISCORD_AT = ""

#link to discord text channel
discordLink = ""

#login to discord
def discordLogin(email, password):
    driver.get(discordLink)
    time.sleep(5)
    elemEmail = driver.find_element_by_name("email")
    elemEmail.send_keys(email)

    elemPw = driver.find_element_by_name("password")
    elemPw.send_keys(password)
    elemPw.send_keys(Keys.RETURN)
    time.sleep(10)

#check rarity
#WIP
def checkRarity():
    message_list = WebDriverWait(driver, timeout=9).until(lambda d: d.find_elements_by_class_name("container-1ov-mD"))
    last_element = message_list[-1]

    element = WebDriverWait(last_element, timeout=5).until(lambda d: d.find_elements_by_css_selector("span.embedFooterText-28V_Wb"))

    if len(element) == 0:
        return "Error"
    element = element[0]

    text = element.text.split()
    print(element.text)
    return text[0]

def spawn(p):
    p.send_keys(";p")
    p.send_keys(Keys.RETURN)

def pb(p):
    p.send_keys("pb")
    p.send_keys(Keys.RETURN)


def gb(p):
    p.send_keys("gb")
    p.send_keys(Keys.RETURN)

def ub(p):
    p.send_keys("ub")
    p.send_keys(Keys.RETURN)

def mb(p):
    p.send_keys("mb")
    p.send_keys(Keys.RETURN)

def getXpath(i):
    return "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/div[1]/div/div/div/div[" + str(i) + "]"

# can do something better than ping to alert you of captchan since it doesn't actually give you a notif
def ping(p):
    p.send_keys(DISCORD_AT)
    p.send_keys(Keys.TAB)
    p.send_keys(Keys.RETURN)



#PB index = 13
#UB index = 16
#GB index = 18

#return list of pb count
def getPbCount():
    message_list = WebDriverWait(driver, timeout=9).until(lambda d: d.find_elements_by_class_name("container-1ov-mD"))
    last_element = message_list[-1]

    element = WebDriverWait(last_element, timeout=5).until(lambda d: d.find_elements_by_css_selector("span.embedFooterText-28V_Wb"))

    if len(element) == 0:
        return "Error"
    element = element[0]

    text = element.text.split()
    print(element.text)

    pbList = [text[13], text[18], text[16]]
    return pbList

#shop buy pokeballs 
def shopBuy(pbList):
    if int(pbList[0]) <= 5:
        p.send_keys(";shop buy 1 5")
        p.send_keys(Keys.RETURN)
    if int(pbList[1]) <= 5:
        p.send_keys(";shop buy 2 5")
        p.send_keys(Keys.RETURN)
    if int(pbList[2]) <= 5:
        p.send_keys(";shop buy 3 5")
        p.send_keys(Keys.RETURN)

    time.sleep(random.randint(4,6))



#login to discord
discordLogin(email, password)
#catch pokemon in infinite loop
p = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]")

x = True
while(x):
    spawn(p)
    time.sleep(random.randint(1,2) + random.random())
    rarity = checkRarity()
    print(rarity)

    #get pb list 
    pbList = getPbCount()

    time.sleep(random.randint(1,3) + random.random())
    if rarity == "Common":
        pb(p)
    elif rarity == "Uncommon":
        gb(p)
    elif rarity == "Rare":
        gb(p)
    elif rarity == "Super":
        ub(p)
    elif rarity =="Error":
        ping(p)
        quit()
    else:
        mb(p)

    time.sleep(random.randint(9,12) + random.random())

    #buy more pb
    shopBuy(pbList)
