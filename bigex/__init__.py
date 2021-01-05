import requests
import urllib
import pymongo
import time

client = pymongo.MongoClient('localhost',27017)
book_qunar = client['qunar']
sheet_qunar_zyx = book_qunar['qunar_zyx']

url = "https://touch.dujia.qunar.com/depCities.qunar"
strhtml = requests.get(url)
dep_dict = strhtml.json()

for dep_item in dep_dict['data']:
    for dep in dep_dict['data'][dep_item]:
        a = []
        print("departion:",dep)
        url = 'https://touch.dujia.qunar.com/golfz/sight/' \
              'arriveRecommend?dep={}&exclude=' \
              '&extensionImg=255,175'.format(urllib.request.quote(dep))
        strhtml = requests.get(url)
        arrive_dict = strhtml.json()
        for arr_item in arrive_dict['data']:
            for arr_item_1 in arr_item['subModules']:
                for query in arr_item_1['items']:
                    if query['query'] not in a:
                        a.append(query['query'])
        for item in a:
            print(item)
            url = "https://touch.dujia.qunar.com/list?modules=list%2CbookingInfo%2CactivityDetail" \
                  "&dep={}&query={}&dappDealTrace=true&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx" \
                  "&it=dujia_hy_destination&date=&needNoResult=true&originalquery={}&limit=0,24&includeAD=true&qsact=search".format(
                urllib.request.quote(dep),urllib.request.quote(item),urllib.request.quote(item))
            proxies = {
                          'http:':'http://61.135.217.7:80'
            }
            headers = {
                "user-agent" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML,likeGecko) Chrome/72.0.3626.122 Safari/537.36 Vivaldi/2.3.1440.61"
            }
            strhtml = requests.get(url,headers=headers,proxies=proxies)
            cookies = requests.utils.dict_from_cookiejar(strhtml.cookies)
            strhtml = requests.get(url,headers=headers,proxies=proxies,cookies=cookies)
            print(strhtml.text)

            try:
                routeCount = int(strhtml.json()['data']['limit']['routeCount'])
                print(routeCount)
            except:
                continue

            for limit in range(0,routeCount,20):
                url = "https://touch.dujia.qunar.com/list?modules=list%2CbookingInfo%2CactivityDetail" \
                  "&dep={}&query={}&dappDealTrace=true&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx" \
                  "&it=dujia_hy_destination&date=&needNoResult=true&originalquery={}&limit={},24&includeAD=true&qsact=search".format(
                urllib.request.quote(dep),urllib.request.quote(item),urllib.request.quote(item),limit)
                strhtml = requests.get(url, headers=headers, proxies=proxies)
                cookies = requests.utils.dict_from_cookiejar(strhtml.cookies)
                strhtml = requests.get(url, headers=headers, proxies=proxies, cookies=cookies)
                print(strhtml.text)
                result = {
                    'data' : time.strftime('%Y-%m-%d',time.localtime(time.time())),
                    'dep' :  dep,
                    'arrive' : item,
                    'limit' : limit,
                    'result' : strhtml.json()
                }
                sheet_qunar_zyx.insert_one(result)

