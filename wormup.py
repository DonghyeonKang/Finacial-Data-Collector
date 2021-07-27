import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:\Program Files\Google\Chrome\chromedriver_win32\chromedriver.exe')
driver.get("https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN=")

search_company = driver.find_element_by_id("SearchText")
search_company.send_keys("한진중공업")
time.sleep(0.3)
search_company.send_keys(Keys.ENTER)

time.sleep(2)
if driver.switch_to_alert():
    driver.switch_to_alert().accept()
    search_company.send_keys(Keys.ESCAPE)
    search_company.send_keys(Keys.ARROW_DOWN)
    search_company.send_keys(Keys.ARROW_DOWN)
    search_company.send_keys(Keys.ENTER)

time.sleep(2)


# soup = BeautifulSoup(driver.page_source, 'html.parser')


