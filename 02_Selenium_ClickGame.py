# ChromeDriver
# https%3A%2F%2Fsites.google.com%2Fa%2Fchromium.org%2Fchromedriver%2Fdownloads&v=ximjGyZ93YQ
# https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = "C:/Python39/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://tsj.tw/")

actions = ActionChains(driver)
time.sleep(2)

blow = driver.find_element(By.XPATH, '//*[@id="click"]')
blow_count = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')

#actions.perform()
items = []
items.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))
items.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))
items.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))

prices = []
prices.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))
prices.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))

for i in range(10000):
    actions.click(blow)
    actions.perform()
    countpoint = int(blow_count.text.replace("您目前擁有", "").replace("技術點", ""))
    
    for j in range(3):
        price = int(prices[j].text.replace("技術點", ""))

        if price <= countpoint:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(items[j])
            upgrade_actions.click()
            upgrade_actions.perform()
            break


time.sleep(5)
driver.quit()