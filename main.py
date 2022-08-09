#    This is a KahootCheatBot expansion to https://github.com/RealNattawattHongthong/kahoot-cheat KahootCheater. It adds the ability to autoklick the right answer.
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

gameid = ''
gamepin = ''
nickname= ''

# get gamepin & gameid
def values():

    global gameid
    global gamepin
    global nickname

    print("\n Please enter Game-ID: ")
    gameid = input()

    print("\n Please enter Game-PIN: ")
    gamepin = input()

    print("\n Please enter your Nickname: ")
    nickname = input()

values()

game_url = 'https://kahoot.it?pin=' + gamepin + '&refer_method=link'
game_id_url = 'https://create.kahoot.it/details/' + gameid

fp = webdriver.FirefoxProfile(profile_directory='/home/jf/.mozilla/firefox/6pgja4fq.default-release')

# Provide the path of firefox present on your system.
browser = webdriver.Firefox(fp)

browser.kahoot_answers = []

browser.button_xpaths = {1: '''//*[@id="root"]/div/main/div[2]/div/div/button[1]''',
                              2: '''//*[@id="root"]/div/main/div[2]/div/div/button[2]''',
                              3: '''//*[@id="root"]/div/main/div[2]/div/div/button[3]''',
                              4: '''//*[@id="root"]/div/main/div[2]/div/div/button[4]'''}

# Send a get request to the url
browser.get(game_id_url)
time.sleep(1)

# GET KAHOOT ANSWERS
# show answers
browser.show_answers_button = browser.find_element(By.XPATH, '''//*[contains(text(), "Show answers")]''')
browser.show_answers_button.click()

# get answers
browser.questions = browser.find_elements(By.CLASS_NAME, "choices")  # finds all questions
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

# JOIN KAHOOT
# #play kahoot itself
browser.get(game_url)
time.sleep(1)
browser.find_element(By.NAME, "nickname").send_keys(nickname, Keys.ENTER)

# PLAY KAHOOT
while True:
    # search for a button to confirm the round has started
    while True:
        try:
            browser.find_element(By.XPATH, browser.button_xpaths[1])
            break
        except:
            pass

    # find round of max rounds for example 5 of 16
    try:
        browser.round_of_max_rounds = browser.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div[2]").text
    except:
        pass

    # split round of max rounds with " " and access first element in the list aka. the current round and convert it to a integer
    browser.round = int(browser.round_of_max_rounds.split(" ")[0])
    # access that rounds answer
    try:
        browser.search_with_xpath = browser.button_xpaths[browser.kahoot_answers[browser.round - 1]]
    except:
        break

    while True:  # loop till success
        try:
            # find the correct button
            browser.button = browser.find_element(By.XPATH, browser.search_with_xpath)

            # if bot is in realistic mode, wait few seconds
            #if is_realistic:
            #    sleep(randint(1, 10))

            browser.button.click()  # click the button
            break  # exit loop
        except:
            pass

    while True:  # loop to avoid double clicking a button
        try:
            browser.find_element(By.XPATH, browser.search_with_xpath)
        except:
            break