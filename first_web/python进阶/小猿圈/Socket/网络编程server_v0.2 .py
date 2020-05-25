import socket
import tkinter as tk
from threading import Thread

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(("127.0.0.1",10010))
sk.listen()

# 准备接受连接
print('准备完毕----------')
conn,address = sk.accept()
print('客户端连接成功')


# 创建窗口
win = tk.Tk()
win.title('聊天窗口')
win.geometry('500x300')

msg_box = tk.Text(win)  #文本域

var = tk.Variable()
tf = tk.Entry(win,textvariable=var)  # 用户输入文本框
# 简单布局
msg_box.pack(side = tk.TOP,fill=tk.X)
tf.pack(side=tk.BOTTOM,fill=tk.X)

def func(event):
    s = var.get()
    conn.send(s.encode("utf-8"))
    print(s)
    var.set("")

tf.bind("<KeyPress-Return>", func)

def recv():
    while 1:
        msg_bytes = conn.recv(1024)
        s = msg_bytes.decode('utf-8')
        msg_box.insert(tk.END, s+"\n")

t = Thread(target=recv)
t.start()

win.mainloop()

conn.close()
sk.close()