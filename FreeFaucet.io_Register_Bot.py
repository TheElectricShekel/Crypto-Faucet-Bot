from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from io import BytesIO
import time
import keyboard
import sys
from random import randrange
import os

driver_path = "chromedriver.exe"
brave_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

dir_path = os.path.dirname(os.path.realpath(__file__))
credentials = "creds.txt"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--incognito")
#option.add_argument("--headless")

with open(credentials) as f:
    creds = f.readlines()
time.sleep(1)

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser.maximize_window()
print("Browser launched")

#r = 1

while True:
    print("Navigating to Freedash.io")
    browser.get("https://freedash.io/?ref=84771")

    username = creds[9]
    password = creds[10]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)

####################################################################

    print("Navigating to Freenem.io")
    browser.get("https://freenem.com/?ref=264523")

    username = creds[13]
    password = creds[14]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to Freecardano.com")
    browser.get("https://freecardano.com/?ref=274019")

    username = creds[17]
    password = creds[18]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to Coinfaucet.io")
    browser.get("https://coinfaucet.io/?ref=747848")

    username = creds[21]
    password = creds[22]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to freebitcoin.io")
    browser.get("https://freebitcoin.io/?ref=424218")

    username = creds[25]
    password = creds[26]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to freesteam.io")
    browser.get("https://freesteam.io/?ref=95823")

    username = creds[29]
    password = creds[30]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to freeusdcoin.com")
    browser.get("https://freeusdcoin.com/?ref=99087")

    username = creds[33]
    password = creds[34]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to freechainlink.io")
    browser.get("https://freechainlink.io/?ref=52222")

    username = creds[37]
    password = creds[38]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to free-tron.com")
    browser.get("https://free-tron.com/?ref=147925")

    username = creds[41]
    password = creds[42]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to freebinancecoin.com")
    browser.get("https://freebinancecoin.com/?ref=100259")

    username = creds[45]
    password = creds[46]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to freeneo.io")
    browser.get("https://freeneo.io/?ref=62439")

    username = creds[49]
    password = creds[50]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to free-ltc.com")
    browser.get("https://free-ltc.com/?ref=67660")

    username = creds[53]
    password = creds[54]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)
####################################################################

    print("Navigating to https://freeethereum.com/")
    browser.get("https://freeethereum.com/?ref=145922")

    username = creds[57]
    password = creds[58]

    reg_button = browser.find_element_by_xpath("/html/body/header/div/div[1]/nav/div/ul/li[4]/a")
    reg_button.click()

    time.sleep(1)

    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered e-mail")

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    dash_pw_field2 = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/div[3]/input")
    dash_pw_field2.click()
    dash_pw_field2.send_keys(password)
    print("Confirmed password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[2]/button")
    login_button.click()
    print("Clicked Register Button")

    time.sleep(5)

    browser.close()

    print("All sites registered")
    print("Click the registration links in your e-mail for each site")
    print("Then run the main FreeFaucet.io_Bot")



