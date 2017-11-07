from socket import *

client = socket(AF_INET,SOCK_STREAM)
server_addr = ("192.168.31.223",8888)
client.connect(server_addr)


while True:
    msg = input(">>")
    client.send(msg.encode())
    recv_data = client.recv(1024)
    print(recv_data)

    if recv_data==b"bye":
        break
client.close()