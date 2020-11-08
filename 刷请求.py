import urllib.request
import time

# 使用build_opener()是为了让python程序模仿浏览器进行访问
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40')]


# 专刷某个页面
print('开始刷了哦：')
tempUrl = 'http://www.lcyzczb.com/cjcx/edut_student_1.asp?id=g000000000000000000'


a = 0
def main():
	global a
	while True:
		try:
			r = opener.open(tempUrl).read().decode('gbk')[-58:] == '<script>alert("不存在该ID的学生");window.history.go(-1);</script>'
			print('%d %s %s' % (a, tempUrl, r))
			a = a + 1
		except urllib.error.HTTPError:
			print('urllib.error.HTTPError')
			time.sleep(1)
		except urllib.error.URLError:
			print('urllib.error.URLError')
			time.sleep(1)

import threading
for i in range(1,10):
	threading._start_new_thread(main,())

main()