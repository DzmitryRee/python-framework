import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
try:
	driver.get("https://www.youtube.com/")
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))
	element = driver.find_element_by_xpath("//input[@id='search']")
	element.send_keys('Rick r')
	element.send_keys(Keys.RETURN)
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="video-title"]')))
	driver.find_element_by_xpath('//a[@id="video-title"]').click()
	time.sleep(7)
finally:
	driver.quit()
