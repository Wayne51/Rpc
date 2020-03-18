



"""
{}
序列话
"""

class RpcProtocol(object):
    def __init__(self):
        self.CMD_CREATE_USER = 1
        self.version = int()
        self.cmd = int()
        self.magicNum = int()
        self.boylen = 0
        self.body = {}
        self.HEAD_LEN = 16


    def getVersion(self):
        return self.version


    def getCmd(self):
        return self.cmd


    def getmagicNum(self):
        return self.magicNum


    def boylen(self):
        return self.boylen



    def getBody(self):
        return self.body


    def head_len(self):
        return self.HEAD_LEN



    def generateByteArray(self):
        data = self.HEAD_LEN + self.boylen
        index = 0

if __name__  == '__main__':
    a = RpcProtocol()
    print(a.version)
