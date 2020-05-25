import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.50.177', 22, 'root', 'root')  # 帆软测试服务器

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())
ssh.close();


#执行命令 - 通过用户名和密码连接服务器
