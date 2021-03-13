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

timer = 0

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--incognito")
#option.add_argument("--headless")

with open(credentials) as f:
    creds = f.readlines()
time.sleep(1)

bot_attempt = 0
dash_bot = 0
nem_bot = 0
ada_bot = 0
xrp_bot = 0
btc_bot = 0
steam_bot = 0
usdc_bot = 0
link_bot = 0
tron_bot = 0
bnc_bot = 0
neo_bot = 0
ltc_bot = 0
eth_bot = 0
dash_skip = 0
nem_skip = 0
ada_skip = 0
xrp_skip = 0
btc_skip = 0
steam_skip = 0
usdc_skip = 0
link_skip = 0
tron_skip = 0
bnc_skip = 0
neo_skip = 0
ltc_skip = 0
eth_skip = 0


def login():
    try:
        print("Checking for ad overlay")
        ad_check = browser.find_element_by_id("fbf-mobile-close-coinzilla")
        ad_check.click()
        print("Ads closed")
    except NoSuchElementException:
        print("No Ads found")

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


browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser.maximize_window()
print("Browser launched")

while True:
    if dash_bot <= 2:
        try:
            print("Navigating to https://Freedash.io")
            browser.get("https://freedash.io/free")

            username = creds[9]
            password = creds[10]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                dash_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        dash_skip += 1
        print("https://Freedash.io skipped for bot cool down")
        if dash_skip > 2:
            dash_skip = 0
            dash_bot = 0
            print("Final cool down for https://Freedash.io")

####################################################################
    if nem_bot <= 2:
        try:
            print("Navigating to https://Freenem.com")
            browser.get("https://freenem.com/free")

            username = creds[13]
            password = creds[14]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                nem_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        nem_skip += 1
        print("https://Freenem.com skipped for bot cool down")
        if nem_skip > 2:
            nem_skip = 0
            nem_bot = 0
            print("Final cool down for https://Freenem.com")
####################################################################
    if ada_bot <= 2:
        try:
            print("Navigating to https://Freecardano.com")
            browser.get("https://freecardano.com/free")

            username = creds[17]
            password = creds[18]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                ada_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        ada_skip += 1
        print("https://Freecardano.com skipped for bot cool down")
        if ada_skip > 2:
            ada_skip = 0
            ada_bot = 0
            print("Final cool down for https://Freecardano.com")
####################################################################
    if xrp_bot <=2:
        try:
            print("Navigating to https://coinfaucet.io")
            browser.get("https://coinfaucet.io/free")

            username = creds[21]
            password = creds[22]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                xrp_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        xrp_skip += 1
        print("https://coinfaucet.io skipped for bot cool down")
        if xrp_skip > 2:
            xrp_skip = 0
            xrp_bot = 0
            print("Final cool down for https://coinfaucet.io")
####################################################################
    if btc_bot <= 2:
        try:
            print("Navigating to https://Freebitcoin.io")
            browser.get("https://freebitcoin.io/free")

            username = creds[25]
            password = creds[26]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                btc_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        btc_skip += 1
        print("https://Freebitcoin.io skipped for bot cooldown")
        if btc_skip > 2:
            btc_skip = 0
            btc_bot = 0
            print("Final cooldown for https://Freebitcoin.io")
####################################################################
    if steam_bot <=2:
        try:
            print("Navigating to https://Freesteam.io")
            browser.get("https://freesteam.io/free")

            username = creds[29]
            password = creds[30]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                steam_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        steam_skip += 1
        print("https://Freesteam.io skipped for bot cooldown")
        if steam_skip > 2:
            steam_skip = 0
            steam_bot = 0
            print("Final cooldown for https://Freesteam.io")
####################################################################
    if usdc_bot <= 2:
        try:
            print("Navigating to https://freeusdcoin.com/")
            browser.get("https://freeusdcoin.com/free")

            username = creds[33]
            password = creds[34]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                usdc_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        usdc_skip += 1
        print("https://freeusdcoin.com/ skipped for bot cooldown")
        if usdc_skip > 2:
            usdc_skip = 0
            usdc_bot = 0
            print("Final cooldown for https://freeusdcoin.com/")
####################################################################
    if link_bot <= 2:
        try:
            print("Navigating to https://Freechainlink.io")
            browser.get("https://freechainlink.io/free")

            username = creds[37]
            password = creds[38]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                link_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        link_skip += 1
        print("https://Freechainlink.io skipped for bot cooldown")
        if link_skip > 2:
            link_skip = 0
            link_bot = 0
            print("Final cooldown for https://Freechainlink.io")
####################################################################
    if tron_bot <= 2:
        try:
            print("Navigating to https://Free-tron.com")
            browser.get("https://free-tron.com/free")

            username = creds[41]
            password = creds[42]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                tron_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        tron_skip += 1
        print("https://Free-tron.com skipped for bot cooldown")
        if tron_skip > 2:
            tron_skip = 0
            tron_bot = 0
            print("Final cooldown for https://Free-tron.com")
####################################################################
    if bnc_bot <= 2:
        try:
            print("Navigating to https://Freebinancecoin.com")
            browser.get("https://freebinancecoin.com/free")

            username = creds[45]
            password = creds[46]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                bnb_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        bnb_skip += 1
        print("https://Freebinancecoin.com skipped for bot cooldown")
        if bnb_skip > 2:
            bnb_skip = 0
            bnb_bot = 0
            print("Final cooldown for https://Freebinancecoin.com")
####################################################################
    if neo_bot <= 2:
        try:
            print("Navigating to https://Freeneo.io")
            browser.get("https://freeneo.io/free")

            username = creds[49]
            password = creds[50]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                neo_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        neo_skip += 1
        print("https://Freeneo.io skipped for bot cooldown")
        if neo_skip > 2:
            neo_skip = 0
            neo_bot = 0
            print("Final cooldown for https://Freeneo.io")
####################################################################
    if ltc_bot <= 2:
        try:
            print("Navigating to https://Free-ltc.com")
            browser.get("https://free-ltc.com/free")

            username = creds[53]
            password = creds[54]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                ltc_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        ltc_skip += 1
        print("https://Free-ltc.com skipped for bot cooldown")
        if ltc_skip > 2:
            ltc_skip = 0
            ltc_bot = 0
            print("Final cooldown for https://Free-ltc.com")
####################################################################
    if eth_bot <= 2:
        try:
            print("Navigating to https://freeethereum.com/")
            browser.get("https://freeethereum.com/free")

            username = creds[57]
            password = creds[58]

            login()

            very_human = randrange(60)
            # time.sleep(very_human)
            timer += very_human

            for remaining in range(very_human, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Waiting {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking for Roll Button            \n")

            try:
                roll_button = browser.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                roll_button.click()
                print("Clicked roll button")
            except ElementNotInteractableException:
                print("No roll button found")
            time.sleep(10)
            try:
                WebDriverWait(browser, 4).until(expected_conditions.alert_is_present())

                alert = browser.switch_to.alert
                alert.accept()
                print("Found bot alert, refreshing page")
                browser.refresh()
                bot_attempt += 1
                eth_bot += 1
                if bot_attempt > 10:
                    bot_attempt = 0
                    print("Bot check loop detected")
                    print("Seriously, who makes bot detection like this?")
                    browser.close()
                    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
                    browser.maximize_window()
            except TimeoutException:
                print("No alerts found")
        except:
            print("Error encountered on page")
            browser.close()
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
            browser.maximize_window()
    else:
        eth_skip += 1
        print("https://freeethereum.com/ skipped for bot cooldown")
        if eth_skip > 2:
            eth_skip = 0
            eth_bot = 0
            print("Final cooldown for https://freeethereum.com/")
####################################################################

    browser.close()

    print("All sites collected")
    total_timer = 3500 - timer
    print("Waiting for countdown: " + str(total_timer))
    for remaining in range(total_timer, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rComplete!            \n")
    timer = 0

    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
    browser.maximize_window()


