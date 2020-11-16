import pyautogui
from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://www.webscraper.io/test-sites/e-commerce/allinone'
driver.get(url)
driver.maximize_window()
driver.execute_script('window.scrollBy(0,500)')
pyautogui.FAILSAFE = False
xp = "//h4[starts-with(@class,'pull')]"

res = driver.find_elements_by_xpath(xp)
for obj in res :
    print(obj.text)
driver.close()