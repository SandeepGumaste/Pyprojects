import pyautogui
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
pyautogui.FAILSAFE = False
pyautogui.alert("Press Enter when the page loads fully after ")
(x,y) = pyautogui.position()
pyautogui.move(-x,-y)
pyautogui.move(607,1038)
lst = list()
n = 60 #input("number of clicks")
m = 0
l = list()
while m < n:
    try:
        res = driver.find_elements_by_xpath("//span[starts-with(@title,'+91')]")
        for c in res:
            l.append(c.text)
        pyautogui.click(clicks = 3)
        m = m +1
    except:
        pyautogui.click(clicks = 3)
        m = m +1
l = set(l)
for cc in l:
    print(cc)