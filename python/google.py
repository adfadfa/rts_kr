import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'C:\\Users\seo\python\kufrankingsystem-281378b273ea.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1Dy-9UaCfiKm5hv_dpv7EvpMoGe6LjAVHqvgsWYSmG8c/edit#gid=0'
# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('Sheet1')

cell_data = worksheet.acell('B1').value
print(cell_data)

worksheet.append_row(['new1', 'new2', 'new3', 'new4'])


