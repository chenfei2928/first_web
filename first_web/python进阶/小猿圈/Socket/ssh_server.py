import socket
import subprocess
import json

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",9000))
s.listen(2)   # 监听

count = 0
while True:   # 循环接受数据连接
    conn,client_addr = s.accept()  # 等待被连接
    count += 1
    print(f'{count}一个新的连接接入:{client_addr}')


    while True:
        cmd = conn.recv(1024)
        if not cmd:
            print(f"{client_addr}断开了。。。bye.")
            break
        print(f'from client{client_addr}:{cmd.decode()}')
        cmd_res = subprocess.getstatusoutput(cmd)
        print(cmd_res)

        conn.send(json.dumps(cmd_res).encode())
         # 把接受的数据解码 大下 编码 发送回去；


s.close()

