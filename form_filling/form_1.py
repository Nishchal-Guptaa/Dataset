from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('https://ambaenterprises.in/contact.html')

name = browser.find_element(By.NAME, 'name')
phnno = browser.find_element(By.NAME, 'phnno')
email = browser.find_element(By.NAME, 'email')
Message = browser.find_element(By.NAME, 'message')

name.send_keys("Bot")
phnno.send_keys(8802499327)
email.send_keys("etc@gmail.com")
Message.send_keys("Testing the bot")

button = browser.find_element(By.XPATH, "//button[text()='Send Message']")
button.click()

time.sleep(3)
browser.close()
