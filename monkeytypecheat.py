#this should be run while the virtual environment is active

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome()

driver.get("https://monkeytype.com")
sleep(5)
cookieelement = driver.find_element(By.CLASS_NAME, "button.active.acceptAll")
cookieelement.click()
wordbox = driver.find_element(By.ID, "wordsInput")
while True:
    currentword = driver.find_element(By.CLASS_NAME, "word.active").text

    wordbox.send_keys(currentword)
    wordbox.send_keys(Keys.SPACE)

