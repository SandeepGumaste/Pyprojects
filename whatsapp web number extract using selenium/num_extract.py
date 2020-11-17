import pyautogui
import csv
from datetime import date
from selenium import webdriver
dat = str(date.today())
fn = dat + '.csv'
driver = webdriver.Chrome()
url = 'https://www.webscraper.io/test-sites/e-commerce/allinone'
driver.get(url)
driver.maximize_window()
driver.execute_script('window.scrollBy(0,200)')
pyautogui.FAILSAFE = False
xp = "//h4[starts-with(@class,'pull')]"
xt = "//a[contains(@class,'title')]"
pp = driver.find_elements_by_xpath(xp)
tt = driver.find_elements_by_xpath(xt)
price = list()
title = list()
for x in pp:
    price.append(x.text)
for x in tt:
    title.append(x.text)
with open(fn ,'w') as csvfile:
    filn = ['Title','Price']
    tw = csv.DictWriter(csvfile ,fieldnames = filn)
    tw.writeheader()
    count = 0
    while count < len(price):
        tw.writerow({'Title':title[count], 'Price':price[count]})
        count+=1
driver.close()
