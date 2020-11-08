from sfzhX import getX
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
c_op = Options()
c_op.add_experimental_option("debuggerAddress", "127.0.0.1:20046")
c_dr = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
dr = webdriver.Chrome(c_dr,options=c_op)
for i in range(0,1000,2):
    a=str(i)
    if i<10:
        a='00'+a
    elif i<100:
        a='0'+a
    a='11000020000101'+a
    a+=getX(a)
    print(i)
    sleep(0.3)
    dr.get('http://www.lcyzczb.com/cjcx/edut_student_1.asp?id=g'+a)
    sleep(0.7)
    try:
        dr.switch_to.alert.accept()
    except:
        if len(dr.find_elements_by_id('sname'))==1:
            if dr.find_element_by_id('sname').get_attribute('value')=='？？？':
                print(a)
                break
