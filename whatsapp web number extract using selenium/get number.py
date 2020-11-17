import pyautogui
import csv
from selenium import webdriver
from datetime import date
dat = str(date.today())
fn = dat + '.csv'
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
pyautogui.FAILSAFE = False
pyautogui.alert("Press Enter when the page loads fully after scanning qr code")
(x,y) = pyautogui.position()
pyautogui.move(-x,-y)
pyautogui.move(607,1050)
lst = list()
n = 30 #input("number of clicks")
m = 0
cl = list() #Contact list
while m < n:
    try:
        res = driver.find_elements_by_xpath("//span[starts-with(@title,'+91')]")
        for c in res:
            cl.append(c.text)
    except:
        pass
    pyautogui.click(clicks = 2)
    m = m +1
cl = list(set(cl))
with open(fn ,'w') as csvfile:
    tw = csv.DictWriter(csvfile ,fieldnames = ['Name','Phone Number'])
    tw.writeheader()
    count = 0
    while count < len(cl):
        tw.writerow({'Name':cl[count], 'Phone Number':cl[count]})
        count+=1
driver.close()
