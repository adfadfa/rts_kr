import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("test.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #GroupBox안에 있는 RadioButton들을 연결합니다.
        #GroupBox의 자세한 설명은 02.14 GroupBox를 참고하세요.

        self.top.clicked.connect(self.groupboxRadFunction)
        self.button.clicked.connect(self.groupboxRadFunction)

    def PP(self, outcome) :
        print(outcome)

    def groupboxRadFunction(self) :
        if self.top.isChecked() : 
            print("GroupBox_rad1 Chekced")
            QtGui.Q
            self.update.clicked(self.PP('hi'))
        elif self.button.isChecked() : 
            print("GroupBox_rad2 Checked")
            self.update.clicked(self.PP('why'))


        




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()