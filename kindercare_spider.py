# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.mobileby import MobileBy
import time



caps = {}
caps["appium:deviceName"] = "Samsung_Galaxy_S10"
caps["appium:platformName"] = "Android"
caps["appium:platformVersion"] = "10"
caps["appium:automationName"] = "UiAutomator2"
caps["appium:appActivity"] = "com.himama.educator.MainActivity"
caps["appium:appPackage"] = "com.kindercare.classroom"
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)






time.sleep(30) # wait for login

# Following a few lines of code is to automatically login to kindercare app
# However, initial testing shows it is not very robust. Now I am logging in
# during 30 seconds wait 

# Find the username text box by resource ID and fill in the content
#element = driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='username']")
#element.send_keys('username')

# Find the password text box by resource ID and fill in the content
#element = driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='password']")
#element.send_keys('password')

#button_elements = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
#button_elements[2].click()



# The following code snippet demonstrates how to scoll down the feed app
# Currently tested to be working quite robustly. However it will become very slow after 
# one hour or so

screen_size = driver.get_window_size()
start_x = int(1)
start_y = int(screen_size['height'] * 0.3)  # Start from 80% of the screen height
end_y = int(screen_size['height'] * 0.1)  # End at 20% of the screen height

while True:
    # Perform the swipe action to scroll down

    driver.swipe(start_x, start_y, start_x, end_y, 200)  # Adjust the duration as needed
    time.sleep(0.2)

    more_buttons = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.View[@class='android.view.View' and @text='More']")
    print(len(more_buttons))
    for b in reversed(more_buttons):
        if b.rect["height"]>10:
            b.click()
            time.sleep(0.5)
            break



# This line of code is used to find the picture and video thumbnails to click 
# We may also use height to identify whether certain thumbnail is currently in the view or not 

# elements = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.View[@class='android.view.View' and @text='javascript:;']")


# print(len(elements))

#driver.quit()


time.sleep(3600)