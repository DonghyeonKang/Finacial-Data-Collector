import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QListWidget, QTableWidget, QTableWidgetItem, QTableView, QAbstractItemView, QHBoxLayout, QLineEdit, QVBoxLayout, QMessageBox, QProgressBar

class FDC:
    def __init__(self):
        super().__init__()
        self.favorites = []
        self.companies_name = []
        self.PER = []
        self.EPS = []
        self.BPS = []
        self.market_cap = []
        self.stock = []
        self.short_term_borrowings = []
        self.long_term_borrowings = []

    def click_search(self, driver):
        wait = WebDriverWait(driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable((By.ID, "selUpjong")))
        except:
            print('로딩 시간 초과')
            
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
        time.sleep(1)
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
            self.click_search(driver)
            time.sleep(2)
            self.get_data(i[1] + 1, driver) 
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
            tmplist = driver.find_elements_by_xpath('//div[@id="svdMainGrid10D"]/table[@class="us_table_ty1 h_fix zigbg_no th_topbdno"]/tbody/tr[4]/td[@class="r"]')
            self.EPS.append(tmplist[0].text)      
        except:
            self.EPS.append("N/A")

        try:
            tmplist = driver.find_elements_by_xpath('//tr[@class="ac_row"]/td[@class="r"]')
            self.PER.append(tmplist[0].text)       
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

class MyApp(QWidget, FDC):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.companies = []
        self.tableitemnum = 0
        self.selected_companies = []
        self.excelopt = 0

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle('Finance Data Collector')
        self.setStyleSheet("background-color: white;")
        self.move(250, 100)
        self.resize(1400, 800)
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        # 회사 목록 업데이트
        btn1 = QPushButton('회사 목록 업데이트', self)
        btn1.move(100, 650)
        btn1.setStyleSheet("background-color: grey")
        btn1.setFont(QtGui.QFont('SansSerif', 15))
        btn1.resize(200, 80)
        btn1.clicked.connect(self.update_list)
        # 데이터 불러오기 버튼
        btn2 = QPushButton('데이터 불러오기', self)
        btn2.move(580, 650)
        btn2.setStyleSheet("background-color: grey")
        btn2.setFont(QtGui.QFont('SansSerif', 15))
        btn2.resize(180, 80)
        btn2.clicked.connect(self.update_table)
        # 텍스트 박스 
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 50)
        self.textbox.resize(320, 21)
        # Search 버튼
        btn3 = QPushButton("Search", self)
        btn3.move(425, 50)
        btn3.setStyleSheet("background-color: grey")
        btn3.setFont(QtGui.QFont('SansSerif', 9))
        btn3.clicked.connect(self.find_item)
        # 엑셀로 출력하기
        btn4 = QPushButton('엑셀 출력', self)
        btn4.move(800, 650)
        btn4.setStyleSheet("background-color: grey")
        btn4.setFont(QtGui.QFont('SansSerif', 15))
        btn4.resize(150, 80)
        btn4.clicked.connect(self.print_excel)
        # 리스트
        self.list = QListWidget(self)
        self.list.resize(400, 520)
        self.list.move(100, 80)
        self.list.itemDoubleClicked.connect(self.add_to_table)
        # 테이블
        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(8)
        self.table.showGrid()
        self.table.resize(800, 550)
        self.table.move(520, 50)
        column_headers = ['회사명', '주가', '시가총액', 'PER', 'EPS', 'BPS', '단기차입금', '장기차입금']
        self.table.itemDoubleClicked.connect(self.del_from_table)
        self.table.setHorizontalHeaderLabels(column_headers)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)        # 편집 기능 제거
        # 보여주기
        self.show()

    def update_list(self):
        fdc = FDC()
        self.companies = fdc.update_company_list()
        for i in self.companies:
            self.list.addItem(i[0])

    def update_found_list(self, text):
        self.list.clear()
        if text == "":
            for i in self.companies:
                self.list.addItem(i[0])
        else:
            for i in self.companies:
                if text == i[0]:
                    self.list.addItem(i[0])

    def update_table(self):
        fdc = FDC()
        fdc.update_finance_data(self.selected_companies)
        for i in range(self.tableitemnum):
            stock = QTableWidgetItem(fdc.stock[i])
            self.table.setItem(i, 1, stock)
            marcap = QTableWidgetItem(fdc.market_cap[i])
            self.table.setItem(i, 2, marcap)
            PER = QTableWidgetItem(fdc.PER[i])
            self.table.setItem(i, 3, PER)
            EPS = QTableWidgetItem(fdc.EPS[i])
            self.table.setItem(i, 4, EPS)
            BPS = QTableWidgetItem(fdc.BPS[i])
            self.table.setItem(i, 5, BPS)
            stb = QTableWidgetItem(fdc.short_term_borrowings[i])
            self.table.setItem(i, 6, stb)
            ltb = QTableWidgetItem(fdc.long_term_borrowings[i])
            self.table.setItem(i, 7, ltb)
        self.excelopt = 1

    def add_to_table(self):
        if self.tableitemnum < 25:
            self.tableitemnum += 1
            self.table.setRowCount(self.tableitemnum)

            tmpitem = self.list.currentItem().text()
            item = QTableWidgetItem(tmpitem)
            self.table.setItem(self.tableitemnum - 1, 0, item)

            for i in self.companies:
                if i[0] == tmpitem:
                    self.selected_companies.append(i)
        else:
            return

    def del_from_table(self):
        self.table.removeRow(self.table.currentRow())
        del self.selected_companies[self.table.currentRow()]
        self.tableitemnum -= 1

    def find_item(self):
        text = self.textbox.text()
        self.update_found_list(text)
    
    def print_excel(self):
        if self.excelopt == 0:
            return

        try:
            wb = openpyxl.load_workbook('FDC.xlsx')
            wb.remove(wb['Data'])
            ws = wb['Data']
            ws.append(['회사명', '주가', '시가총액', 'PER', 'EPS', 'BPS', '단기차입금', '장기차입금'])
            for i in range(self.tableitemnum):
                stock = self.table.item(i, 1).text()
                marcap = self.table.item(i, 2).text()
                PER = self.table.item(i, 3).text()
                EPS = self.table.item(i, 4).text()
                BPS = self.table.item(i, 5).text()
                stb = self.table.item(i, 6).text()
                ltb = self.table.item(i, 7).text()

                ws.cell(i + 2, 1, self.selected_companies[i][0])
                ws.cell(i + 2, 2, stock)
                ws.cell(i + 2, 3, marcap)
                ws.cell(i + 2, 4, PER)
                ws.cell(i + 2, 5, EPS)
                ws.cell(i + 2, 6, BPS)
                ws.cell(i + 2, 7, stb)
                ws.cell(i + 2, 8, ltb)
            wb.save('FDC.xlsx')
            wb.close()
        except:             # no file
            wb = openpyxl.Workbook()
            ws =  wb.active
            ws.title = "Data"
            ws.append(['회사명', '주가', '시가총액', 'PER', 'EPS', 'BPS', '단기차입금', '장기차입금'])
            for i in range(self.tableitemnum):
                stock = self.table.item(i, 1).text()
                marcap = self.table.item(i, 2).text()
                PER = self.table.item(i, 3).text()
                EPS = self.table.item(i, 4).text()
                BPS = self.table.item(i, 5).text()
                stb = self.table.item(i, 6).text()
                ltb = self.table.item(i, 7).text()

                ws.cell(i + 2, 1, self.selected_companies[i][0])
                ws.cell(i + 2, 2, stock)
                ws.cell(i + 2, 3, marcap)
                ws.cell(i + 2, 4, PER)
                ws.cell(i + 2, 5, EPS)
                ws.cell(i + 2, 6, BPS)
                ws.cell(i + 2, 7, stb)
                ws.cell(i + 2, 8, ltb)
            wb.save(filename = 'FDC.xlsx')
            wb.close()

        msg = QMessageBox()
        msg.setWindowTitle("알림")
        msg.setText('엑셀 출력 완료')
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        result = msg.exec_()
        self.excelopt = 0


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
