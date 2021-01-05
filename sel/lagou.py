import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def get_url(url):
    time.sleep(1)
    return(requests)

if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.lagou.com")
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,"search_input")))
    driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/ul/li[8]/a').click()
    inp = input("请输入职位：")
    #清空搜索框
    driver.find_element_by_xpath("//*[@id='search_input']").clear()
    #将东西写进去
    driver.find_element_by_xpath('//*[@id="search_input"]').send_keys(inp)
    #点击搜索
    driver.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[1]/form/input[5]").click()
    fileobj = open('zhiwei_data.json', 'w', encoding='utf-8')
    #开始抓取
    for i in range(5):
        fileobj.writelines("第{}页".format(i+1)+"\n")

        routes = driver.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
        for route in routes:
            str = route.text
            list = str.split("\n")
            resule = {
                '职位': list[0],
                "薪酬": list[3],
                "公司名称": list[4]
            }
            json_str = json.dumps(resule,ensure_ascii=False)
            fileobj.writelines(json_str + "\n")
        hb = driver.find_elements_by_xpath('/html/body/div[7]/div/div[2]')
        for a in hb:
          if a.text == u"给也不要":
              a.click()
        xye = driver.find_elements_by_xpath('/html/body/div[5]/div[2]/div[1]/div[3]/div[2]/div/span[6]')
        for a in xye:
            if a.text == u"下一页":
                a.click()
                time.sleep(5)
                break
fileobj.close()
driver.close()