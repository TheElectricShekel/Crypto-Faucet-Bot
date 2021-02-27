from selenium import webdriver
from PIL import Image
from io import BytesIO
import time
import pytesseract
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pyperclip
import keyboard
from random import randrange
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
credentials = "creds.txt"

driver_path = "chromedriver.exe"
brave_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

with open(credentials) as f:
    creds = f.readlines()
time.sleep(1)

option = webdriver.ChromeOptions()
option.binary_location = brave_path
#option.add_argument("--incognito")
#option.add_argument("--headless")

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser.maximize_window()
print("Browser launched")

username = creds[9]
password = creds[10]

browser.get("https://cointiply.com/login")
print("Navigate: Cointiply login page")

login_field = browser.find_element_by_css_selector("input[type='text']")
login_field.send_keys(username)
print("Entered Username")

pw_field = browser.find_element_by_css_selector("input[type='password']")
pw_field.send_keys(password)
print("Entered Password")

print("Waiting for Captcha...")
time.sleep(10)


captcha = browser.find_element_by_id("adcopy-outer").screenshot("captcha.png")
print("Solving Captcha...")
img = Image.open("captcha.png")
width, height = img.size
img_res = img.crop((0, 130, width, height))
img_res.save("captcha.png")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

captcha_string = pytesseract.image_to_string("captcha.png")
s = captcha_string
sliced_captcha = s[14:]
print(sliced_captcha)

pyperclip.copy(sliced_captcha)

captcha_field = browser.find_element_by_css_selector("input[type='text'][name='adcopy_response'][class='md-input']")

captcha_field.click()
time.sleep(1)

captcha_field.send_keys(sliced_captcha)
#keyboard.send("ctrl+v")
print("Captcha Solved")

time.sleep(2)

#browser.find_element_by_css_selector("button[type='button'][class='md-button md-raised md-accent font-weight-600 md-theme-default']").click
pw_field.click()
keyboard.send("enter")

######################################################

time.sleep(5)

browser.get("https://cointiply.com/home?intent=faucet")
print("Navigating to Faucet")

time.sleep(3)

try:
    print("Joining Rain Pool...")
    chat_button = browser.find_element_by_xpath(
        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
    chat_button.click()

    time.sleep(5)

    rain_button = browser.find_element_by_xpath(
        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
    rain_button.click()
    time.sleep(2)
    tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
    tos_button.click()
    print("Rain Pool successfully joined")
except:
    print("Error joining Rain Pool - already joined")

time.sleep(1)

#roll_button = browser.find_element_by_class_name("md-ink-ripple").click()
try:
    roll_button = browser.find_element_by_xpath("/html/body/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
    roll_button.click()
    print("Clicked Roll Button")

    print("Waiting for Captcha...")
    time.sleep(11)

    captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
    print("Solving Captcha #2...")
    img2 = Image.open("captcha2.png")
    width, height = img2.size
    img_res2 = img2.crop((0, 130, width, height))
    img_res2.save("captcha2.png")

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    captcha_string2 = pytesseract.image_to_string("captcha2.png")
    s = captcha_string2
    sliced_captcha2 = s[14:]
    print(sliced_captcha2)

    pyperclip.copy(sliced_captcha2)

    captcha_field2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")

    captcha_field2.click()
    time.sleep(2)

    captcha_field2.send_keys(sliced_captcha2)
    #keyboard.send("ctrl+v")
    print("Captcha Solved")

    time.sleep(2)

    final_roll = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
    final_roll.click()
    time.sleep(2)
    print("Clicked Roll Button")
except:
    print("Countdown timer active")

while True:
    print("Waiting for countdown...")
    very_human = randrange(180)
    roll_wait = 3600
    #total_wait = roll_wait + very_human
    rain_differential = roll_wait // 10
    rain_check = 0
    while rain_check <= 9:
        for remaining in range(rain_differential, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("Checking Rain Pool in {:2d} seconds.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

        sys.stdout.write("\rChecking Rain Pool...            \n")

        try:
            print("Joining Rain Pool...")
            #try:
            #    chat_button = browser.find_element_by_xpath(
            #        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
            #    chat_button.click()
            #    print("Joined Chat")
            #except:
            #    print("Chat already joined")

            #time.sleep(5)

            rain_button = browser.find_element_by_xpath("/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
            rain_button.click()
            time.sleep(2)
            tos_button = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/button[2]")
            tos_button.click()
            print("Rain Pool successfully joined")

        except:
            print("Error joining Rain Pool - already joined")

        rain_check += 1

    print("Roll Timer complete!")

    for remaining in range(very_human, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("Randomizing wait time: {:2d} seconds remaining".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rRandomized wait time complete!            \n")

    #countdown = roll_wait + very_human
    #time.sleep(roll_wait + very_human)

    #browser.refresh()
    browser.get("https://cointiply.com/home?intent=faucet")
    time.sleep(3)

    try:
        print("Joining Rain Pool...")
        chat_button = browser.find_element_by_xpath(
            "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
        chat_button.click()

        time.sleep(5)

        rain_button = browser.find_element_by_xpath(
            "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
        rain_button.click()
        time.sleep(2)
        tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
        tos_button.click()
        print("Rain Pool successfully joined")
    except:
        print("Error joining Rain Pool - already joined")

    time.sleep(1)

    roll_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
    roll_button.click()
    print("Clicked Roll Button")

    print("Waiting for Captcha...")
    time.sleep(10)

    captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
    print("Solving Captcha #2...")
    img2 = Image.open("captcha2.png")
    width, height = img2.size
    img_res2 = img2.crop((0, 130, width, height))
    img_res2.save("captcha2.png")

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    captcha_string2 = pytesseract.image_to_string("captcha2.png")
    s = captcha_string2
    sliced_captcha2 = s[14:]
    print(sliced_captcha2)

    pyperclip.copy(sliced_captcha2)

    captcha_field2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")
    captcha_field2.click()
    time.sleep(2)
    captcha_field2.send_keys(sliced_captcha2)
    #keyboard.send("ctrl+v")
    print("Captcha Solved")

    time.sleep(1)

    final_roll = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
    final_roll.click()
    print("Clicked Roll Button")

    time.sleep(5)

    try:
        print("Wrong Answer Check...")
        error = browser.find_element_by_xpath("//*[contains(text(), 'wrong answer')]").is_displayed()
        #error2 = browser.find_element_by_xpath("//*[contains(text(), 'puzzle expired')]").is_displayed()
        if error == True: #or error2 == True:
            print("Captcha Failed - Wrong Answer")
            print("Retrying in 15 min.")
            #time.sleep(900)
            for remaining in range(900, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\rComplete!            \n")
            #refresh = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/button")
            #refresh.click()
            #browser.refresh
            #time.sleep(12)
            browser.get("https://cointiply.com/home?intent=faucet")

            time.sleep(3)

            try:
                print("Joining Rain Pool...")
                chat_button = browser.find_element_by_xpath(
                    "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
                chat_button.click()

                time.sleep(5)

                rain_button = browser.find_element_by_xpath(
                    "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
                rain_button.click()
                time.sleep(2)
                tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
                tos_button.click()
                print("Rain Pool successfully joined")
            except:
                print("Error joining Rain Pool - already joined")

            time.sleep(1)

            # roll_button = browser.find_element_by_class_name("md-ink-ripple").click()
            roll_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
            roll_button.click()
            print("Clicked Roll Button")

            print("Waiting for Captcha...")
            time.sleep(11)

            captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
            print("Solving Captcha #2...")
            img2 = Image.open("captcha2.png")
            width, height = img2.size
            img_res2 = img2.crop((0, 130, width, height))
            img_res2.save("captcha2.png")

            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

            captcha_string2 = pytesseract.image_to_string("captcha2.png")
            s = captcha_string2
            sliced_captcha2 = s[14:]
            print(sliced_captcha2)

            pyperclip.copy(sliced_captcha2)

            captcha_field2 = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")

            captcha_field2.click()
            time.sleep(2)

            captcha_field2.send_keys(sliced_captcha2)
            #keyboard.send("ctrl+v")
            print("Captcha Solved")

            time.sleep(2)

            final_roll = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
            final_roll.click()
            time.sleep(2)
            print("Clicked Roll Button")
    except NoSuchElementException:
        print("Wrong Answer check passed")


    try:
        print("Invalid Captcha Check...")
        #error = browser.find_element_by_xpath("//*[contains(text(), 'wrong answer')]").is_displayed()
        error2 = browser.find_element_by_xpath("//*[contains(text(), 'Invalid captcha response')]").is_displayed()
        if error2 == True: #or error2 == True:
            print("Captcha Failed - Invalid captcha response")
            print("Retrying in 15 min.")
            #time.sleep(900)
            for remaining in range(900, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\rComplete!            \n")
            #refresh = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/button")
            #refresh.click()
            #time.sleep(12)
            #browser.refresh()
            browser.get("https://cointiply.com/home?intent=faucet")

            time.sleep(3)

            try:
                print("Joining Rain Pool...")
                chat_button = browser.find_element_by_xpath(
                    "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
                chat_button.click()

                time.sleep(5)

                rain_button = browser.find_element_by_xpath(
                    "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
                rain_button.click()
                time.sleep(2)
                tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
                tos_button.click()
                print("Rain Pool successfully joined")
            except:
                print("Error joining Rain Pool - already joined")

            time.sleep(1)

            # roll_button = browser.find_element_by_class_name("md-ink-ripple").click()
            roll_button = browser.find_element_by_xpath(
                "/html/body/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
            roll_button.click()
            print("Clicked Roll Button")

            print("Waiting for Captcha...")
            time.sleep(11)

            captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
            print("Solving Captcha #2...")
            img2 = Image.open("captcha2.png")
            width, height = img2.size
            img_res2 = img2.crop((0, 130, width, height))
            img_res2.save("captcha2.png")

            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

            captcha_string2 = pytesseract.image_to_string("captcha2.png")
            s = captcha_string2
            sliced_captcha2 = s[14:]
            print(sliced_captcha2)

            pyperclip.copy(sliced_captcha2)

            captcha_field2 = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")

            captcha_field2.click()
            time.sleep(2)

            captcha_field2.send_keys(sliced_captcha2)
            #keyboard.send("ctrl+v")
            print("Captcha Solved")

            time.sleep(2)

            final_roll = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
            final_roll.click()
            time.sleep(2)
            print("Clicked Roll Button")
    except NoSuchElementException:
        print("Invalid Captcha Check Passed")

    try:
        print("Puzzle Expired Check...")
        #error = browser.find_element_by_xpath("//*[contains(text(), 'wrong answer')]").is_displayed()
        error2 = browser.find_element_by_xpath("//*[contains(text(), 'puzzle expired')]").is_displayed()
        if error2 == True: #or error2 == True:
            print("Captcha Failed - Puzzle Expired")
            print("Retrying in 15 min.")
            #time.sleep(900)
            for remaining in range(900, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\rComplete!            \n")
            #refresh = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/button")
            #refresh.click()
            #time.sleep(12)
            #browser.refresh()
            browser.get("https://cointiply.com/home?intent=faucet")

            time.sleep(3)

            try:
                print("Joining Rain Pool...")
                chat_button = browser.find_element_by_xpath(
                    "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
                chat_button.click()

                time.sleep(5)

                rain_button = browser.find_element_by_xpath(
                    "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
                rain_button.click()
                time.sleep(2)
                tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
                tos_button.click()
                print("Rain Pool successfully joined")
            except:
                print("Error joining Rain Pool - already joined")

            time.sleep(1)

            # roll_button = browser.find_element_by_class_name("md-ink-ripple").click()
            roll_button = browser.find_element_by_xpath(
                "/html/body/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
            roll_button.click()
            print("Clicked Roll Button")

            print("Waiting for Captcha...")
            time.sleep(11)

            captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
            print("Solving Captcha #2...")
            img2 = Image.open("captcha2.png")
            width, height = img2.size
            img_res2 = img2.crop((0, 130, width, height))
            img_res2.save("captcha2.png")

            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

            captcha_string2 = pytesseract.image_to_string("captcha2.png")
            s = captcha_string2
            sliced_captcha2 = s[14:]
            print(sliced_captcha2)

            pyperclip.copy(sliced_captcha2)

            captcha_field2 = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")

            captcha_field2.click()
            time.sleep(2)

            captcha_field2.send_keys(sliced_captcha2)
            #keyboard.send("ctrl+v")
            print("Captcha Solved")

            time.sleep(2)

            final_roll = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
            final_roll.click()
            time.sleep(2)
            print("Clicked Roll Button")
    except NoSuchElementException:
        print("Puzzle Expired Check Passed")



