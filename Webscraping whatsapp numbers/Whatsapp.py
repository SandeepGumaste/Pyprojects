import pyautogui
import csv
import random
import string
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
cng = list() #To store generated contact names
def rs(length): #rs = random string
    letters = string.ascii_lowercase
    rn = ''.join(random.choice(letters) for i in range(length))
    cng.append(rn)
n = 60 #input("number of clicks")
m = 0
ng = 0
cl = list() #Contact list
while m < n: #
    try:
        res = driver.find_elements_by_xpath("//span[starts-with(@title,'+91')]")
        for c in res:
            cl.append(c.text)
    except:
        pass
    pyautogui.click(clicks = 2)
    m+=1
cl = list(set(cl))
while ng < len(cl):
    rs(6)
    ng+=1

with open(fn ,'w') as csvfile:
    tw = csv.DictWriter(csvfile ,fieldnames = ['Name','Phone Number'])
    tw.writeheader()
    count = 0
    while count < len(cl):
        tw.writerow({'Name':cng[count], 'Phone Number':cl[count]})
        count+=1
pyautogui.alert("press Enter after Logging out")
driver.close()