import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #实例化
c.connect(('localhost',9000))

while True:
    msg = input('input your msg >>>:').strip()
        # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    if not msg:continue
    if msg == 'q':
        break
    c.send(msg.encode())

    server_response = c.recv(1024)
    print(f"from server:{server_response.decode()}")

c.close()