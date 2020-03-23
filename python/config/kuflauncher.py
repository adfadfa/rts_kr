# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\seo\Downloads\mobile-master\python\kuflauncher.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'C:\\Users\seo\Downloads\mobile-master\python\kufrankingsystem-281378b273ea.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1Dy-9UaCfiKm5hv_dpv7EvpMoGe6LjAVHqvgsWYSmG8c/edit#gid=0'
# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('통계')
worksheet1 = doc.worksheet('랭킹')


import socket

def ipcheck():
	return socket.gethostbyname(socket.getfqdn())

print(ipcheck())



range_list = worksheet.range('A2:A100') #맵리스트 범위 지정

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 284)
        MainWindow.resize(531, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cafe = QtWidgets.QPushButton(self.centralwidget)
        self.cafe.setGeometry(QtCore.QRect(270, 30, 101, 81))
        self.cafe.setObjectName("cafe")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 120, 451, 111))
        self.groupBox.setObjectName("groupBox")
        self.update = QtWidgets.QPushButton(self.groupBox)
        self.update.setGeometry(QtCore.QRect(340, 10, 101, 91))
        self.update.setObjectName("update")
        self.myrace = QtWidgets.QComboBox(self.groupBox)
        self.myrace.setGeometry(QtCore.QRect(160, 20, 76, 22))
        self.myrace.setObjectName("myrace")
        self.myrace.addItem("")
        self.myrace.addItem("")
        self.myname = QtWidgets.QLineEdit(self.groupBox)
        self.myname.setGeometry(QtCore.QRect(60, 20, 91, 20))
        self.myname.setObjectName("myname")
        self.yourname = QtWidgets.QLineEdit(self.groupBox)
        self.yourname.setGeometry(QtCore.QRect(60, 50, 91, 20))
        self.yourname.setObjectName("yourname")
        self.yourace = QtWidgets.QComboBox(self.groupBox)
        self.yourace.setGeometry(QtCore.QRect(160, 50, 76, 22))
        self.yourace.setObjectName("yourace")
        self.yourace.addItem("")
        self.yourace.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 41, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 41, 21))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.win = QtWidgets.QRadioButton(self.groupBox)
        self.win.setGeometry(QtCore.QRect(260, 20, 51, 21))
        self.win.setTabletTracking(False)
        self.win.setObjectName("win")
        self.win.setChecked(True) # 라디오버튼 기본 체크
        self.lose = QtWidgets.QRadioButton(self.groupBox)
        self.lose.setGeometry(QtCore.QRect(260, 50, 51, 21))
        self.lose.setObjectName("lose")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 41, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 80, 181, 22))
        self.comboBox.setObjectName("map") #콤보박스 리스트 숫자

        
        

        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(40, 240, 450, 40))
        self.start.setObjectName("start")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\seo\Downloads\mobile-master\python\KingdomUnderFire_128.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.start.setIcon(icon)
        
        for cell in range_list:            
            if cell.value == '':
                break
            self.comboBox.addItem("")
            
        self.balance = QtWidgets.QPushButton(self.centralwidget)
        self.balance.setGeometry(QtCore.QRect(380, 30, 101, 81))
        self.balance.setObjectName("balance")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 30, 104, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gold = QtWidgets.QPushButton(self.groupBox_2)
        self.gold.setObjectName("gold")
        self.verticalLayout.addWidget(self.gold)
        self.original = QtWidgets.QPushButton(self.groupBox_2)
        self.original.setObjectName("original")
        self.verticalLayout.addWidget(self.original)
        self.rank = QtWidgets.QPushButton(self.centralwidget)
        self.rank.setGeometry(QtCore.QRect(160, 30, 101, 81))
        self.rank.setObjectName("rank")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_6)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "킹덤언더파이어 런처"))
        self.cafe.setText(_translate("MainWindow", "커프 커뮤니티"))
        self.cafe.clicked.connect(self.CAFE)
        self.groupBox.setTitle(_translate("MainWindow", "전적 업데이트"))
        self.update.setText(_translate("MainWindow", "업데이트"))
        self.update.clicked.connect(self.RANK_UPDATE)
        self.myrace.setItemText(0, _translate("MainWindow", "휴먼"))
        self.myrace.setItemText(1, _translate("MainWindow", "데빌"))
        self.yourace.setItemText(0, _translate("MainWindow", "휴먼"))
        self.yourace.setItemText(1, _translate("MainWindow", "데빌"))
        self.label_2.setText(_translate("MainWindow", "상대방"))
        self.label_3.setText(_translate("MainWindow", "나"))
        self.win.setText(_translate("MainWindow", "승리"))
        self.lose.setText(_translate("MainWindow", "패배"))
        self.label_4.setText(_translate("MainWindow", "대전맵"))
        self.start.setText(_translate("MainWindow", "KUF Start"))
        cnt = 0
        for cell in range_list: # 맵리스트 출력
            self.comboBox.setItemText(cnt, _translate("MainWindow", cell.value))
            cnt+=1
            print(cell.value, cnt)
            if cell.value == '':
                break
        self.balance.setText(_translate("MainWindow", "유닛 상성표"))
        self.balance.clicked.connect(self.BALANCE)
        self.groupBox_2.setTitle(_translate("MainWindow", "패치 적용하기"))
        self.gold.setText(_translate("MainWindow", "골드패치"))
        self.original.setText(_translate("MainWindow", "오리지널 패치"))
        self.rank.setText(_translate("MainWindow", "전적기록실"))
        self.rank.clicked.connect(self.OPEN_RANK)
        self.menu.setTitle(_translate("MainWindow", "설정"))
        self.menu_2.setTitle(_translate("MainWindow", "런처업데이트"))
        self.action.setText(_translate("MainWindow", "런처 업데이트"))
        self.action_2.setText(_translate("MainWindow", "런처 업데이트"))
        self.action_3.setText(_translate("MainWindow", "경로설정"))
        self.action_4.setText(_translate("MainWindow", "설치 경로설정"))
        self.action_5.setText(_translate("MainWindow", "런처 정보"))
        self.action_6.setText(_translate("MainWindow", "종료"))

    

    def OPEN_RANK(self):
        print("hi")
        webbrowser.open_new("https://docs.google.com/spreadsheets/d/1Dy-9UaCfiKm5hv_dpv7EvpMoGe6LjAVHqvgsWYSmG8c/edit#gid=0")
    def BALANCE(self):
        webbrowser.open_new("https://docs.google.com/spreadsheets/d/1arhuFzACojr21NKBKj_yBechPgFg2_HSOEQDZU14FvM/edit#gid=0")
    def CAFE(self):
        webbrowser.open_new("https://cafe.naver.com/kufagain")
    def RANK_UPDATE(self):
       worksheet1.append_row(['new1', 'new2', 'new3', 'new4', 'new5', 'new6'])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
