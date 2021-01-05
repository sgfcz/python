import requests
import pymongo

client = pymongo.MongoClient('localhost',27017)
book_weather = client['weather']
sheet_weather = book_weather['sheet_weather_3']

url = " http://cdn.heweather.com/china-city-list.txt"
strhtml = requests.get(url)
strhtml.encoding='utf-8'
data = strhtml.text
data1 = data.split("\n")
for i in range(6):
    data1.remove(data1[0])
for item in data1[0:10]:
    url='https://free-api.heweather.net/s6' \
        '/weather/forecast?location='+ item[2:14] +\
        '&key=509ff55cddc6407592f28f3fa3c80bf6'
    strhtml=requests.get(url)
    dic=strhtml.json()
    sheet_weather.insert_one(dic)
