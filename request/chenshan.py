import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/72.0.3626.122 Safari/537.36 Vivaldi/2.3.1440.61'
}
url = "https://wenda.so.com/search/?q=衬衫&filt=20"
strhtml = requests.get(url, headers = headers)
soup = BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#js-qa-list > li > div.qa-i-hd > h3 > a')
print(data)
for item in data:
    dic = {
        'title': item.get_text()
    }
    print(dic)