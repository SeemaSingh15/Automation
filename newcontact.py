import pandas as pd
import sys
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

def send():
    pass
def contact(df):
    for index, row in df.iterrows():
        name = row["name"]
        number = row["number"]
        desired_cap1 = {
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:deviceName": "RZ8RC1F7A3W",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.samsung.android.dialer",
        "appium:appActivity": "com.samsung.android.dialer.DialtactsActivity",
        "appium:appWaitForLaunch": "false",
        "appium:noReset": "true"
        }
        driver1 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap1)
        driver1.implicitly_wait(10)
        el1 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.dialer:id/contactlist_tab_button")
        el1.click()
        driver1.implicitly_wait(10)
        element1 = driver1.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create new contact")
        driver1.implicitly_wait(5)
        element1.click()
        driver1.implicitly_wait(5)
        element2 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/nameEdit")
        driver1.implicitly_wait(5)
        element2.send_keys(name)
        element3 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/edit_fields_container")
        driver1.implicitly_wait(5)
        element3.click()
        driver1.implicitly_wait(5)
    # element3.send_keys(number)
        element4 = driver1.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.EditText")
        driver1.implicitly_wait(5)
        element4.send_keys(number)
        driver1.implicitly_wait(5)
        element5 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/menu_done")
        element5.click()
        driver1.implicitly_wait(5)
        element6 = driver1.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
        element6.click()

        print("saving of " + name + " completed")
        driver1.quit()

def whatsapp(df):
    for index, row in df.iterrows():
        name = row["name"]
        number = row["number"]
        message = row["message"]
        desired_cap2 = {
                "platformName": "Android",
                "appium:platformVersion": "13",
                "appium:deviceName": "RZ8RC1F7A3W",
                "appium:automationName": "UiAutomator2",
                "appium:appPackage": "com.whatsapp",
                "appium:appActivity":"com.whatsapp.HomeActivity",
                "appium:appWaitForLaunch": "false",
                "appium:noReset": "true"
            }
        driver2 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap2)
        driver2.implicitly_wait(5)
        el1 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WhatsApp")
        el1.click()
        driver2.implicitly_wait(5)
        el2 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="New chat")
        el2.click()
        driver2.implicitly_wait(5)
        el3 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el3.click()
        driver2.implicitly_wait(5)
        el5 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/search_src_text")
        el5.click()
        driver2.implicitly_wait(5)
        el5.send_keys(number)
        driver2.implicitly_wait(5)
        el6 = driver2.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView")
        el6.click()
        driver2.implicitly_wait(5)
        el7 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/entry")
        el7.click()
        driver2.implicitly_wait(5)
        el8 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/entry")
        el8.send_keys(message)
        driver2.implicitly_wait(5)
        el9 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Send")
        el9.click()
        driver2.quit()



