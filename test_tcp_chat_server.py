from socket import *
import threading

server = socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server_addr = ("192.168.31.223",8888)
server.bind(server_addr)
server.listen(5)


def deal(client):
    while True:
        recv_msg = client.recv(1024)
        client.send(recv_msg)
        if recv_msg == b"bye":
            print("%s已经断开了"%client)
            break
    client.close()

while True:
    client,client_addr = server.accept()
    deal_thread = threading.Thread(target=deal,args=(client,))
    deal_thread.start()


