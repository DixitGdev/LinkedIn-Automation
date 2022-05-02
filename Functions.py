from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException, \
    StaleElementReferenceException, InvalidElementStateException
from helper import *
import random

h = Helper()

inv_list = [
    "Hello I am CBD manufacturer based in California, USA. I can provide the quickest selling products for your shelf. Add me to your list.",
    "Hi, I would like to share with you our list products in CBD. You will find amazing quality and prices. Accept my Invitation?",
    "We are producer of CBD/THCO/HHC/HHCO products. Add me for more detail.",
    "I would like to give you our best offer in the CBD market. We offer best product quality and services in California, USA. Connect soon.",
    "If you are looking for next hottest product to sell for CBD relating product. I can explain more.",
    "I have what it takes to succeed in the CBD Market, and I can share it with you. Accept Please.",
    "We are the best manufacturer of CBD products you can source from. Connect with me.",
    "CBD products are projected to be big sales in the next few years. Can I explain how you can sell in this market? Get in touch soon."
]


def click_continue(driver):
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.Button[@text="Continue"]')))
    continue_button.click()


def click_remember_me(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.CheckBox[@text="Remember me."]')))
    cb.click()


def click_messaging_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.Button[@resource-id="com.linkedin.android:id/home_messaging"]')))
    cb.click()


def click_profile_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.ImageView[@content-desc="My Profile and Communities"]')))
    cb.click()


def click_setting_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.Button[@text="Settings"]')))
    cb.click()


def click_send_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.Button[@text="Send"]')))
    cb.click()


def click_sign_out_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@text="Sign out"]')))
    cb.click()
    try:
        remember = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//android.widget.TextView[@text="No, don’t remember and sign out"]')))
        remember.click()
    except(NoSuchElementException, TimeoutException):
        pass


def click_close_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.ImageView[@content-desc="Cancel"]')))
    cb.click()


def click_search_bar(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.Button[@resource-id="com.linkedin.android:id/search_bar"]')))
    cb.click()


def click_and_inside_search_bar(driver, search_word):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.EditText[@resource-id="com.linkedin.android:id/search_bar_edit_text"]')))
    cb.send_keys(search_word)


def click_filter_by_people(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.Button[@content-desc="Filter by People"]')))
    cb.click()


def click_filter_by_location(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.Button[@content-desc="Filter by Locations"]')))
    cb.click()


def click_add_location_filter(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.Button[@content-desc="Add a location, Search field"]')))
    cb.click()


def click_connect_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.ImageButton[@content-desc="Connect"]')))
    cb.click()


def click_blue_connect_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.Button[@text="Connect"]')))
    cb.click()


def click_auto_location_type(driver, location):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.MultiAutoCompleteTextView[@index="0"]')))
    cb.click()
    time.sleep(1)
    cb.send_keys(location)


def click_first_search_result(driver):
    time.sleep(2)
    locations = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, f'//android.widget.TextView[@index="0"]')))
    locations[0].click()
    time.sleep(1)


def click_more_option_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.ImageButton[@content-desc="More options"]')))
    cb.click()


def click_back_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.ImageButton[@content-desc="Back"]')))
    cb.click()


def click_unread_filter_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             f'//android.widget.CompoundButton[@resource-id="com.linkedin.android:id/filter_unread_lever_btn"]')))
    cb.click()


def click_all_filter_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             f'//android.widget.CompoundButton[@resource-id="com.linkedin.android:id/filter_nofilter_lever_btn"]')))
    cb.click()


def click_message_filter_button(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.Button[@content-desc="Filter messages"]')))
    cb.click()


def click_personalize_invite(driver):
    time.sleep(2)
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.TextView[@text="Personalize invite"]')))
    cb.click()


def type_personalized_message(driver, msg):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        f'//android.widget.EditText[@resource-id="com.linkedin.android:id/mynetwork_custom_invitation_message"]')))
    driver.find_element(by=By.XPATH,
                        value=f'//android.widget.EditText[@resource-id="com.linkedin.android:id/mynetwork_custom_invitation_message"]').send_keys(
        msg)


def type_login_email(email, driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.EditText[@text="Email or Phone"]')))
    driver.find_element(by=By.XPATH, value=f'//android.widget.EditText[@text="Email or Phone"]').send_keys(email)


def type_login_password(password, driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.EditText[@text="Password"]')))
    driver.find_element(by=By.XPATH, value=f'//android.widget.EditText[@text="Password"]').send_keys(password)


def check_login_otp(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//android.widget.Button[@text="Submit pin"]')))
        return True
    except (NoSuchElementException, TimeoutException):
        return False


def go_home(driver):
    time.sleep(1)
    driver.start_activity('com.linkedin.android', 'com.linkedin.android.authenticator.LaunchActivity')


def go_setting(driver):
    time.sleep(1)
    driver.start_activity('com.linkedin.android', 'com.linkedin.android.settings.ui.SettingsActivity')


def go_login_screen(driver):
    time.sleep(1)
    driver.start_activity('com.linkedin.android', 'com.linkedin.android.infra.navigation.MainActivity')


def press_seach_key(driver):
    driver.press_keycode(66)


def swipe(driver):
    driver.swipe(500, 1600, 500, 200, 900)
    driver.swipe(500, 1600, 500, 200, 900)


def swipe_one_time(driver):
    time.sleep(1)
    driver.swipe(500, 1600, 500, 900, 1100)


def swipe_one_time_up(driver):
    time.sleep(1)
    driver.swipe(500, 1600, 500, 1700, 300)


def login(email, password, driver):
    check_activity(driver)
    type_login_email(email, driver)
    type_login_password(password, driver)
    click_remember_me(driver)
    click_continue(driver)
    if check_login_otp(driver):
        print("NEED TO ENTER OTP")
        open_vpn_one_time(driver)
        return False
    else:
        return True


def logout(driver):
    go_setting(driver)
    swipe(driver)
    click_sign_out_button(driver)
    time.sleep(0.5)
    driver.close_app()


def check_activity(driver):
    google_Ac = ".auth.api.credentials.assistedsignin.ui.AssistedSignInActivity"
    time.sleep(6)
    activity = driver.current_activity;
    if activity == google_Ac:
        click_close_button(driver)
        return True


def is_emulator_is_ready(driver):
    home_ac = ".infra.navigation.MainActivity"
    time.sleep(1)
    activity = driver.current_activity;
    if activity == home_ac:
        return True
    elif check_activity(driver):
        return True
    else:
        return False


def open_vpn(driver):
    driver.start_activity('com.windscribe.vpn', 'com.windscribe.mobile.windscribe.WindscribeActivity')
    time.sleep(3)
    driver.start_activity('com.windscribe.vpn', 'com.windscribe.mobile.windscribe.WindscribeActivity')


def open_vpn_one_time(driver):
    driver.start_activity('com.windscribe.vpn', 'com.windscribe.mobile.windscribe.WindscribeActivity')


def open_linkedin(driver):
    time.sleep(4)
    driver.launch_app()


def turn_on_vpn_switch(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.ImageView[@resource-id="com.windscribe.vpn:id/on_off_button"]')))
    cb.click()
    time.sleep(3)
    print("VPN ON...")
    open_linkedin(driver)
    print("Switched to Linkedin")


def search_process(driver, search_word, location):
    time.sleep(2)
    click_search_bar(driver)
    click_and_inside_search_bar(driver, search_word)
    press_seach_key(driver)
    click_filter_by_people(driver)
    click_filter_by_location(driver)
    click_add_location_filter(driver)
    click_auto_location_type(driver, location)
    click_first_search_result(driver)
    driver.back()


def refresh_research(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.TextView[@resource-id="com.linkedin.android:id/search_bar_text_view"]')))
    cb.click()
    time.sleep(1.5)
    press_seach_key(driver)
    time.sleep(2)


def send_invitation_message_from_profile(driver, msg):
    click_more_option_button(driver)
    click_personalize_invite(driver)
    type_personalized_message(driver, msg)
    time.sleep(0.5)
    click_send_button(driver)
    time.sleep(2.5)
    click_back_button(driver)
    time.sleep(1)
    click_back_button(driver)
    time.sleep(1)
    refresh_research(driver)


def start_connect(driver, max_connects, delay):
    connects = 0
    while connects < max_connects:
        for index in range(1, 5):
            try:
                main_banner = WebDriverWait(driver, 4).until(
                    EC.presence_of_element_located((By.XPATH, f'//android.view.ViewGroup[@index="{index}"]')))
                main_banner.find_element(By.XPATH,
                                         value='//android.widget.ImageButton[@resource-id="com.linkedin.android:id/search_result_primary_action_icon_tertiary"]')
                main_banner.find_element(By.XPATH, value='//android.widget.ImageButton[@content-desc="Connect"]')
                print(index)
                main_banner.find_element(By.XPATH,
                                         value='//android.widget.TextView[@resource-id="com.linkedin.android:id/search_entity_result_title"]').click()
                msg = random.choice(inv_list)
                send_invitation_message_from_profile(driver, msg)
                connects += 1
                time.sleep(delay)
            except (
                    TimeoutException, NoSuchElementException, StaleElementReferenceException,
                    InvalidElementStateException):
                pass
        swipe_one_time(driver)


def handle_messaging(driver):
    swipe_one_time_up(driver)
    click_messaging_button(driver)
    click_message_filter_button(driver)
    send_msg_to_unread_messages(driver)


def click_notifications_bottom_icon(driver):
    cb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//android.widget.TextView[@text="Notifications"]')))
    cb.click()


def check_accepted_invitations(driver, msg):
    click_notifications_bottom_icon(driver)
    count = 0
    for i in range(1, 5):
        for index in range(1, 5):
            try:
                main_banner = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, f'//android.widget.Button[@index="{index}"]')))
                title = main_banner.find_element(By.XPATH,
                                                 value="//android.widget.TextView[contains(@text, 'accepted your invitation to connect.')]")
                name = title.text.replace("accepted your invitation to connect.", "")
                print(name)
                namelist = h.read_json("name.json")
                if name in namelist:
                    print(f"Already msg sent to {name}")
                else:
                    h.append_to_json("name.json", name)
                    main_banner.find_element(By.XPATH, value='//android.widget.Button[@text="Message"]').click()
                    send_message(driver, msg)
                    time.sleep(1)
                    click_back_button(driver)
                    count += 1
            except (
                    TimeoutException, NoSuchElementException, StaleElementReferenceException,
                    InvalidElementStateException):
                pass
        swipe_one_time(driver)


def send_msg_to_unread_messages(driver):
    while True:
        time.sleep(1)
        try:
            click_unread_filter_button(driver)
            all_unread_convs = WebDriverWait(driver, 4).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                                   f'//android.view.ViewGroup[@resource-id="com.linkedin.android:id/messaging_conversation_list_item_container"]')))
            all_unread_convs[0].click()
            all_msgs = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                           f'//android.widget.TextView[@resource-id="com.linkedin.android:id/body"]')))
            bot_response = h.read_json('./config.json')["Message for responder"]
            send_message(driver, bot_response)
            time.sleep(1)
            click_back_button(driver)
            click_all_filter_button(driver)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
            break


def send_message(driver, msg):
    ip = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.EditText[@text="Write a message…"]')))
    ip.send_keys(msg)
    sb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.Button[@content-desc="Send"]')))
    sb.click()
