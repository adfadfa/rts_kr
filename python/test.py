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

self.GOOGLESHEET()