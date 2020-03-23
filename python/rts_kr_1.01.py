import pywintypes
import win32api
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


form_class = uic.loadUiType("C:\\Users\\seo\\AndroidStudioProjects\\rts_kr\\python\\rts_kr.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


        #창고정
        self.setFixedSize(760,510)

        #시간
        self.now = datetime.now()
        self.today= "{}-{}-{} {}:{}:{}".format(self.now.year, self.now.month, self.now.day, self.now.hour, self.now.minute, self.now.second)
        print(self.today)

        #내 아이피 확인
        self.myip = self.ipcheck()
        print(self.myip)
        self.global_myip.setText(self.myip)

        #IP 버튼 이벤트 핸들러
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

        #닉네임 초기화값 및 dynamic update from global_nikname to xx_myname

        self.global_nikname.textChanged.connect(self.CHANGE_MYNAME)
        self.global_nikname.editingFinished.connect(self.UPDATE_MYRANK)

        #######전적 관리시스템###########
        self.GOOGLESHEET()

        #글로벌 닉네임 로드
        try:
            self.loadip = self.admin_worksheet_tooluser.find(self.myip)
            print("닉네임이 있다.",self.loadip.value)
            self.loadnikname = self.admin_worksheet_tooluser.cell(self.loadip.row,3)
            self.global_nikname.setText(str(self.loadnikname.value))
            
            self.kuf_myname.setText(str(self.loadnikname.value))
            self.imjinrok_myname.setText(str(self.loadnikname.value))
            self.jurassic_myname.setText(str(self.loadnikname.value))
            self.mirrorwar_myname.setText(str(self.loadnikname.value))
            self.newmyth_myname.setText(str(self.loadnikname.value))
            self.atrox_myname.setText(str(self.loadnikname.value))

            self.UPDATE_MYRANK()     
            self.nonikchk = 0 
        except :
            print("닉네임이 없다")
            QMessageBox.about(self,"닉네임 등록요청", "왼쪽상단에 닉네임을 등록해주세요!")
            self.nonikchk = 1


            #self.cell_list = self.admin_worksheet_tooluser.range('C2:C1000') #유저 리스트 범위 지정
            #for self.cell in self.cell_list: # 유저 리스트 반복문
            #    if self.cell.value == '':
            #        print("유저 최초 등록 : ",self.checkusername)
            #        self.admin_worksheet_tooluser.update_cell(self.cell.row,2, self.myip)
            #        self.admin_worksheet_tooluser.update_cell(self.cell.row,3, gloabl_nikname)
            #        break            



        #런처 정보&접속자 이력확인 확인
        self.toolver = str(1.01)
        self.lastver = self.admin_worksheet_admintool.cell(2,3).value
        self.lastdownload =self.admin_worksheet_admintool.cell(3,3).value
        
        print("런처 버전: ", str(self.toolver),"최신버전 :", self.lastver)
        
        
        if(self.toolver != self.lastver) :
            QMessageBox.about(self,"업데이트 알림", "최신버전이 아닙니다.\n최신버전을 다운로드 해야 합니다.\n현재버전 : "+self.toolver + "\n최신버전 : " + self.lastver)
            self.WEBLINK(self.lastdownload)
            sys.exit(0)
        
        #로그기록
        #self.TOOL_LOGFILE()

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
        self.kuf_start.clicked.connect(lambda: self.OPENFILE('"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Phantagram\\Kingdom Under Fire\\Kingdom Under Fire.lnk"'))

    # 나의 랭킹 출력
    def UPDATE_MYRANK(self):
        try:      
            self.target = self.kuf_worksheet_rank.find(self.global_nikname.text())
        
            self.loadwin = self.kuf_worksheet_rank.cell(self.target.row,self.target.col+1).value
            self.loadlose = self.kuf_worksheet_rank.cell(self.target.row,self.target.col+2).value
            self.loadper = self.kuf_worksheet_rank.cell(self.target.row,self.target.col+3).value
            self.loadrate = self.kuf_worksheet_rank.cell(self.target.row,self.target.col+4).value
            self.loadrank = self.kuf_worksheet_rank.cell(self.target.row,self.target.col+5).value
            self.loadgrade = self.kuf_worksheet_rank.cell(self.target.row,self.target.col+6).value
        
            self.loadlabel = "현재순위 : " + self.loadrank + " | 닉네임 : " + self.target.value + " | 랭크 :" + self.loadgrade + "("+self.loadrate+") | 전적 :" + self.loadwin + "승"+ self.loadlose + "패("+ self.loadper +")"
            print("출력",self.loadlabel)
            self.kuf_myrank.setText(str(self.loadlabel))
        except:
            print("유저가 등록이 안되어있습니다.")


        

    def TEST(self):
        #self.lastver =self.admin_worksheet_admintool.cell(2,3).value
        #self.admin_worksheet_admintool.update_cell(1,1,"하이")
        if self.nonikchk == 1 :
            self.admin_worksheet_tooluser.append_row([self.myip, self.global_nikname.text()])
        
        #닉네임을 바꾼 경우
        try:
            if self.global_nikname.text() != self.loadnikname :
                print("닉네임을 변경함")
                self.admin_worksheet_tooluser.update_cell(self.loadip.row,self.loadip.col+1,self.global_nikname.text())
        except:
            print("종료시 메시지입니다.")

    def TOOL_LOGFILE(self):
        f = open("rts_rk.log", 'a')
        data = "서네떡입니다. \n"
        f.write(data)
        f.close()

    def OPENFILE(self, filepath):
        os.system(filepath)

    def GOOGLESHEET(self):
        self.scope = [
                    'https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive',
                    ]
        self.json_file_name = 'C:\\Users\\seo\\Downloads\\mobile-master\\python\\kufrankingsystem-281378b273ea.json'
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.json_file_name, self.scope)
        self.gc = gspread.authorize(self.credentials)
        self.admin_sheeturl = 'https://docs.google.com/spreadsheets/d/17NHDVM_sLCN_SSHr6NJsYRlg_XuZeevDpdaGZBMlSkY/edit#gid=0'
        self.kuf_spreadsheeturl = 'https://docs.google.com/spreadsheets/d/1Dy-9UaCfiKm5hv_dpv7EvpMoGe6LjAVHqvgsWYSmG8c/edit#gid=0'
        # 스프레스시트 문서 가져오기
        self.admindoc=  self.gc.open_by_url('https://docs.google.com/spreadsheets/d/17NHDVM_sLCN_SSHr6NJsYRlg_XuZeevDpdaGZBMlSkY/edit#gid=0')
        self.admin_worksheet_admintool = self.admindoc.worksheet('관리자도구')
        self.admin_worksheet_toolconn = self.admindoc.worksheet('런처접속자현황')
        self.admin_worksheet_tooluser = self.admindoc.worksheet('런처사용자')

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

    #유저확인
    def FIND_USER(self,username):
        #self.checkusername=self.kuf_myname.text()
        self.checkusername = username
        self.kuf_userlist = self.kuf_worksheet_rank.range('A2:A100')
        self.cnt = 0
        self.chk = 0
        for self.user in self.kuf_userlist:
            #print("검색중" , self.cnt,self.user,self.checkusername)
            
            if ( self.user.value == self.checkusername):
                print("찾았음 : ", self.user.value, self.checkusername)
                self.chk = 1
                break
            else:
                print("유저 없음", self.chk)
            self.cnt+=1
        #print("검색 끝")

        if(self.chk == 0):
            print(type(self.checkusername))
            #self.kuf_worksheet_rank.append_row([self.checkusername,'','','',1500])
            self.cell_list = self.kuf_worksheet_rank.range('A2:A1000') #유저 리스트 범위 지정
            for self.cell in self.cell_list: # 유저 리스트 반복문
                if self.cell.value == '':
                    print("유저 최초 등록 : ",self.checkusername)
                    self.kuf_worksheet_rank.update_cell(self.cell.row,1, self.checkusername)
                    self.kuf_worksheet_rank.update_cell(self.cell.row,5, 1500)
                    break
            print("패배")
            print("사용자 추가")
        else:
            print("이미 있는 사용자입니다. : ",self.chk)
        


    def RANK_UPDATE(self, game, myrace, myname,yourname, yourace, gamemap,outcome) :
        #ragistry user
        self.FIND_USER(myname)
        self.FIND_USER(yourname)

        # if outcome == True :
        # find before rating point
        self.findmyname = self.kuf_worksheet_rank.find(myname)
        self.myrating = self.kuf_worksheet_rank.cell(self.findmyname.row, self.findmyname.col+4).value
        self.findyourname = self.kuf_worksheet_rank.find(yourname)
        self.yourating = self.kuf_worksheet_rank.cell(self.findyourname.row, self.findyourname.col+4).value
        # Calculate after rating
        self.aftermyrating= float(self.myrating)+64*(1-1/(1+10**((float(self.yourating)-float(self.myrating))/400)))  
        self.afteryourating = float(self.yourating)+32*(0-1/(1+10**((float(self.myrating)-float(self.yourating))/400)))
        self.fluctmyrating= float(self.aftermyrating) - float(self.myrating)
        self.fluctyourating= float(self.afteryourating) - float(self.yourating)

        #print("나의 이전레이팅",self.myrating,"이후레이팅:",int(self.aftermyrating))
        #print("레이팅은 %s행%s열" % (self.findmyname.row, self.findmyname.col+4))

            
        #self.kuf_worksheet_history.append_row([' ',self.today, gamemap,self.myrating, myrace, myname, yourname, yourace, self.yourating, self.fluctmyrating, self.aftermyrating, self.afteryourating, self.fluctyourating])
        #print("업데이트할 현재레이팅위치", self.findmyname.row, self.findmyname.col+4,'E'+str(self.findmyname.row) )
        #self.kuf_worksheet_history.update_cell(행,열,'=SUM(1+1)')
        
        if outcome == True :
            #check , is update row line emty?
            #print("중요한 시간!")
            self.cell_list = self.kuf_worksheet_history.range('B4:B1000') #히스토리삽입 할 곳 범위지넝
            for self.cell in self.cell_list: # 맵리스트 출력
                if self.cell.value == '':
                    print("승자전적 처리중")
                    self.kuf_worksheet_history.update_cell(self.cell.row,2, self.today)
                    self.kuf_worksheet_history.update_cell(self.cell.row,3, gamemap)
                    self.kuf_worksheet_history.update_cell(self.cell.row,4, self.myrating)
                    self.kuf_worksheet_history.update_cell(self.cell.row,5, myrace)
                    self.kuf_worksheet_history.update_cell(self.cell.row,6, myname)
                    self.kuf_worksheet_history.update_cell(self.cell.row,7, yourname)
                    self.kuf_worksheet_history.update_cell(self.cell.row,8, yourace)
                    self.kuf_worksheet_history.update_cell(self.cell.row,9, self.yourating)
                    self.kuf_worksheet_history.update_cell(self.cell.row,10, self.fluctmyrating)
                    self.kuf_worksheet_history.update_cell(self.cell.row,11, self.aftermyrating)
                    self.kuf_worksheet_history.update_cell(self.cell.row,12, self.afteryourating)
                    self.kuf_worksheet_history.update_cell(self.cell.row,13, self.fluctyourating)
                    break

            print("승리")
        elif outcome == False :
            #self.kuf_worksheet_history.append_row(['',self.today, gamemap, self.yourating, yourace, yourname, myname, myrace, self.myrating, self.fluctyourating, self.afteryourating, self.aftermyrating, self.fluctmyrating])
            self.cell_list = self.kuf_worksheet_history.range('B4:B1000') #히스토리삽입 할 곳 범위지넝
            for self.cell in self.cell_list: # 맵리스트 출력
                if self.cell.value == '':
                    self.aftermyrating1= float(self.yourating)+64*(1-1/(1+10**((float(self.myrating)-float(self.yourating))/400)))  
                    self.afteryourating1 = float(self.myrating)+32*(0-1/(1+10**((float(self.yourating)-float(self.myrating))/400)))
                    self.fluctmyrating1= float(self.afteryourating1) - float(self.yourating)
                    self.fluctyourating1= float(self.aftermyrating1) - float(self.myrating)
                    
                    print("패자전적 처리중")
                    self.kuf_worksheet_history.update_cell(self.cell.row,2, self.today)
                    self.kuf_worksheet_history.update_cell(self.cell.row,3, gamemap)
                    self.kuf_worksheet_history.update_cell(self.cell.row,4, self.yourating)
                    self.kuf_worksheet_history.update_cell(self.cell.row,5, yourace)
                    self.kuf_worksheet_history.update_cell(self.cell.row,6, yourname)
                    self.kuf_worksheet_history.update_cell(self.cell.row,7, myname)
                    self.kuf_worksheet_history.update_cell(self.cell.row,8, myrace)
                    self.kuf_worksheet_history.update_cell(self.cell.row,9, self.myrating)
                    self.kuf_worksheet_history.update_cell(self.cell.row,10, self.fluctyourating1)

                    self.kuf_worksheet_history.update_cell(self.cell.row,11, self.aftermyrating1)

                    self.kuf_worksheet_history.update_cell(self.cell.row,12, self.afteryourating1)
                    self.kuf_worksheet_history.update_cell(self.cell.row,13, self.fluctmyrating1)
                    break
            print("패배")

        #update current rating info
        self.kuf_worksheet_rank.update_cell(self.findmyname.row, 2, "=COUNTIF('전적히스토리'!F:F," +'"' + myname + '")')#승자 승리횟수
        self.kuf_worksheet_rank.update_cell(self.findmyname.row, 3, "=COUNTIF('전적히스토리'!G:G," +'"' + myname + '")')#승자 패배횟수
        self.kuf_worksheet_rank.update_cell(self.findmyname.row, 4, '=IFERROR(B'+ str(self.findmyname.row) + '/(B' + str(self.findmyname.row) + '+C' + str(self.findmyname.row) + '),"")') #승자 승률
        self.kuf_worksheet_rank.update_cell(str(self.findmyname.row),5, self.aftermyrating) #승자 승리후 레이팅
        self.kuf_worksheet_rank.update_cell(str(self.findmyname.row), 6, '=RANK(E' + str(self.findmyname.row) + ',E:E,0)') #승자 순위
        
        self.grade = 'IF(F' + str(self.findmyname.row) + '/COUNTA(A$2:A)*100'
        self.gradeformula = '=' + self.grade + '< 16,"S", ' + self.grade + ' < 30,"A", ' + self.grade + ' < 44,"B", ' + self.grade + ' < 59,"C", ' +  self.grade + ' < 72,"D", ' +  self.grade + ' < 86,"E", "F"))))))'
        self.kuf_worksheet_rank.update_cell(self.findmyname.row, 7, self.gradeformula) #랭크

        #self.kuf_worksheet_rank.cell(self.findmyname.row,4, )
        self.tabname1="'전적히스토리'!F:F,\""
        self.tabname2="\",'전적히스토리'!E:E,"
        self.tabname3="'전적히스토리'!G:G,\""
        self.tabname4="\",'전적히스토리'!H:H,"
        self.race1 = '=IFERROR(round(COUNTIFS(' + self.tabname1 + self.findmyname.value + self.tabname2 + '"휴먼")/(COUNTIFS(' +  self.tabname1 + self.findmyname.value + self.tabname2 + '"휴먼")+COUNTIFS(' + self.tabname3 + self.findmyname.value + self.tabname4 + '"휴먼")),4),0)'
        self.kuf_worksheet_rank.update_cell(self.findmyname.row,8,self.race1) #종족1 승률
        
        self.race2 = '=IFERROR(round(COUNTIFS(' + self.tabname1 + self.findmyname.value + self.tabname2 + '"데빌")/(COUNTIFS(' +  self.tabname1 + self.findmyname.value + self.tabname2 + '"데빌")+COUNTIFS(' + self.tabname3 + self.findmyname.value + self.tabname4 + '"데빌")),4),0)'
        self.kuf_worksheet_rank.update_cell(self.findmyname.row,9,self.race2)# 종족2 승률




        self.kuf_worksheet_rank.update('E'+str(self.findyourname.row), self.afteryourating) #패자 승리후 레이팅
        self.kuf_worksheet_rank.update_cell(self.findyourname.row, 2, "=COUNTIF('전적히스토리'!F:F," +'"' + yourname + '")')#패자 승리횟수
        self.kuf_worksheet_rank.update_cell(self.findyourname.row, 3, "=COUNTIF('전적히스토리'!G:G," +'"' + yourname + '")')#패자 패배횟수
        self.kuf_worksheet_rank.update_cell(self.findyourname.row, 4, '=IFERROR(B'+ str(self.findyourname.row) + '/(B' + str(self.findyourname.row) + '+C' + str(self.findyourname.row) + '),"")') #승자 승률
        self.kuf_worksheet_rank.update_cell(str(self.findyourname.row),5, self.afteryourating) #패자 승리후 레이팅
        self.kuf_worksheet_rank.update_cell(str(self.findyourname.row), 6, '=RANK(E' + str(self.findyourname.row) + ',E:E,0)') #패자 순위
        
        self.grade = 'IF(F' + str(self.findyourname.row) + '/COUNTA(A$2:A)*100'
        self.gradeformula = '=' + self.grade + '< 16,"S", ' + self.grade + ' < 30,"A", ' + self.grade + ' < 44,"B", ' + self.grade + ' < 59,"C", ' +  self.grade + ' < 72,"D", ' +  self.grade + ' < 86,"E", "F"))))))'
        self.kuf_worksheet_rank.update_cell(self.findyourname.row, 7, self.gradeformula) #랭크

        self.race1 = '=IFERROR(round(COUNTIFS(' + self.tabname1 + self.findyourname.value + self.tabname2 + '"휴먼")/(COUNTIFS(' +  self.tabname1 + self.findyourname.value + self.tabname2 + '"휴먼")+COUNTIFS(' + self.tabname3 + self.findyourname.value + self.tabname4 + '"휴먼")),4),0)'
        self.kuf_worksheet_rank.update_cell(self.findyourname.row,8,self.race1) #패자 종족1 승률
        
        self.race2 = '=IFERROR(round(COUNTIFS(' + self.tabname1 + self.findyourname.value + self.tabname2 + '"데빌")/(COUNTIFS(' +  self.tabname1 + self.findyourname.value + self.tabname2 + '"데빌")+COUNTIFS(' + self.tabname3 + self.findyourname.value + self.tabname4 + '"데빌")),4),0)'
        self.kuf_worksheet_rank.update_cell(self.findyourname.row,9,self.race2)# 패자 종족2 승률

        self.UPDATE_MYRANK()
        QMessageBox.about(self,"전적기록","기록정상 종료")

        print("기록 정상 종료")

        

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
            self.jurrasic_frame.setGeometry(250, 65, 491, 401)
    def KUF_FRAME(self) :
            print("킹덤언더파이어")
            self.kuf_frame.setGeometry(250, 65, 491, 401)
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
        self.imjinrok_frame.setGeometry(250, 65, 491, 401)
        self.atrox_frame.setGeometry(250, 65, 491, 1)
        self.jurrasic_frame.setGeometry(250, 65, 491, 1)
    def NEWMYTH_FRAME(self) :
        print("신천년의신화")
        self.kuf_frame.setGeometry(250, 65, 491, 1)
        self.mirror_frame.setGeometry(250, 65, 491, 1)
        self.newmyth_frame.setGeometry(250, 65, 491, 401)
        self.imjinrok_frame.setGeometry(250, 65, 491, 1)
        self.atrox_frame.setGeometry(250, 65, 491, 1)
        self.jurrasic_frame.setGeometry(250, 65, 491, 1)
    def MIRRORWAR_FRAME(self) :
        print("거울전쟁")
        self.kuf_frame.setGeometry(250, 65, 491, 1)
        self.mirror_frame.setGeometry(250, 65, 491, 401)
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
        self.atrox_frame.setGeometry(250, 65, 491, 401)
        self.jurrasic_frame.setGeometry(250, 65, 491, 1)
    
    
    
    


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit(myWindow.TEST())