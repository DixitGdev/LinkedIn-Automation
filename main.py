import time

from appium import webdriver
from Functions import *
from threading import Thread
from sheet_mgmt import *
import os

desired_cap_Linkedin = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "com.linkedin.android",
    "noReset": 'true',
    "appActivity": "com.linkedin.android.authenticator.LaunchActivity",
    "automationName": "UiAutomator2",
    "fullReset": 'false',
    "newCommandTimeout": "50000",
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap_Linkedin)

# DEFAULT PARAMETERS
default_max_follow_per_day = h.read_json('./config.json')["default_max_follow_per_day"]
default_delay = h.read_json('./config.json')["default_delay"]                 # SECONDS
default_message_for_AI_bot = h.read_json('./config.json')["default_message_for_AI_bot"]





