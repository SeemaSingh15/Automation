import sys
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
text=""
name = "seema"
number = "+91 9010443691"
message="ohkjh"
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
if (text=="Invite to WhatsApp"):
    el11 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/inviteNewContactList")
    el11.click()
    driver2.implicitly_wait(5)
    el22 = driver2.find_element(by=AppiumBy.ID, value="com.samsung.android.messaging:id/attachsheet")
    el22.click()
else :
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



