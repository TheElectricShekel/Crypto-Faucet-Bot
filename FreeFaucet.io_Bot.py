from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
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

browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser.maximize_window()
print("Browser launched")

while True:
    print("Navigating to https://Freedash.io")
    browser.get("https://freedash.io/free")

    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

    try:
        ad_close = browser.find_element_by_xpath("/html/body/div[1]/div")
        ad_close.click()
    except:
        pass

    username = creds[9]
    password = creds[10]

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)

####################################################################

    print("Navigating to https://Freenem.io")
    #try:
    #    browser.get("https://freenem.com/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()
    browser.get("https://freenem.com/free")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

    username = creds[13]
    password = creds[14]

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to https://Freecardano.com")
    #try:
    #    browser.get("https://Freecardano.com/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()
    browser.get("https://Freecardano.com/free")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

    username = creds[17]
    password = creds[18]

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to https://Coinfaucet.io")
    #try:
    #    browser.get("https://Coinfaucet.io/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()
    browser.get("https://Coinfaucet.io/free")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

    username = creds[21]
    password = creds[22]

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to https://freebitcoin.io")
    #try:
    #    browser.get("https://freebitcoin.io/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()

    browser.get("https://freebitcoin.io/free")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

    username = creds[25]
    password = creds[26]

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to https://freesteam.io")
    #try:
    #    browser.get("https://freesteam.io/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()

    browser.get("https://freesteam.io/free")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

    username = creds[29]
    password = creds[30]

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to https://freeusdcoin.com")
    #try:
    #    browser.get("https://freeusdcoin.com/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()

    browser.get("https://freeusdcoin.com")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

    username = creds[33]
    password = creds[34]

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to https://freechainlink.io")
    #try:
    #    browser.get("https://freechainlink.io/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()

    browser.get("https://freechainlink.io/free")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

    username = creds[37]
    password = creds[38]

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to https://free-tron.com")
    #try:
    #    browser.get("https://free-tron.com/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()

    browser.get("https://free-tron.com/free")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to https://freebinancecoin.com")
    #try:
    #    browser.get("https://freebinancecoin.com/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()

    browser.get("https://freebinancecoin.com/free")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)
####################################################################

    print("Navigating to https://freeneo.io")
    #try:
    #    browser.get("https://freeneo.io/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()

    browser.get("https://freeneo.io/free")
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        browser.refresh()
        print("No bot alerts found")

    username = creds[49]
    password = creds[50]

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

    try:
        roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        roll_button.click()
        print("Clicked roll button")
        time.sleep(10)
    except ElementNotInteractableException:
        print("No roll button found")
    time.sleep(10)

    browser.close()

####################################################################

    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

    print("Navigating to https://free-ltc.com")
    #time.sleep(5)
    #try:
    #    browser.get("https://free-ltc.com/free")
    #except UnexpectedAlertPresentException:
    #    browser.refresh()
    #browser.refresh()
    time.sleep(5)
    try:
        browser.get("https://free-ltc.com/free")
        time.sleep(5)
        browser.refresh()
        time.sleep(5)
        print("Checking for bot alerts")
    except:
        browser.get("https://freeethereum.com/free")
        time.sleep(5)
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

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
    print("Checking for bot alerts")
    try:
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()
        print("Found bot alert, refreshing page")
        browser.refresh()
    except TimeoutException:
        print("No bot alerts found")

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


