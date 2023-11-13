import pandas as pd
import sys
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#file = "C:/Users/seema/OneDrive/Documents/contacts.xlsx"
#df = pd.read_excel(file)
def whatsapp(df):
        for index, row in df.iterrows():
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
                el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WhatsApp")
                el5.click()
                el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="New chat")
                el6.click()
                el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
                el7.click()
                el8 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/search_src_text")
                el8.click()
                el8.send_keys(number)
                el9 = driver.find_element(by=AppiumBy.XPATH,
                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView")
                el9.click()
                el10 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/entry")
                el10.click()
                el10.send_keys(message)
                el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Send")
                el11.click()

