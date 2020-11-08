from urllib.request import urlopen
from urllib.parse import quote
from gzip import decompress
from json import loads
print('------天气查询------')
def get_weather_data() :
	city_name = input('请输入要查询的城市名称（直接敲回车则默认为龙川）：')
	if city_name == '':
		city_name = '龙川'
	url = 'http://wthrcdn.etouch.cn/weather_mini?city='+quote(city_name)
	weather_data = urlopen(url).read()
	#读取网页数据
	weather_data = decompress(weather_data).decode('utf-8')
	#解压网页数据
	weather_dict = loads(weather_data)
	#将json数据转换为dict数据
	return weather_dict

def show_weather(weather_data):
	weather_dict = weather_data
	if weather_dict.get('desc') == 'invilad-citykey':
		print('您输入的城市名有误，或者天气中心暂未收录您所在城市！')
	elif weather_dict.get('desc') =='OK':
		forecast = weather_dict.get('data').get('forecast')
		print('您输入的城市：',weather_dict.get('data').get('city'))
		print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
		print('感冒概率：',weather_dict.get('data').get('ganmao'))
		print('风向（风吹来的方向）：',forecast[0].get('fengxiang'))
		print('风级：',forecast[0].get('fengli')[9:forecast[0].get('fengli').find(']')])
		print('最高温度：',forecast[0].get('high')[3:])
		print('最低温度：',forecast[0].get('low')[3:])
		print('大致天气：',forecast[0].get('type'))
		print('当前日期：',forecast[0].get('date'))
		print('*******************************')
		four_day_forecast =input('是否要显示未来四天天气？输入“是”、大小写的“Y”、“Y”大小写的“Yes”均为显示，其它均为停止：')
		if four_day_forecast in ('是','Y','y','Yes','yes'):
			for i in range(1,5):
				print('--------------------------')
				print('日期：',forecast[i].get('date'))
				print('风向（风吹来的方向）：',forecast[i].get('fengxiang'))
				print('风级：',forecast[i].get('fengli')[9:forecast[i].get('fengli').find(']')])
				print('最高温度：',forecast[i].get('high')[3:])
				print('最低温度：',forecast[i].get('low')[3:])
				print('大致天气：',forecast[i].get('type'))
			print('***********************************')
if __name__=='__main__':
	show_weather(get_weather_data())
