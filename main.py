from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

# Getting detais from config file
f = open('config.json', )
user_config = json.load(f)


def summon_chrome_window(user_answer, url):
    driver.get(url)
    if user_answer == 1:
        print(user_config(["xpaths"]))
        # password_xpath = user_config(["xpaths"]["facebook_xpath"]["fb_xpath_array"][1])
        # search = driver.find_element_by_xpath(username_xpath)
        # search.send_keys(user_config["facebook_login"][0])
        # search = driver.find_element_by_xpath(password_xpath)
        # search.send_keys(user_config["facebook_login"][1])
#
#     if user_answer == 2:
#         username_xpath = user_config(["xpaths"]["instagram_xpath"]["instagram_xpath_array"][0])
#         password_xpath = user_config(["xpaths"]["instagram_xpath"]["instagram_xpath_array"][1])
#     if user_answer == 3:
#         username_xpath = user_config(["xpaths"]["reddit_xpath"]["reddit_xpath_array"][0])
#         username_xpath = user_config(["xpaths"]["reddit_xpath"]["reddit_xpath_array"][1])



if __name__ == "__main__":
    lobby_answer = input("Facebook, Type 1" + "\n" + "Instagram, Type 2" + "\n" + "Reddit, Type 3")
    requested_url = ''
    if lobby_answer == 1:
        requested_url = "https://www.facebook.com/login/"
    if lobby_answer == 2:
        requested_url = "https://www.instagram.com/accounts/login/"
    if lobby_answer == 3:
        requested_url = "https://www.reddit.com/login/"

    #Setting up web driver
    PATH = user_config["chrome_driver_path"]
    driver = webdriver.Chrome(PATH)

    summon_chrome_window(lobby_answer, requested_url)

# def facebook_login(requested_url):
#     driver.get(requested_url)
#     fb_username_xpath = '//*[@id="email"]'
#     fb_password_xpath = '//*[@id="pass"]'
#     search = driver.find_element_by_xpath(fb_username_xpath)
#     search.send_keys('***@gmai.com')
#     search.send_keys(Keys.RETURN)