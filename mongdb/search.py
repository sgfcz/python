﻿import pymongo

client = pymongo.MongoClient('localhost',27017)
book_weather = client['weather']
sheet_weather = book_weather['sheet_weather_3']

for item in sheet_weather.find():
    for i in range(3):
        try:
            tmp = item["HeWeather6"][0]['daily_forecast'][i]['tmp_max']
            sheet_weather.update_one({'_id':item['_id']},{'$set':
        {'HeWeather6.0.daily_forecast.{}.tmp_max'.format(i):int(tmp)}})
        except:
            continue
    for item in sheet_weather.find({'HeWeather6.daily_forecast.tmp_max':
                                        {'$gt':1}}):
        print(item['HeWeather6'][0]['basic']['location'])

