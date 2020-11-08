# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtGui import QIcon 

from urllib.request import urlopen
from gzip import decompress
from json import loads
from urllib.parse import quote

def get_weather_data(cityName) :
    #city_name = input('请输入要查询的城市名称：')
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+quote(cityName)
    weather_data = urlopen(url).read()
    #读取网页数据
    weather_data = decompress(weather_data).decode()
    #解压网页数据
    weather_dict = loads(weather_data)
    #将json数据转换为dict数据
    return weather_dict

def show_weather(weather_data,m4Days):
    weather_dict = weather_data 
    #将json数据转换为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        weather_str='您输入的城市名有误，或者天气中心未收录您所在城市！'
    elif weather_dict.get('desc') =='OK':
        forecast = weather_dict.get('data').get('forecast')
        weather_str='您输入的城市：'+weather_dict.get('data').get('city')+'\n'
        weather_str=weather_str + '温度：' + weather_dict.get('data').get('wendu')+'℃ '+'\n'
        weather_str=weather_str + '感冒概率：' + weather_dict.get('data').get('ganmao') +'\n'
        weather_str=weather_str + '风向（风吹来的方向）：'+forecast[0].get('fengxiang')+'\n'
        wind_level=forecast[0].get('fengli')
        tailor_str=wind_level[wind_level.index('[CDATA[')+7:wind_level.index(']]')]
        weather_str=weather_str + '风级：'+tailor_str+'\n'
        weather_str=weather_str + '最高温度：'+forecast[0].get('high')+'\n'
        weather_str=weather_str.replace("高温 ",'')
        weather_str=weather_str + '最低温度：'+forecast[0].get('low')+'\n'
        weather_str=weather_str.replace("低温 ",'')
        weather_str=weather_str + '天气：'+forecast[0].get('type')+'\n'
        weather_str=weather_str + '今天是 '+forecast[0].get('date')+'\n'
        weather_str=weather_str + '**********************************************'+'\n'
        if m4Days==1:
            for i in range(1,5):
                weather_str=weather_str +'日期：'+forecast[i].get('date')+'\n'
                weather_str=weather_str +'风向（风吹来的方向）：'+forecast[i].get('fengxiang')+'\n'
                wind_level=forecast[i].get('fengli')
                tailor_str=wind_level[wind_level.index('[CDATA[')+7:wind_level.index(']]')]
                weather_str=weather_str +'风级：'+tailor_str+'\n'
                weather_str=weather_str + '最高温度：'+forecast[0].get('high')+'\n'
                weather_str=weather_str.replace("高温 ",'')
                weather_str=weather_str + '最低温度：'+forecast[0].get('low')+'\n'
                weather_str=weather_str.replace("低温 ",'')
                weather_str=weather_str +'天气：'+forecast[i].get('type')+'\n'
                weather_str=weather_str +'--------------------------'+'\n'
    return weather_str

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(423, 691)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 60, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(230, 60, 121, 31))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setObjectName("checkBox")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 100, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(0, 0, 549, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(10, 220, 401, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setReadOnly(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 240, 401, 441))
        self.textEdit.setObjectName("textEdit")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 110, 401, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CitypushButton01 = QtWidgets.QPushButton(self.widget)
        self.CitypushButton01.setObjectName("CitypushButton01")
        self.horizontalLayout_3.addWidget(self.CitypushButton01)
        self.CitypushButton02 = QtWidgets.QPushButton(self.widget)
        self.CitypushButton02.setObjectName("CitypushButton02")
        self.horizontalLayout_3.addWidget(self.CitypushButton02)
        self.CitypushButton03 = QtWidgets.QPushButton(self.widget)
        self.CitypushButton03.setObjectName("CitypushButton03")
        self.horizontalLayout_3.addWidget(self.CitypushButton03)
        self.CitypushButton04 = QtWidgets.QPushButton(self.widget)
        self.CitypushButton04.setObjectName("CitypushButton04")
        self.horizontalLayout_3.addWidget(self.CitypushButton04)
        self.CitypushButton05 = QtWidgets.QPushButton(self.widget)
        self.CitypushButton05.setObjectName("CitypushButton05")
        self.horizontalLayout_3.addWidget(self.CitypushButton05)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 140, 401, 26))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CitypushButton06 = QtWidgets.QPushButton(self.widget1)
        self.CitypushButton06.setObjectName("CitypushButton06")
        self.horizontalLayout_4.addWidget(self.CitypushButton06)
        self.CitypushButton07 = QtWidgets.QPushButton(self.widget1)
        self.CitypushButton07.setObjectName("CitypushButton07")
        self.horizontalLayout_4.addWidget(self.CitypushButton07)
        self.CitypushButton08 = QtWidgets.QPushButton(self.widget1)
        self.CitypushButton08.setObjectName("CitypushButton08")
        self.horizontalLayout_4.addWidget(self.CitypushButton08)
        self.CitypushButton09 = QtWidgets.QPushButton(self.widget1)
        self.CitypushButton09.setObjectName("CitypushButton09")
        self.horizontalLayout_4.addWidget(self.CitypushButton09)
        self.CitypushButton10 = QtWidgets.QPushButton(self.widget1)
        self.CitypushButton10.setObjectName("CitypushButton10")
        self.horizontalLayout_4.addWidget(self.CitypushButton10)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(10, 170, 401, 26))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.CitypushButton11 = QtWidgets.QPushButton(self.widget2)
        self.CitypushButton11.setObjectName("CitypushButton11")
        self.horizontalLayout_5.addWidget(self.CitypushButton11)
        self.CitypushButton12 = QtWidgets.QPushButton(self.widget2)
        self.CitypushButton12.setObjectName("CitypushButton12")
        self.horizontalLayout_5.addWidget(self.CitypushButton12)
        self.CitypushButton13 = QtWidgets.QPushButton(self.widget2)
        self.CitypushButton13.setObjectName("CitypushButton13")
        self.horizontalLayout_5.addWidget(self.CitypushButton13)
        self.CitypushButton14 = QtWidgets.QPushButton(self.widget2)
        self.CitypushButton14.setObjectName("CitypushButton14")
        self.horizontalLayout_5.addWidget(self.CitypushButton14)
        self.CitypushButton15 = QtWidgets.QPushButton(self.widget2)
        self.CitypushButton15.setObjectName("CitypushButton15")
        self.horizontalLayout_5.addWidget(self.CitypushButton15)
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(10, 200, 401, 26))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.CitypushButton16 = QtWidgets.QPushButton(self.widget3)
        self.CitypushButton16.setObjectName("CitypushButton16")
        self.horizontalLayout_6.addWidget(self.CitypushButton16)
        self.CitypushButton17 = QtWidgets.QPushButton(self.widget3)
        self.CitypushButton17.setObjectName("CitypushButton17")
        self.horizontalLayout_6.addWidget(self.CitypushButton17)
        self.CitypushButton18 = QtWidgets.QPushButton(self.widget3)
        self.CitypushButton18.setObjectName("CitypushButton18")
        self.horizontalLayout_6.addWidget(self.CitypushButton18)
        self.CitypushButton19 = QtWidgets.QPushButton(self.widget3)
        self.CitypushButton19.setObjectName("CitypushButton19")
        self.horizontalLayout_6.addWidget(self.CitypushButton19)
        self.CitypushButton20 = QtWidgets.QPushButton(self.widget3)
        self.CitypushButton20.setObjectName("CitypushButton20")
        self.horizontalLayout_6.addWidget(self.CitypushButton20)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "天气查询"))
        self.label.setText(_translate("Form", "请输入城市名称或选择下方城市："))
        self.pushButton.setText(_translate("Form", "查询"))
        self.checkBox.setText(_translate("Form", "未来四天天气"))
        self.CitypushButton01.setText(_translate("Form", "北京"))
        self.CitypushButton02.setText(_translate("Form", "上海"))
        self.CitypushButton03.setText(_translate("Form", "广州"))
        self.CitypushButton04.setText(_translate("Form", "南京"))
        self.CitypushButton05.setText(_translate("Form", "西安"))
        self.CitypushButton06.setText(_translate("Form", "成都"))
        self.CitypushButton07.setText(_translate("Form", "武汉"))
        self.CitypushButton08.setText(_translate("Form", "合肥"))
        self.CitypushButton09.setText(_translate("Form", "石家庄"))
        self.CitypushButton10.setText(_translate("Form", "天津"))
        self.CitypushButton11.setText(_translate("Form", "郑州"))
        self.CitypushButton12.setText(_translate("Form", "重庆"))
        self.CitypushButton13.setText(_translate("Form", "乌鲁木齐"))
        self.CitypushButton14.setText(_translate("Form", "深圳"))
        self.CitypushButton15.setText(_translate("Form", "洛阳"))
        self.CitypushButton16.setText(_translate("Form", "济南"))
        self.CitypushButton17.setText(_translate("Form", "杭州"))
        self.CitypushButton18.setText(_translate("Form", "长沙"))
        self.CitypushButton19.setText(_translate("Form", "哈尔滨"))
        self.CitypushButton20.setText(_translate("Form", "龙川"))

class myWeather(QDialog, Ui_Form):
    global m4Days
    global mStr
    global mCityStr
    def __init__(self,parent=None):  
        super(myWeather,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('Mostly Sunny.ico'))
        self.checkBox.stateChanged.connect(self.checkboxstate)
        self.CitypushButton01.clicked.connect(lambda: self.hotcity(1))
        self.CitypushButton02.clicked.connect(lambda: self.hotcity(2))
        self.CitypushButton03.clicked.connect(lambda: self.hotcity(3))
        self.CitypushButton04.clicked.connect(lambda: self.hotcity(4))
        self.CitypushButton05.clicked.connect(lambda: self.hotcity(5))
        self.CitypushButton06.clicked.connect(lambda: self.hotcity(6))
        self.CitypushButton07.clicked.connect(lambda: self.hotcity(7))
        self.CitypushButton08.clicked.connect(lambda: self.hotcity(8))
        self.CitypushButton09.clicked.connect(lambda: self.hotcity(9))
        self.CitypushButton10.clicked.connect(lambda: self.hotcity(10))
        self.CitypushButton11.clicked.connect(lambda: self.hotcity(11))
        self.CitypushButton12.clicked.connect(lambda: self.hotcity(12))
        self.CitypushButton13.clicked.connect(lambda: self.hotcity(13))
        self.CitypushButton14.clicked.connect(lambda: self.hotcity(14))
        self.CitypushButton15.clicked.connect(lambda: self.hotcity(15))
        self.CitypushButton16.clicked.connect(lambda: self.hotcity(16))
        self.CitypushButton17.clicked.connect(lambda: self.hotcity(17))
        self.CitypushButton18.clicked.connect(lambda: self.hotcity(18))
        self.CitypushButton19.clicked.connect(lambda: self.hotcity(19))
        self.CitypushButton20.clicked.connect(lambda: self.hotcity(20))

        self.pushButton.clicked.connect(self.checkWeather)


    def checkboxstate(self,state):
        global m4Days
        if(state==QtCore.Qt.Unchecked):
            m4Days=0
        else:
            m4Days=1
        #print ('Check Box state=', m4Days)

    def hotcity(self,n):

        if (n==1):
          cityName=self.CitypushButton01.text()
          self.lineEdit.setText(cityName)
        elif (n==2):
          cityName=self.CitypushButton02.text()
          self.lineEdit.setText(cityName)
        elif (n==3):
          cityName=self.CitypushButton03.text()
          self.lineEdit.setText(cityName)
        elif (n==4):
          cityName=self.CitypushButton04.text()
          self.lineEdit.setText(cityName)
        elif (n==5):
          cityName=self.CitypushButton05.text()
          self.lineEdit.setText(cityName)
        elif (n==6):
          cityName=self.CitypushButton06.text()
          self.lineEdit.setText(cityName)
        elif (n==7):
          cityName=self.CitypushButton07.text()
          self.lineEdit.setText(cityName)
        elif (n==8):
          cityName=self.CitypushButton08.text()
          self.lineEdit.setText(cityName)
        elif (n==9):
          cityName=self.CitypushButton09.text()
          self.lineEdit.setText(cityName)
        elif (n==10):
          cityName=self.CitypushButton10.text()
          self.lineEdit.setText(cityName)
        elif (n==11):
          cityName=self.CitypushButton11.text()
          self.lineEdit.setText(cityName)
        elif (n==12):
          cityName=self.CitypushButton12.text()
          self.lineEdit.setText(cityName)
        elif (n==13):
          cityName=self.CitypushButton13.text()
          self.lineEdit.setText(cityName)
        elif (n==14):
          cityName=self.CitypushButton14.text()
          self.lineEdit.setText(cityName)
        elif (n==15):
          cityName=self.CitypushButton15.text()
          self.lineEdit.setText(cityName)
        elif (n==16):
          cityName=self.CitypushButton16.text()
          self.lineEdit.setText(cityName)
        elif (n==17):
          cityName=self.CitypushButton17.text()
          self.lineEdit.setText(cityName)
        elif (n==18):
          cityName=self.CitypushButton18.text()
          self.lineEdit.setText(cityName)
        elif (n==19):
          cityName=self.CitypushButton19.text()
          self.lineEdit.setText(cityName)
        elif (n==20):
          cityName=self.CitypushButton20.text()
          self.lineEdit.setText(cityName)
        else:
          self.textEdit.setText('城市名称错误！')


    def checkWeather(self):
        global m4Days
        cityName=self.lineEdit.text()
        mStr=show_weather(get_weather_data(cityName),m4Days)
        self.textEdit.setText(mStr)





if __name__=="__main__":  
    import sys  
    global m4Days

    m4Days=0

    app=QApplication(sys.argv)  
    myshow=myWeather()  
    myshow.show()  
    sys.exit(app.exec_()) 
