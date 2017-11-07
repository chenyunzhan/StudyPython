import socket
import threading

udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

recieveAddr = ("192.168.31.223", 8888)
udpSocket.bind(recieveAddr)


def recieve():
    recieveData = udpSocket.recvfrom(1024)
    print(recieveData[0])


def send():
    msg = input("")
    print("             "+msg)
    sendToAddr = ("192.168.31.223",9999)
    udpSocket.sendto(msg.encode("utf-8"),sendToAddr)

while True:
    send()
    recieve()
