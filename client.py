import socket
import sys
from server import ip_getter

localhost = '127.0.0.1'

class Client_class:
    def __init__(self):
        print("I am a client")
        print("my ip is:"+ ip_getter())
        self.host = localhost
        HOST = self.host   # The remote host
        PORT = 42069              # The same port as used by the server
        #self.host = input("what is the server address?:")
        
        print("you put in:"+self.host+ 'len of string:'+ str(len(self.host)))
        
    def client_func(self):
        HOST = self.host   # The remote host
        PORT = 42069              # The same port as used by the server
        s = None
        for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
            print('res =' + str(res))
            af, socktype, proto, canonname, sa = res
            try:
                s = socket.socket(af, socktype, proto)
                print("my sock address is :"+str(s.getsockname()))
            except OSError as msg:
                s = None
                continue
            try:
                s.connect(sa)
            except OSError as msg:
                s.close()
                s = None
                continue
            break
        if s is None:
            print('could not open socket')
            sys.exit(1)
        with s:
            string = b'Hello, world'
            print('sending:' + str(string))
            s.sendall(string)
            data = s.recv(1024)
        print('Received', repr(data))
