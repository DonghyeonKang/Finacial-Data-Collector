import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

companies = ['한진중공업', '삼성전자', 'SK']

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
driver.get("https://comp.fnguide.com/SVO2/ASP/SVD_UJRank.asp?pGB=1&gicode=A079160&cID=&MenuYn=Y&ReportGB=&NewMenuID=301&stkGb=701")

# ---- 1. 검색 시 생기는 경고창 처리는 어떻게 해야 하는가? ----
selectopt = driver.find_element_by_id("selUpjong")
selectopt.send_keys(Keys.ENTER)
selectopt.send_keys(Keys.ARROW_UP)
selectopt.send_keys(Keys.ENTER)

button = driver.find_element_by_id("btnSearch")
button.send_keys(Keys.ENTER)
time.sleep(10)  # 로딩 대기 시간

elements = driver.find_elements_by_xpath('//tbody/tr[@class]/td[@class=" l tbold"]/a')         # SK 하이닉스
a = elements[0]
a.send_keys(Keys.ENTER)

time.sleep(1)
#for i in elements:
#    print(i.text)

# for i in companies:
#     search_company = driver.find_element_by_id("SearchText")
#     time.sleep(0.5)
#     search_company.send_keys(i)
#     search_company.send_keys(Keys.ENTER)

#     try:
#         driver.switch_to_alert()


#     time.sleep(0.5)
#     search_company.send_keys(Keys.ESCAPE)
#     time.sleep(0.5)
#     search_company.send_keys(Keys.ESCAPE)
#     time.sleep(0.5)
#     search_company.send_keys(Keys.ARROW_DOWN)
#     time.sleep(0.5)
#     search_company.send_keys(Keys.ARROW_DOWN)
#     time.sleep(0.5)
#     search_company.send_keys(Keys.ENTER)
#     time.sleep(0.5)
    
#     print(i)


# ---- 2. 특정 요소 찾기는 어떻게 해야 하는가? ----
# elements = driver.find_elements_by_xpath('//tr[@class="ac_row"]/td[@class="r"]')        # 첫 번째 요소 값이 PER 값이다. 
# for i in elements:
#     print(i.text)

# time.sleep(1)

# ---- 3. 회사가 달라도 동일한 코드로 원하는 데이터를 얻을 수 있는가?  ----
# companies = ['삼성전자', 'SK하이닉스', 'SK', 'SK이노베이션', '솔브레인홀딩스', 'KB금융', 'LG', '신한지주', '기업은행', 'LG전자']
# PER = []

# for i in companies:

#     elements = driver.find_elements_by_xpath('//tr[@class="ac_row"]/td[@class="r"]')        # 첫 번째 값이 PER 값이다. 
#     PER.append(elements[0])

# for i in range(len(companies)):
#     print(companies[i], " ", PER[i])

driver.quit()