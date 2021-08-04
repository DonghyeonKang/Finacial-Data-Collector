import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FDC:

    def __init__(self):
        super().__init__()
        self.favorites = []
        self.companies_name = []
        self.PER = []
        self.BPS = []
        self.market_cap = []
        self.stock = []
        self.short_term_borrowings = []
        self.long_term_borrowings = []

    def click_search(self, driver):
        time.sleep(1)
        selectopt = driver.find_element_by_id("selUpjong")
        selectopt.send_keys(Keys.ENTER)
        selectopt.send_keys(Keys.ARROW_UP)
        selectopt.send_keys(Keys.ENTER)

        button = driver.find_element_by_id("btnSearch")    # 검색 버튼
        button.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="UJRankGrid"]//tbody/tr[2400]')))
        except:
            print('로딩 시간 초과')

    def update_company_list(self):
        options = webdriver.ChromeOptions()       # headless 옵션
        options.add_argument('headless')
        driver = webdriver.Chrome('chromedriver.exe', options=options)
        driver.get("https://comp.fnguide.com/SVO2/ASP/SVD_UJRank.asp?pGB=1&gicode=A079160&cID=&MenuYn=Y&ReportGB=&NewMenuID=301&stkGb=701")
        time.sleep(2)
        self.click_search(driver)
            
        tmplist = driver.find_elements_by_xpath('//tbody/tr[@class]/td[@class=" l tbold"]/a')
        companies = []
        for num, data in enumerate(tmplist):
            companies.append((data.text, num))
        driver.close()
        return companies

    def update_finance_data(self, selected_companies):
        options = webdriver.ChromeOptions()       # headless 옵션
        options.add_argument('headless')
        driver = webdriver.Chrome('chromedriver.exe', options=options)
        driver.get("https://comp.fnguide.com/SVO2/ASP/SVD_UJRank.asp?pGB=1&gicode=A079160&cID=&MenuYn=Y&ReportGB=&NewMenuID=301&stkGb=701")
        self.__init__()     # 리스트 초기화

        for i in selected_companies:         # 순위 목록 순서대로 
            self.get_data(i[1] + 1, driver) 
            time.sleep(2)
            self.click_search(driver)
        driver.close()

    def get_data(self, i, driver):
        time.sleep(1)
        company = driver.find_element_by_xpath('//div[@id="UJRankGrid"]//tbody/tr[%d]/td[@class=" l tbold"]/a' % i)     # 회사 페이지 인
        company.send_keys(Keys.ENTER)

        time.sleep(0.5)
        try:
            tmplist = driver.find_elements_by_id('svdMainChartTxt11')
            self.stock.append(tmplist[0].text)
        except:
            self.stock.append("N/A")        # 값이 없다면, can't find element error

        try:
            tmplist = driver.find_elements_by_xpath('//div[@id="svdMainGrid1"]//tbody/tr[5]/td[1]')
            self.market_cap.append(tmplist[0].text)
        except:
            self.market_cap.append("N/A")

        try:
            tmplist = driver.find_elements_by_xpath('//tr[@class="ac_row"]/td[@class="r"]')
            self.PER.append(tmplist[0].text)        # 첫 번째 요소 값이 PER 값이다. 
        except:
            self.PER.append("N/A")

        try:
            tmplist = driver.find_elements_by_xpath('//div[@id="highlight_D_A"]//tbody/tr[20]/td')
            if tmplist[len(tmplist) - 1].text != " ":           # 마지막 값이 없을 수도 있다. 그런데 마지막에서 두 번째 값도 없다면? 
                self.BPS.append(tmplist[len(tmplist) - 1].text)
            else:
                self.BPS.append(tmplist[len(tmplist) - 2].text)
        except:
                self.BPS.append("N/A")

        time.sleep(2)
        button = driver.find_element_by_xpath("//div[@class='headergnb']//li[@class='gnb_dp2 gnb_dp2_start']/a[3]")         # 제무제표 페이지
        button.send_keys(Keys.ENTER)                                                                                        # 인
        time.sleep(0.5)
        try:
            button = driver.find_element_by_id("grid2_6")
            button.send_keys(Keys.ENTER)
            time.sleep(0.5)
            tmplist = driver.find_elements_by_xpath('//div[@id="divDaechaY"]//tbody/tr[32]/td')
            if tmplist[len(tmplist) - 1].text != " ":
                self.short_term_borrowings.append(tmplist[len(tmplist) - 1].text)
            else:
                self.short_term_borrowings.append(tmplist[len(tmplist) - 2].text)
        except:
            self.short_term_borrowings.append("N/A")

        try:
            button = driver.find_element_by_id("grid2_7")
            button.send_keys(Keys.ENTER)
            time.sleep(0.5)
            tmplist = driver.find_elements_by_xpath('//div[@id="divDaechaY"]//tbody/tr[46]/td')
            if tmplist[len(tmplist) - 1].text != " ":
                self.long_term_borrowings.append(tmplist[len(tmplist) - 1].text)
            else:
                self.long_term_borrowings.append(tmplist[len(tmplist) - 2].text)
        except:
            self.long_term_borrowings.append("N/A")
        driver.back()          # 제무제표 페이지 아웃
        time.sleep(1)
        driver.back()          # 회사 페이지 아웃