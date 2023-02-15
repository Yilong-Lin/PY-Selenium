# ChromeDriver
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2xCZkY0dkFCdTFtY0ZaeUQ4V3lHQkhKdFlxd3xBQ3Jtc0tuUjAzeFU2bWhqd19ram82b24zLXlTNldvR3Q0aDJ5U05LbXRsLWdDMGpqaEUyOW5WWmZJMDlrYzMwZmhmV2JNc1A0TnM0bU9QX0FqSXBXa3ltR2c2SF9UMWJNRkJtLWFpSWM1ZlM4d2pPbzJWdHpQNA&q=https%3A%2F%2Fsites.google.com%2Fa%2Fchromium.org%2Fchromedriver%2Fdownloads&v=ximjGyZ93YQ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:/Python39/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://google.com")

# print(driver.title)
time.sleep(2)
search = driver.find_element(By.NAME, "q")
search.clear()

search.send_keys("shuiba inu")
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.ID,"result-stats")
)

titles = driver.find_elements(By.CLASS_NAME, "LC20lb")
for title in titles:
    if (title.text != ""):
        print(title.text)


link = driver.find_element(By.CSS_SELECTOR, "#kp-wp-tab-overview > div:nth-child(20) > div > div > div > div.g.Ww4FFb.vt6azd.tF2Cxc > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a > h3")

link.click()

driver.back()
driver.forward()

time.sleep(5)
driver.quit()