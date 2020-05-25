import socket

cli =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cli.connect(('localhost',9000))

data =cli.recv(1024)    #最大收1024，

print(data.decode())

cli.send('好好学习，天天向上'.encode())

cli.close()