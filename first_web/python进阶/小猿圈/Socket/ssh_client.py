import socket
import json

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #实例化
c.connect(('localhost',9000))

while True:
    cmd = input('input your cmd >>>:').strip()
        # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    if not cmd:continue
    if cmd == 'q':
        break

    c.send(cmd.encode())


    cmd_result = c.recv(1024).decode()
    print('cmd',cmd_result)
    cmd_res_tuple = json.loads(cmd_result)
    print(cmd_res_tuple[0])  # 命令执行结果

    print(f"命令执行状态{cmd_res_tuple[0]}")

c.close()