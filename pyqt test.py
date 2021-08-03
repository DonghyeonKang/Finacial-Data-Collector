import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QListWidget, QTableWidget, QTableWidgetItem, QTableView, QAbstractItemView
from main import FDC

class MyApp(QWidget, FDC):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.companies = []
        self.tableitemnum = 0
        self.selected_companies = []

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle('My First Application')
        self.setStyleSheet("background-color: white;")
        self.move(250, 100)
        self.resize(1400, 800)
        
        # 버튼1
        btn1 = QPushButton('회사 목록 업데이트', self)
        btn1.move(100, 650)
        btn1.setStyleSheet("background-color: grey")
        btn1.setFont(QtGui.QFont('SansSerif', 15))
        btn1.resize(400, 80)
        btn1.clicked.connect(self.update_list)
        # 버튼2 
        btn2 = QPushButton('데이터 불러오기', self)
        btn2.move(900, 650)
        btn2.setStyleSheet("background-color: grey")
        btn2.setFont(QtGui.QFont('SansSerif', 15))
        btn2.resize(400, 80)
        btn1.clicked.connect(self.update_table)
        # 리스트
        self.list = QListWidget(self)
        self.list.resize(400, 500)
        self.list.move(100, 50)
        self.list.itemDoubleClicked.connect(self.add_to_table)
        # 테이블
        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(7)
        self.table.showGrid()
        self.table.resize(800, 500)
        self.table.move(520, 50)
        column_headers = ['회사명', '주가', '시가총액', 'PER', 'BPS', '단기차입금', '장기차입금']
        self.table.itemDoubleClicked.connect(self.del_from_table)
        self.table.setHorizontalHeaderLabels(column_headers)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 보여주기
        self.show()

    def update_list(self):
        fdc = FDC()
        self.companies = fdc.update_company_list()
        for i in self.companies:
            self.list.addItem(i)

    def update_table(self):
        pass

    def add_to_table(self):
        tmpitem = self.list.currentIndex()
        self.tableitemnum += 1
        self.table.setRowCount(self.tableitemnum)
        item = QTableWidgetItem(self.companies[tmpitem.row()])
        self.table.setItem(self.tableitemnum - 1, 0, item)
        self.selected_companies.append(self.companies[tmpitem.row()])

    def del_from_table(self):
        self.table.removeRow(self.table.currentRow())
        self.tableitemnum -= 1



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())