# ChromeDriver
# https%3A%2F%2Fsites.google.com%2Fa%2Fchromium.org%2Fchromedriver%2Fdownloads&v=ximjGyZ93YQ
# https://www.selenium.dev/documentation/
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import wget


PATH = "C:/Python39/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.NAME, 'username')
)
WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.NAME, 'password')
)

# login_btn = driver.find_element(By.XPATH,'//*[@id="mount_0_0_7c"]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div/div[2]/div[2]/button')
name_input = driver.find_element(By.NAME, 'username')
pass_input = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

name_input.clear()
pass_input.clear()
name_input.send_keys("yilong0528")
pass_input.send_keys("")

login_button.click()

# actions = ActionChains(driver)
# actions.click(login_btn)
# actions.perform()

search_input = WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.CLASS_NAME, '_aauy')
)

#search_input = driver.find_element(By.CLASS_NAME, '_aauy')

keyword = "shib inu"
search_input.clear()

search_input.send_keys(keyword)
time.sleep(2)
search_input.send_keys(Keys.RETURN)
# time.sleep(2)
# search_input.send_keys(Keys.RETURN)

search_input = WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.CLASS_NAME, '_aagw')
)

#x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3

#"//div[@class='target with space or maybe another-long-text']"

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)

imgs = driver.find_elements(By.XPATH, '//*[@id="mount_0_0_dY"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[1]/img')
#imgs = driver.find_elements(By.XPATH, "//div[@class='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']")

path = os.path.join(keyword)
os.mkdir(path)

count = 0
for img in imgs:
    save_as = os.path.join(path, keyword + str(count) + '.jpg')
    wget.download(img.get_attribute("src"), save_as)
    count += 1

time.sleep(5)
driver.quit()