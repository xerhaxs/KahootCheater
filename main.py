#    This is a KahootCheatBot expansion to https://github.com/RealNattawattHongthong/kahoot-cheat KahootCheater. It adds the ability to autoklick the right answer.
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# main function
gameid = '  '
gamepin = '4755908'
url = 'https://kahoot.it?pin=' + gamepin + '&refer_method=link'
nickname = 'Testuser1'

fp = webdriver.FirefoxProfile(profile_directory='/home/jf/.mozilla/firefox/6pgja4fq.default-release')

# Provide the path of chromedriver present on your system.
browser = webdriver.Firefox(fp)

# Send a get request to the url
browser.get(url)
time.sleep(2)
browser.find_element(By.NAME, "nickname").send_keys(nickname, Keys.ENTER)