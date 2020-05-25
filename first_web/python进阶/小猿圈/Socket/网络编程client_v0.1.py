import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print('准备连接服务器')

sk.connect(("127.0.0.1",10086))

print('连接成功')

while 1:

    # 接受数据
    msg_bytes =sk.recv(1024)
    s = msg_bytes.decode('utf-8')
    print(f'接受的数据是:{s}')

    sk.send('天王盖地虎'.encode('utf-8'))