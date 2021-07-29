import socket, sys
from time import sleep

socket6 = socket.socket(socket.AF_INET6)

host = sys.argv[-2]
port = 5000

address = (host, port)

socket6.settimeout(10)  # 设置十秒连接超时

socket6.connect(address)
socket6.send(sys.argv[-1].encode())


sleep(0.2)

# socket6.send('close'.encode())

print(socket6.recv(1024).decode())

# socket6.close()

sleep(15)



# socket6.send('close'.encode())
socket6.send('ping'.encode())

sleep(5)
socket6.close()