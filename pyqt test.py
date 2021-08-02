import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QListWidget
from PyQt5.QtGui import QFont
from main import FDC

class MyApp(QWidget, FDC):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.companies = []

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
        btn1.setFont(QFont('SansSerif', 15))
        btn1.resize(400, 80)
        btn1.clicked.connect(self.update_list1)
        # 버튼2 
        btn2 = QPushButton('데이터 불러오기', self)
        btn2.move(900, 650)
        btn2.setStyleSheet("background-color: grey")
        btn2.setFont(QFont('SansSerif', 15))
        btn2.resize(400, 80)
        btn1.clicked.connect(self.update_list2)
        # 리스트 박스1
        self.list1 = QListWidget(self)
        self.list1.resize(400, 500)
        self.list1.move(100, 50)
        self.list1.itemDoubleClicked.connect(self.add_to_list2)
        # 리스트 박스2
        self.list2 = QListWidget(self)
        self.list2.resize(700, 500)
        self.list2.move(600, 50)
        self.list2.insertItem(0, "qweq")
        self.list2.insertItem(1, "qweq")
        self.list2.insertItem(2, "qweq")
        self.list2.itemDoubleClicked.connect(self.del_from_list2)
        
        self.show()

    def update_list1(self):
        fdc = FDC()
        self.companies = fdc.update_company_list()
        for i in self.companies:
            self.list1.addItem(i)

    def update_list2(self):
        pass

    def add_to_list2(self):
        item = self.list1.currentIndex()
        self.list2.addItem(self.companies[item.row()])

    def del_from_list2(self):
#        item = self.list1.currentIndex()
        listItems = self.list2.selectedItems()
        for item in listItems:
            self.list2.takeItem(self.list2.row(item))



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())