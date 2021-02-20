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
    browser.get("https://freedash.io/free")

    username = creds[9]
    password = creds[10]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)

####################################################################

    print("Navigating to Freenem.io")
    browser.get("https://freenem.com/free")

    username = creds[13]
    password = creds[14]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to Freecardano.com")
    browser.get("https://Freecardano.com/free")

    username = creds[17]
    password = creds[18]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to Coinfaucet.io")
    browser.get("https://Coinfaucet.io/free")

    username = creds[21]
    password = creds[22]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to freebitcoin.io")
    browser.get("https://freebitcoin.io/free")

    username = creds[25]
    password = creds[26]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to freesteam.io")
    browser.get("https://freesteam.io/free")

    username = creds[29]
    password = creds[30]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to freeusdcoin.com")
    browser.get("https://freeusdcoin.com/free")

    username = creds[33]
    password = creds[34]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to freechainlink.io")
    browser.get("https://freechainlink.io/free")

    username = creds[37]
    password = creds[38]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to free-tron.com")
    browser.get("https://free-tron.com/free")

    username = creds[41]
    password = creds[42]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to freebinancecoin.com")
    browser.get("https://freebinancecoin.com/free")

    username = creds[45]
    password = creds[46]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to freeneo.io")
    browser.get("https://freeneo.io/free")

    username = creds[49]
    password = creds[50]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)

####################################################################

    print("Navigating to free-ltc.com")
    browser.get("https://free-ltc.com/free")

    username = creds[53]
    password = creds[54]

    #input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    #browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)

####################################################################

    print("Navigating to https://freeethereum.com/")
    browser.get("https://freeethereum.com/free")

    username = creds[57]
    password = creds[58]

    # input("Press Enter to continue...")
    dash_un_field = browser.find_element_by_xpath(
        "/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    dash_un_field.click()
    dash_un_field.send_keys(username)
    print("Entered username")

    time.sleep(1)

    dash_pw_field = browser.find_element_by_xpath(
        "/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    dash_pw_field.click()
    dash_pw_field.send_keys(password)
    print("Entered password")

    time.sleep(1)

    login_button = browser.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    login_button.click()
    print("Clicked Login Button")

    time.sleep(5)

    # browser.get("https://freedash.io/free")

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)

    browser.close()

    print("All sites collected")
    print("Waiting for countdown:")
    for remaining in range(3500, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rComplete!            \n")

    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
    browser.maximize_window()


