# Echo server program
import socket
import sys
import json
import requests

def ip_getter():
    
    info = json.loads(requests.get("http://jsonip.com").text)
    return info["ip"]
class Server_class:
    
    def __init__(self):
        print("I am a server")
        print("my ip is:"+ ip_getter())
        self.client_list = []
        while self.server_func():
            pass
    def broadcast(self, message):
        for client_socket_number in client_list:
            conn.sendall(message)
            
    def server_func(self):
        HOST = None               # Symbolic name meaning all available interfaces
        PORT = 42069              # Arbitrary non-privileged port
        s = None
        not_end_q = True
        for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                    socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
            af, socktype, proto, canonname, sa = res
            try:
                s = socket.socket(af, socktype, proto)
                print('server address is:' + str(s.getsockname()))
            except OSError as msg:
                s = None
                continue
            try:
                print('tried to bind')
                s.bind(sa)
                print('trying to listen')
                s.listen(1)
            except OSError as msg:
                print("stopped listening")
                s.close()
                s = None
                not_end_q = False
                continue
            break
        if s is None:
            print('could not open socket')
            sys.exit(1)
        conn, addr = s.accept()
        
        with conn:
            client_list.append(conn)
            print('Connected by', addr, ' con:', conn)
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.send(data)
        return not_end_q
