import bs4
from bs4 import BeautifulSoup
from html import parser
driver = web
url = "https://www.webscraper.io/test-sites/e-commerce/allinone"
driver.get(url)
driver.maximize_window()
soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())
