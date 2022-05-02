from appium import webdriver

from Functions import *
from sheet_mgmt import *

# DEFAULT PARAMETERS
default_max_follow_per_day = h.read_json('./config.json')["default_max_follow_per_day"]
default_delay = h.read_json('./config.json')["default_delay"]  # SECONDS
default_message_for_AI_bot = h.read_json('./config.json')["default_message_for_AI_bot"]

print("MESSAGING")

if __name__ == '__main__':
    data = read_data()
    for each in data:
        while True:
            try:
                email_from_sheet = each[5]
                password_from_sheet = each[6]
                instance_name = each[9]
                default_keyword = each[10]
                default_location = each[11]
                index = each[12]

                print("\n------------------------------------------------------------------\n")
                print(f"Instance : Instance_{instance_name}\n"
                      f"Email : {email_from_sheet}\n"
                      f"Password : {password_from_sheet}\n"
                      f"Account Index : {index}\n")

                time.sleep(2)
                os.popen(f"emulator -avd Instance_{instance_name}")

                desired_cap_Linkedin = {
                    "deviceName": f"Instance_{instance_name}",
                    "platformName": "Android",
                    "appPackage": "com.linkedin.android",
                    "noReset": 'true',
                    "appActivity": "com.linkedin.android.authenticator.LaunchActivity",
                    "automationName": "UiAutomator2",
                    "fullReset": 'false',
                    "newCommandTimeout": "50000",
                }

                print(f"Running....Instance_{instance_name}\n")
                time.sleep(25)
                driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap_Linkedin)

                if is_emulator_is_ready(driver):
                    driver.close_app()
                    open_vpn_one_time(driver)
                    check_activity(driver)
                    turn_on_vpn_switch(driver)

                    if login(email_from_sheet, password_from_sheet, driver):
                        check_accepted_invitations(driver, msg=default_message_for_AI_bot)
                        handle_messaging(driver)
                        logout(driver)
                        open_vpn_one_time(driver)
                        driver.close_app()
                        print(f"Task done in Instance_{instance_name}, Killing it...\n\n")
                        time.sleep(2)
                        os.popen("adb -e emu kill")
                    else:
                        open_vpn_one_time(driver)
                        driver.close_app()
                        print(f"Task done in Instance_{instance_name}, Killing it...\n\n")
                        time.sleep(2)
                        os.popen("adb -e emu kill")
                else:
                    print(f"Failed to ready Emulator,{instance_name}, Killing it...\n")
                    print(f"Cold boot emulator to fix this issue")
                    os.popen("adb -e emu kill")
                time.sleep(9)
                break
            except:
                print("Retry")
