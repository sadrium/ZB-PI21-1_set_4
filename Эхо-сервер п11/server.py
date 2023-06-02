import socket
import select
import sys
from _thread import *


def clientthread(conn, addr):
    conn.send('Welcome to this chatroom!'.encode())
    while True:
        message = conn.recv(2048).decode()
        if message:
            print ("<" + addr[0] + '> ' + message)
            messageToSend = "<" + addr[0] + "> " + message
            broadcast(messageToSend, conn)
        else:
            remove(conn)

def broadcast(message, connection):
    for client in clientsList:
        if client != connection:
            client.send(message.encode())

def remove(connection):
    if connection in clientsList:
        clientsList.remove(connection)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ipaddr = input('Enter IP address: ')
if not ipaddr: ipaddr = 'localhost'
port = 9090
server.bind((ipaddr, port))
server.listen(10)
clientsList = []

while True:
    conn, addr = server.accept()
    clientsList.append(conn)
    print(addr[0] + ' connected')
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()