from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
c_op = Options()
c_op.add_experimental_option("debuggerAddress", "127.0.0.1:20046")
c_dr = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
dr = webdriver.Chrome(c_dr,options=c_op)
def getId():
    d={}
    dr.get('https://lcwebsite.cn/yzwebld')
    for i in sid:
        dr.find_element_by_id('sfzh').clear()
        dr.find_element_by_id('sfzh').send_keys(i)
        dr.find_element_by_id('gpsm').click()
        al=dr.switch_to.alert.text
        al=al[4:] if al[:4] == '密码是：' else '<#ERR:未获取到密码！#>'
        d[i]=al
        dr.switch_to.alert.accept()
    dr.find_element_by_id('sfzh').clear()
    dr.find_element_by_id('sfzh').click()
    return d

if __name__=='__main__':
    d=getPaw([])
    print(d)
