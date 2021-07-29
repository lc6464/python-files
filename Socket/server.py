import socket
from getAddress import IPAddress, socketObject
from time import sleep, time
from threading import Thread




class Server:
	def __init__(self, socketObject, address):
		self.address = address
		self.socket = socketObject
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)  # 设置端口复用
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)  # keepalive 保持长连接
		self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 30)  # 设置超时时间为 30s
		self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 10)  # 每次尝试 10s
		self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)  # 尝试五次


	def run(self, address=None):
		if address != None:
			self.address = address
		self.socket.bind(self.address)  # 绑定地址和端口
		self.socket.listen(100)
		while True:
			clientSocket, clientAddress = self.socket.accept()  # 等待连接
			if len(clientAddress) == 4:  # 判断是 IPv6 请求还是 IPv4，获取客户端地址字符串
				clientAddressString = ('[{}]:{}' if clientAddress[3] == 0 else ('[{}%' + clientAddress[3] + ']:{}')).format(clientAddress[0], clientAddress[1])
			else:
				clientAddressString = clientAddress[0]
			print('客户端 %s 已连接！' % clientAddressString)  # 打印已连接信息
			clientSocket.send('已连接！'.encode())  # 发送给客户端
			lastTime = time()  # 超时检测时间初始化
			t = Thread(target=self.process_data, args=(clientSocket, clientAddress, lastTime, clientAddressString))  # 处理数据
			t.start()  # 启动线程


	def process_data(self, clientSocket, clientAddress, lastTime, clientAddressString):  # 处理数据
		while True:
			if lastTime <= time() - 60:  # 超时检测
				print('客户端 %s 超时！' % clientAddressString)  # 打印信息
				break
			try:
				data = clientSocket.recv(2048)  # 接收信息
			except ConnectionResetError as e:  # 连接充值
				print('与客户端 %s 的连接已重置！\n信息：%s' % (clientAddressString, e.strerror))
				break
			if data != b'':  # 正常信息
				lastTime = time()  # 重置计时器
				try:
					result = data.decode()  # 解码数据
				except:
					result = None  # 解码失败
				if result == 'close':  # 客户端通知断连
					print('客户端 %s 通知服务器断开连接！' % clientAddressString)
					break
				elif result == 'ping':  # ping/pong
					lastTime = time()
				else:  # 打印客户端发送的数据
					print('客户端 %s 发送了：%s' % (clientAddressString, result))
			else:  # 异常信息
				print('客户端 %s 离线了！' % clientAddressString)
				break
		clientSocket.close()  # 关闭连接

if __name__ == '__main__':
	server = Server(socketObject, (IPAddress, 5000))  # 初始化对象
	server.run()  # 启动服务