import socket, sys
from time import sleep

i = 0  # 初始化 ID
IDs = []

addressInfos = socket.getaddrinfo(socket.gethostname(), None)  # 获取地址信息列表
# (family, type, proto, canonname, sockaddr)
# type like STREAM
# AddressFamily like [AF_INET | AF_INET6]
# sockaddr [(address, port, flowinfo, scope_id) | (address, port)]


print('ID\tAddress')  # 打印表头

for addressInfo in addressInfos:  # 打印 IP 地址信息
	i += 1
	IDs.append(str(i))
	if addressInfo[0] == socket.AF_INET6:
		show = '[%s]' if addressInfo[4][3] == 0 else '[%s%%' + str(addressInfo[4][3]) + ']'
	else:
		show = '%s'
	print('%s\t%s' % (i, show % addressInfo[4][0]))

print('\n')
ID = input('请输入您需要绑定的 IP 地址的 ID：')  # 获取用户输入

if ID not in IDs:  # 判断是否存在
	print('您输入的 ID 有误！')
	sys.exit(0)

addressInfo = addressInfos[int(ID)-1]  # 选中的 IP 地址信息

socketObject = socket.socket(addressInfo[0])  # 创建 Socket 对象
IPAddress = addressInfo[4][0]  # 对应的 IP 地址

print('IP Address:', IPAddress)