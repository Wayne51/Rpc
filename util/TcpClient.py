#_*_coding:utf-8_*_
import socket

BUFSIZE=1024
ip_port=('127.0.0.1',8081)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res=s.connect_ex(ip_port)

while True:
    msg=input('>>: ').strip()
    if len(msg) == 0:continue
    if msg == 'quit':break

    s.send(msg.encode('utf-8'))
    act_res=s.recv(BUFSIZE)

    print(act_res.decode('utf-8'),end='')