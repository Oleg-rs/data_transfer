from socket import *
from generor import generator

i = 0
while i < 1000:
    my_socket = socket(AF_INET, SOCK_STREAM)
    my_socket.connect(('localhost', 22))
    a = generator()
    b = a.encode()
    my_socket.send(b)
    my_socket.close()
    i += 1
