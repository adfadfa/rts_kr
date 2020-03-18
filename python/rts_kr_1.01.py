import webbrowser
import socket
import sys
import pyperclip
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("rts_kr.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #GroupBox안에 있는 RadioButton들을 연결합니다.
        #GroupBox의 자세한 설명은 02.14 GroupBox를 참고하세요.

        #내 아이피 확인
        #self.kuf_menu.clicked.connect(JURASSIC_FRAME)

        myip = self.ipcheck()
        self.global_myip.setText(myip)
        self.global_myip.clicked.connect(self.COPY_MYIP)

        self.seo_menu.clicked.connect(lambda: self.WEBLINK(self, 'https://www.youtube.com/channel/UChkU4i0CdTsF8xOochVdkQg?view_as=subscriber'))

    def ipcheck(self):
        return socket.gethostbyname(socket.getfqdn())

    def WEBLINK(weblink):
            webbrowser.open_new(weblink)
            print(weblink)

    def COPY_MYIP():
        pyperclip.copy(self.myip)         
        copymyip = pyperclip.paste()         
        print(copymyip)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()