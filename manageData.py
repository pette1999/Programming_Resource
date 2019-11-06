import gspread
import authentication

json_file_name = 'hip-host-262902-5bd9ba44ee67.json'
credential = authentication.authenticate(json_file_name)
gc = gspread.authorize(credential)
wks = gc.open("domainTest").sheet1

# get value from a cell
# row,column
val = wks.cell(1,2).value

# get values from a volumn
values_list = wks.col_values(1)

count = 0
for i in values_list:
    count += 1
    print(count , " ", i)
