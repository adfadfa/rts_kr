import webbrowser
import socket
import sys
import pyperclip
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os

from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("rts_kr.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #시간
        self.now = datetime.now()
        self.today= "{}-{}-{} {}:{}:{}".format(self.now.year, self.now.month, self.now.day, self.now.hour, self.now.minute, self.now.second)
        print(self.today)

        #내 아이피 확인
        self.myip = self.ipcheck()
        print(self.myip)
        self.global_myip.setText(self.myip)

        #버튼 이벤트 핸들러
        self.global_myip.clicked.connect(self.COPY_MYIP)

        # side menu click event
        #self.weburl='https://www.youtube.com/channel/UChkU4i0CdTsF8xOochVdkQg?view_as=subscriber'
        self.seo_menu.clicked.connect(lambda: self.WEBLINK('https://www.youtube.com/channel/UChkU4i0CdTsF8xOochVdkQg?view_as=subscriber'))
        self.kuf_menu.clicked.connect(self.KUF_FRAME)
        self.jurassic_menu.clicked.connect(self.JURASSIC_FRAME)
        self.imjinrok_menu.clicked.connect(self.IMJINROK_FRAME)
        self.newmyth_menu.clicked.connect(self.NEWMYTH_FRAME)
        self.mirrorwar_menu.clicked.connect(self.MIRRORWAR_FRAME)
        self.atrox_menu.clicked.connect(self.ATROX_FRAME)

        #dynamic update from global_nikname to xx_myname
        self.global_nikname.textChanged.connect(self.CHANGE_MYNAME)

        #######전적 관리시스템###########
        self.GOOGLESHEET()



        # for self.cell in self.kuf_maplist:
            # # if self.cell.value == '':
                # break
            # self.kuf_map.addItem("")

        ##KUF_FRAME
        #WEB_site
        self.kuf_down.clicked.connect(lambda:self.WEBLINK('https://drive.google.com/file/d/0B9brBgUmPmnUZDRlTGpoS2R6UkE/view'))
        self.kuf_rank.clicked.connect(lambda:self.WEBLINK('https://docs.google.com/spreadsheets/d/1Dy-9UaCfiKm5hv_dpv7EvpMoGe6LjAVHqvgsWYSmG8c/edit#gid=0'))
        self.kuf_honor.clicked.connect(lambda:self.WEBLINK('http://kingdomunderfire.kr/%eb%aa%85%ec%98%88%ec%9d%98%ec%a0%84%eb%8b%b9/'))
        self.kuf_cafe.clicked.connect(lambda:self.WEBLINK('https://cafe.naver.com/kufagain'))
        self.kuf_kakao.clicked.connect(lambda:self.WEBLINK('https://open.kakao.com/o/gzO67CQ'))
        self.kuf_balance.clicked.connect(lambda:self.WEBLINK('https://docs.google.com/spreadsheets/d/1arhuFzACojr21NKBKj_yBechPgFg2_HSOEQDZU14FvM/edit#gid=0'))

        ## kuf_update
        #self.kuf_update.clicked.connect(lambda : self.RANK_UPDATE('kuf', self.kuf_myrace.currentText(), self.kuf_myname.text(), self.kuf_yourname.text(), self.kuf_yourace.currentText(), self.kuf_map.currentText(), 'win'))

        #Qradiobutton & Update Rank in Googlesheet
        self.kuf_update.clicked.connect(lambda : self.RANK_UPDATE('kuf', self.kuf_myrace.currentText(), self.kuf_myname.text(), self.kuf_yourname.text(), self.kuf_yourace.currentText(), self.kuf_map.currentText(), self.kuf_win.isChecked()))

        #EXEC KUF
        self.kuf_start.clicked.connect(self.OPENFILE)


    def OPENFILE(self):
        self.filepath = '"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Phantagram\Kingdom Under Fire\Kingdom Under Fire.lnk"'
        os.system(self.filepath)

    def GOOGLESHEET(self):
        self.scope = [
                    'https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive',
                    ]
        self.json_file_name = 'C:\\Users\\seo\\Downloads\\mobile-master\\python\\kufrankingsystem-281378b273ea.json'
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.json_file_name, self.scope)
        self.gc = gspread.authorize(self.credentials)
        self.kuf_spreadsheeturl = 'https://docs.google.com/spreadsheets/d/1Dy-9UaCfiKm5hv_dpv7EvpMoGe6LjAVHqvgsWYSmG8c/edit#gid=0'
        # 스프레스시트 문서 가져오기 
        self.doc = self.gc.open_by_url(self.kuf_spreadsheeturl)
        # 시트 선택하기
        self.kuf_worksheet_rank = self.doc.worksheet('랭킹')
        self.kuf_worksheet_history = self.doc.worksheet('전적히스토리')
        self.kuf_worksheet_stat= self.doc.worksheet('통계')

        self.kuf_maplist = self.kuf_worksheet_stat.range('A2:A100') #맵리스트 범위 지정

        for self.cell in self.kuf_maplist: # 맵리스트 출력
            if self.cell.value == '':
                break
            self.kuf_map.addItem(self.cell.value)


    def RANK_UPDATE(self, game, myrace, myname,yourname, yourace, gamemap,outcome) :
        if outcome == True :
            self.kuf_worksheet_history.update_cells('B16',['',self.today, gamemap,1500,myrace, myname, yourname, yourace,1500, '=K7-D7'])
            #self.kuf_worksheet_history.append_row(['',self.today, gamemap,1500,myrace, myname, yourname, yourace,1500, =K7-D7])
            print("승리")
        elif outcome == False :
            self.kuf_worksheet_history.append_row(['',self.today, gamemap, '1500',yourace, yourname, myname, myrace])
            print("패배")


    def CHANGE_MYNAME(self):
            #self.kuf_myname.text = v_myname
            self.global_nikname.textChanged[str].connect(self.kuf_myname.setText)
            self.global_nikname.textChanged[str].connect(self.imjinrok_myname.setText)
            self.global_nikname.textChanged[str].connect(self.jurassic_myname.setText)
            self.global_nikname.textChanged[str].connect(self.newmyth_myname.setText)
            self.global_nikname.textChanged[str].connect(self.mirrorwar_myname.setText)
            self.global_nikname.textChanged[str].connect(self.atrox_myname.setText)
            print(self.global_nikname.text())

    #copy myip   
    def COPY_MYIP(self):
        pyperclip.copy(self.myip)
        #pyperclip.copy(self.global_myip.text())         
        copymyip = pyperclip.paste()         
        print(copymyip)
    
    # extrac myip
    def ipcheck(self):
        return socket.gethostbyname(socket.getfqdn())

    def WEBLINK(self, weburl):
            webbrowser.open_new(weburl)
    def JURASSIC_FRAME(self) :
            print("쥬라기원시전")
            self.kuf_frame.setGeometry(250, 65, 491, 1)
            self.mirror_frame.setGeometry(250, 65, 491, 1)
            self.newmyth_frame.setGeometry(250, 65, 491, 1)
            self.imjinrok_frame.setGeometry(250, 65, 491, 1)
            self.atrox_frame.setGeometry(250, 65, 491, 1)
            self.jurrasic_frame.setGeometry(250, 65, 491, 321)
    def KUF_FRAME(self) :
            print("킹덤언더파이어")
            self.kuf_frame.setGeometry(250, 65, 491, 321)
            self.mirror_frame.setGeometry(250, 65, 491, 1)
            self.newmyth_frame.setGeometry(250, 65, 491, 1)
            self.imjinrok_frame.setGeometry(250, 65, 491, 1)
            self.atrox_frame.setGeometry(250, 65, 491, 1)
            self.jurrasic_frame.setGeometry(250, 65, 491, 1)
    def IMJINROK_FRAME(self) :
        print("조선의반격")
        self.kuf_frame.setGeometry(250, 65, 491, 1)
        self.mirror_frame.setGeometry(250, 65, 491, 1)
        self.newmyth_frame.setGeometry(250, 65, 491, 1)
        self.imjinrok_frame.setGeometry(250, 65, 491, 321)
        self.atrox_frame.setGeometry(250, 65, 491, 1)
        self.jurrasic_frame.setGeometry(250, 65, 491, 1)
    def NEWMYTH_FRAME(self) :
        print("신천년의신화")
        self.kuf_frame.setGeometry(250, 65, 491, 1)
        self.mirror_frame.setGeometry(250, 65, 491, 1)
        self.newmyth_frame.setGeometry(250, 65, 491, 321)
        self.imjinrok_frame.setGeometry(250, 65, 491, 1)
        self.atrox_frame.setGeometry(250, 65, 491, 1)
        self.jurrasic_frame.setGeometry(250, 65, 491, 1)
    def MIRRORWAR_FRAME(self) :
        print("거울전쟁")
        self.kuf_frame.setGeometry(250, 65, 491, 1)
        self.mirror_frame.setGeometry(250, 65, 491, 321)
        self.newmyth_frame.setGeometry(250, 65, 491, 1)
        self.imjinrok_frame.setGeometry(250, 65, 491, 1)
        self.atrox_frame.setGeometry(250, 65, 491, 1)
        self.jurrasic_frame.setGeometry(250, 65, 491, 1)
    def ATROX_FRAME(self) :
        print("아트록스")
        self.kuf_frame.setGeometry(250, 65, 491, 1)
        self.mirror_frame.setGeometry(250, 65, 491, 1)
        self.newmyth_frame.setGeometry(250, 65, 491, 1)
        self.imjinrok_frame.setGeometry(250, 65, 491, 1)
        self.atrox_frame.setGeometry(250, 65, 491, 321)
        self.jurrasic_frame.setGeometry(250, 65, 491, 1)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()