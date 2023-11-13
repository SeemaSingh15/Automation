import pandas as pd
import sys
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#file="C:/Users/seema/OneDrive/Documents/contacts.xlsx"
#df = pd.read_excel(file
def whatsapp(df):
    file = "C:/Users/seema/OneDrive/Documents/contacts.xlsx"
    df = pd.read_excel(file)
    for index, row in df.iterrows():
        #name = row["name"]
        number = row["number"]
        message = row["message"]
        desired_cap = {
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:deviceName": "RZ8RC1F7A3W",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": " com.whatsapp",
        "appium:appActivity": "com.whatsapp.HomeActivity",
        "appium:noReset": "true",
        "appium:appWaitForLaunch": "false",
        "newCommandTimeout": 3000,
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        driver.implicitly_wait(5)
        el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WhatsApp")
        el11.click()
        driver.implicitly_wait(5)
        el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="New chat")
        el12.click()
        driver.implicitly_wait(5)
        el13 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el13.click()
        driver.implicitly_wait(5)
        el14 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/search_src_text")
        el14.click()
        driver.implicitly_wait(5)
        el14.send_keys(number)
        el15 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView")
        el15.click()
        driver.implicitly_wait(5)
        el16 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/entry")
        el16.click()
        driver.implicitly_wait(5)
        el16.send_keys(message)
        el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Send")
        el17.click()
        print("saved")
if __name__ == '_main_'  :
    file = "C:/Users/seema/Desktop/list.xlsx"

    df = pd.read_excel()

    for index, row in df.iterrows():
        name = row["name"]
        number = row["number"]
        message = row["message"]
        whatsapp(number,message)


