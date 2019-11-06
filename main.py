import gspread
from oauth2client.service_account import ServiceAccountCredentials
#https://gspread.readthedocs.io/en/latest/

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'hip-host-262902-5bd9ba44ee67.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("domainTest").sheet1

# wks.update_acell('B2', "it's down there somewhere, let me take another look.")
val = wks.cell(2, 2).value

print(val)
 
