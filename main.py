from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json


# Getting detais from config file
f = open('config.json', )
user_config = json.load(f)

# Establishing the driver
PATH = 'C:\webdrivers\chromedriver.exe'
# driver = webdriver.Chrome(PATH)




def get_website_url(userAnswer):
    if userAnswer == 1:
        requested_url = "https://www.facebook.com/login/"
    if userAnswer == 2:
        requested_url = "https://twitter.com/login"
    if userAnswer == 3:
        requested_url = "https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F"
    return requested_url


# def facebook_login(requested_url):
#     driver.get(requested_url)
#     fb_username_xpath = '//*[@id="email"]'
#     fb_password_xpath = '//*[@id="pass"]'
#     search = driver.find_element_by_xpath(fb_username_xpath)
#     search.send_keys('***@gmai.com')
#     search.send_keys(Keys.RETURN)

if __name__ == "__main__":
    print(type(user_config['facebook_login']))


# answer = get_website_url(1)
# facebook_login(answer)
