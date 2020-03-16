



class RpcProtocol(object):
    def __init__(self):
        self.CMD_CREATE_USER = 1
        self.version = ""
        self.cmd = ""
        self.magicNum = ""
        self.boylen = ""
        self.body = ""
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



if __name__  == '__main__':
    a = RpcProtocol()
