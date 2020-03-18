
import socket
import socketserver




class ServerHandler(socketserver.BaseRequestHandler):
    """
    Sockert Connect

    """
    def init(self):
        CMD_CREATE_USER = 1
        CMD_FIND_USER = 2
        return CMD_CREATE_USER,CMD_FIND_USER


    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                print(self.init())
                if len(data) == 0:break
                self.request.send(data.upper())
            except ConnectionResetError:
                break

    def channelRead(self, msg):
        recvData = msg
        if recvData == 0:
            print("receive request from client, but the data length is 0")

            return
        else:
            print("传输的数据是{}".format(recvData))









if __name__ == '__main__':
    # print('123')

    server = socketserver.ThreadingTCPServer(('127.0.0.1',8081), ServerHandler)
    server.serve_forever()






