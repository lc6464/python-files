from time import sleep
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from accdb import *
c_op = Options()
c_op.add_experimental_option("debuggerAddress", "127.0.0.1:20046")
dr = webdriver.Chrome(options=c_op)
def getInfo(dri=dr):
    d={}
    e=dri.find_elements_by_css_selector(".alarm-item a")
    for i in e:
        info=i.text
        link=i.get_attribute("href")
        info[:info.find('气象台')]+'-'+info[info.find('发布')+2:len(info)-4]
        d[info]=link
    return d

dr.get('http://www.nmc.cn/f/alarm.html')
sleep(0.3)
page=[]
for i in range(0,15):
    page.append(getInfo())
    dr.find_element_by_css_selector(".next").click()
    sleep(0.7)
