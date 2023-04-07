from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


def play_kahoot():
    fp = webdriver.FirefoxProfile(profile_directory='/home/jf/.mozilla/firefox/6pgja4fq.default-release')
    # Run Firefox
    browser = webdriver.Firefox(fp)

    gameid = "9983b771-65bc-4175-af56-d647d3cabc8d"

    browser.get('https://kahoot.it/rest/kahoots/' + gameid)
    time.sleep(1)

    browser.kahoot_answers = []

    browser.button_xpaths = {1: '''//*[@id="root"]/div/main/div[2]/div/div/button[1]''',
                             2: '''//*[@id="root"]/div/main/div[2]/div/div/button[2]''',
                             3: '''//*[@id="root"]/div/main/div[2]/div/div/button[3]''',
                             4: '''//*[@id="root"]/div/main/div[2]/div/div/button[4]'''}

    # GET KAHOOT ANSWERS
    # show answers

    # get answers
    browser.questions = browser.find_elements(By.NAME, "creator")  # finds all questions
    print(browser.questions)

    for browser.item_1 in browser.questions:  # loop through questions
        browser.choices = browser.item_1.find_elements(By.TAG_NAME, "li")  # find possible answers
        i = 1  # number of the correct answer (1-4)
        for browser.item_2 in browser.choices:  # loop through answers
            try:
                browser.correct_answer = browser.item_2.find_element(By.CLASS_NAME,
                                                                     "choices__choice--correct")  # if --correct div found on choice, choice is correct.
                browser.kahoot_answers += [i]
                break
            except:
                i += 1  # --correct div wasn't found, choice was incorrect, continueing...

play_kahoot()