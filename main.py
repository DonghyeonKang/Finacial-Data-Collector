import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FDC:
    favorites = []
    companies_name = []
    PER = []
    BPS = []
    market_cap = []
    stock = []
    short_term_borrowings = []
    long_term_borrowings = []
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://comp.fnguide.com/SVO2/ASP/SVD_UJRank.asp?pGB=1&gicode=A079160&cID=&MenuYn=Y&ReportGB=&NewMenuID=301&stkGb=701")

    def __init__(self):
        super().__init__()
        selectopt = self.driver.find_element_by_id("selUpjong")
        selectopt.send_keys(Keys.ENTER)
        selectopt.send_keys(Keys.ARROW_UP)
        selectopt.send_keys(Keys.ENTER)
        self.click_search()
        self.update_company_list()
        self.update_finance_data()

    def click_search(self):
        button = self.driver.find_element_by_id("btnSearch")
        button.send_keys(Keys.ENTER)
        time.sleep(6)  # 로딩 대기 시간

    def update_finance_data(self):
        for i in range(1, len(self.companies_name) + 1):         # 순위 목록 순서대로 
            company = self.driver.find_element_by_xpath('//div[@id="UJRankGrid"]//tbody/tr[%d]/td[@class=" l tbold"]/a' % i)     # 회사 페이지
            company.send_keys(Keys.ENTER)                                                                                   # 인
            self.update_PER()
            self.update_BPS()
            self.update_market_cap()
            self.update_stock()
            button = self.driver.find_element_by_xpath("//div[@class='headergnb']//li[@class='gnb_dp2 gnb_dp2_start']/a[3]")    # 제무제표 페이지
            button.send_keys(Keys.ENTER)                                                                                        # 인
            self.short_term_borrowings.append(self.update_short_term_borrowings())
            self.long_term_borrowings.append(self.update_long_term_borrowings())
            self.driver.back()          # 제무제표 페이지 아웃
            time.sleep(0.5)
            self.driver.back()          # 회사 페이지 아웃
            self.click_search()

    def update_stock(self):
        try:
            tmplist = self.driver.find_elements_by_id('svdMainChartTxt11')
            print(tmplist[0].text)
            self.stock.append(tmplist[0].text)
        except:
            self.stock.append(" ")

    def update_market_cap(self):
        try:
            tmplist = self.driver.find_elements_by_xpath('//div[@id="svdMainGrid1"]//tbody/tr[5]/td[1]')
            print(tmplist[0].text)
            self.stock.append(tmplist[0].text)
            self.market_cap.append(tmplist[0].text)
        except:
            self.market_cap.append(" ")

    def update_PER(self):
        try:
            tmplist = self.driver.find_elements_by_xpath('//tr[@class="ac_row"]/td[@class="r"]')
            print(tmplist[0].text)
            self.PER.append(tmplist[0].text)        # 첫 번째 요소 값이 PER 값이다. 
        except:
            self.PER.append(" ")        # 첫 번째 요소 값이 PER 값이다. 


    def update_BPS(self):
        try:
            tmplist = self.driver.find_elements_by_xpath('//div[@id="highlight_D_A"]//tbody/tr[20]/td')        # 첫 번째 요소 값이 PER 값이다. 
            if tmplist[len(tmplist) - 1].text != " ":           # 마지막 값이 없을 수도 있다. 그런데 마지막에서 두 번째 값도 없다면? 
                print(tmplist[len(tmplist) - 1].text)
                self.BPS.append(tmplist[len(tmplist) - 1].text)
            else:
                self.BPS.append(tmplist[len(tmplist) - 2].text)
        except:
                self.BPS.append(" ")

    def update_short_term_borrowings(self):
        time.sleep(0.2)
        try:
            button = self.driver.find_element_by_id("grid2_6")
            button.send_keys(Keys.ENTER)
            tmplist = self.driver.find_elements_by_xpath('//div[@id="divDaechaY"]//tbody/tr[32]/td')
            if tmplist[len(tmplist) - 1].text != " ":
                return tmplist[len(tmplist) - 1].text
            else:
                return tmplist[len(tmplist) - 2].text
        except:
            return " "

    def update_long_term_borrowings(self):
        time.sleep(0.2)
        try:
            button = self.driver.find_element_by_id("grid2_7")
            button.send_keys(Keys.ENTER)
            tmplist = self.driver.find_elements_by_xpath('//div[@id="divDaechaY"]//tbody/tr[46]/td')
            if tmplist[len(tmplist) - 1].text != " ":
                return tmplist[len(tmplist) - 1].text
            else:
                return tmplist[len(tmplist) - 2].text
        except:
            return " "


    def update_company_list(self):
        companies = self.driver.find_elements_by_xpath('//tbody/tr[@class]/td[@class=" l tbold"]/a')
        for i in companies:
            self.companies_name.append(i.text)
#        self.companies_name.sort()

    def set_excel_frame(self):
        pass

    def print_data_to_excel(self):
        pass

    def set_favorites(self):
        pass

a = FDC()
a.update_finance_data()
print(a.BPS)
