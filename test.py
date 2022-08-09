from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


class browser():

    def browser(self):
        # Provide the path of firefox present on your system.
        fp = webdriver.FirefoxProfile(profile_directory='/home/jf/.mozilla/firefox/6pgja4fq.default-release')
        # Run Firefox
        browser = webdriver.Firefox(fp)

    def hi(self):
        print('hi')

test = browser()
test.browser()