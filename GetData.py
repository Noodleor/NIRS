import requests
import time
import json
from datetime import datetime


#def to_date(unix_time):
#    unix = int(unix_time)+10800
#    dttime = datetime.utcfromtimestamp(unix).strftime('%m') #('%d.%m.%Y %H:%M:%S')
#    return(dttime)

def to_unix(dttime):
    year = int(dttime[0:4])
    month = int(dttime[5:7])
    day = int(dttime[8:10])
    hour = int(dttime[11:13])
    minutes = int(dttime[14:16])
    seconds = int(dttime[17:19])
    try:
        dttime = datetime(year, month, day, hour, minutes, seconds)  # 1970-01-01 05:30:00 2020-01-01 10:00:00
    except ValueError:
        exit(-1)
    unix = (time.mktime(dttime.timetuple()))
    #print(unix)
    return(int(unix))

#url = 'https://api.bcs.ru/udfdatafeed/v1/history?symbol=SBER&classcode=TQBR&resolution=60&from=1682671341&to=1682947667'
#'https://api.bcs.ru/udfdatafeed/v1/history?symbol=TSLA&classcode=SPBXM&resolution=1&from=1683098951&to=1683126735'
#'https://api.bcs.ru/udfdatafeed/v1/history?symbol=GAZP&classcode=TQBR&resolution=60&from=1683021989&to=1683057989'

#2023-06-05 10:00:00

stock_code = input('Input stock code: ')       #TSLA  SBER  GAZP  VTBR
exchange_code = input('Input exchange code: ') #SPBXM TQBR  TQBR
resolution = input('Input resolution: ') #60 supported_resolutions: "1", "5", "15", "30", "60", "1D"= D, "1W"= D, "1M"= D
start_count_time = str(to_unix(input('Input start count time: '))) # input('Input start count time: ')
end_count_time = str(to_unix(input('Input end count time: ')))   # input('Input end count time: ')
custom_url = 'https://api.bcs.ru/udfdatafeed/v1/history?symbol=' + stock_code + '&classcode=' + exchange_code + '&resolution=' + resolution + '&from=' + start_count_time + '&to=' + end_count_time

if (requests.get(custom_url)):
    response = requests.get(custom_url)
else:
    exit(-2)
print(response)

json_text = json.loads(response.text)

scale = json_text['scale']
unix_time = json_text['t']
open_price = json_text['o']
close_price = json_text['c']
highest_price = json_text['h']
lowest_price = json_text['l']

# for i in range(len(unix_time)):
#     unix_time[i] = int(unix_time[i])/60/60/24
# print(unix_time[1], type(unix_time[1]))

#print(len(open_price), open_price[0::])
#print(len(close_price), close_price[0::])
#print(len(unix_time), unix_time[1::], unix_time[::1])

mid_price = []
for i in range(len(open_price)):
    mid_price.append((open_price[i]+close_price[i])/2)

