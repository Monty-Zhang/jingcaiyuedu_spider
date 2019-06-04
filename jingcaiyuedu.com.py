
from selenium import webdriver

# 起始页面
url = 'http://www.jingcaiyuedu.com/novel/BaJoa2.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'Referer': 'http://jingcaiyuedu.com/novel/bDAfQ.html'}

browser = webdriver.Chrome()
browser.get(url)

links = browser.find_elements_by_xpath('//*[@class="panel panel-default hidden-xs"]/dl/dd/a')

urls = [l.get_attribute('href') for l in links]

with open(r'd:/my_pic/noval.txt', 'w') as f:

    for url in urls:
        browser.get(url)

        title = browser.find_element_by_class_name('readTitle').text
        content = browser.find_element_by_class_name('panel-body').text

        print('正在抓取：', url)

        f.write(title)
        f.write(content)
        f.write('\n')

