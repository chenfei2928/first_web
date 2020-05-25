import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(("127.0.0.1",10086))
sk.listen()

# 准备接受连接
print('准备完毕----------')
conn,address = sk.accept()
print('客户端连接成功')

while 1:

    # 发送的数据必须是bytes 字节
    conn.send('你好，你好，你好'.encode('utf-8'))

    msg_bytes =conn.recv(1024)
    s = msg_bytes.decode('utf-8')
    print(f'来自客户端的数据是:{s}')

