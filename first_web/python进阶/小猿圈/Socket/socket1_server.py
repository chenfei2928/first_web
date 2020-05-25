import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # step1 初始化实例
s.bind(('0.0.0.0',9000))# step2 127.0.0.1 只能本金访问，外网无法访问  绑定IP地址及端口
s.listen(2)  # step3 允许挂起多少个链接

print('服务器开启，等待客户端连接。。。。')

s.accept()  # step4 等待连接
            # 当一个连接进来，生成一个专门的实例
client_conn,cliend_addr = s.accept()
print(cliend_addr,cliend_addr)
client_conn.send("保持终身学习".encode())  # 只接受字节类型  # 发数据给客户端
data = client_conn.recv(1024)  # 从客户端收数据,1024字节  1K
print('服务器端消息:',data.decode())


client_conn.close()   # 关掉客户端连接
s.close()   # 关掉服务器

