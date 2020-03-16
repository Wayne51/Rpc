
import socket


class ServerHandler(object):
    """

    """
    def __init__(self):
        self.CMDB_CREATE_USER = 1
        self.CMD_FIND_USER = 2




    def channelActive(self):
        udp_sk = socket.socket(type=socket.SOCK_DGRAM)  # 创建一个服务器的套接字
        udp_sk.bind(('127.0.0.1', 9000))  # 绑定服务器套接字
        msg, addr = udp_sk.recvfrom(1024)
        print(msg)
        udp_sk.sendto(b'hi', addr)  # 对话(接收与发送)
        udp_sk.close()  # 关闭服务器套接字




if  __name__  ==  '__main__':
    a = ServerHandler()
    a.channelActive()





