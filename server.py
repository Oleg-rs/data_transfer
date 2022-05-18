from socket import *
from generor import chek

my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.bind(('localhost', 22))
my_socket.listen(10)

i = 0
while i < 1000:
    client, adress = my_socket.accept()
    my_time = client.recv(1024)
    my_time_code = my_time.decode()
    with open("log.txt", "a", encoding='utf-8') as file:
        file.writelines(my_time_code + "\n")
    my = chek(my_time_code)
    if my != False:
        print(my, end='')
    client.close()
    i += 1
