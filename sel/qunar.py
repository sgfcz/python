import random
import time
import urllib
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()
#driver.get("https://fh.dujia.qunar.com/?tf=package")
#WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID, "depCity")))

def get_url(url):
    time.sleep(1)
    return(requests.get(url))
if __name__=="__main__":
    driver = webdriver.Chrome()

    #出发地城市列表
    dep_cities = ["武汉"]
    for dep in dep_cities:
       # strhtml = get_url('https://touch.dujia.qunar.com/golfz/sight/arriveRecommend?dep=' +
                  #        urllib.request.quote(dep) + '&extensionImg=255,175')
       # arrive_dict = strhtml.json()

        #得到城市dict
        #for arrive_item in arrive_dict['data']:
            #for arrive_item_1 in arrive_item['subModules']:
                #for query in arrive_item_1['items']:
        driver.get("https://fh.dujia.qunar.com/?tf=package")
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "depCity")))
        #清空出发文本
        driver.find_element_by_xpath("//*[@id='depCity']").clear()
        #将出发地写进去
        driver.find_element_by_xpath("//*[@id='depCity']").send_keys(dep)
        #将目的地写进去
        driver.find_element_by_xpath("//*[@id='arrCity']").send_keys("三亚")
        #点击【开始定制】按钮
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/a").click()
        print("dep:%s arr:%s" % (dep,"三亚"))

        #最多抓两页
        for i in range(2):
            time.sleep(random.uniform(5,6))

            routes = driver.find_elements_by_xpath('//*[@id="list"]/div')
            for route in routes:
                resule = {
                    'date' : time.strftime('%y-%m-%d', time.localtime(time.time())),
                    'dep':dep,
                    'arrive': "三亚",
                    'resule': route.text
                }
                print(resule)
            if i < 9:
                btns = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[7]/div/div/a[7]')
                for a in btns:
                    if a.text == u"下一页":
                        a.click()
                        break
driver.close()