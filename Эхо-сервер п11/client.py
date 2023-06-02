import socket
import select
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddr = input('Enter IP address: ')
if not ipaddr: ipaddr = 'localhost'
port = 9090
server.connect((ipaddr, port))

while True:
    socketsList = [sys.stdin, server]
    readSockets, writeSocket, errorSocket = select.select(socketsList, [], [])
    for socks in readSockets:
        if socks == server:
            message = socks.recv(1024).decode()
            print(message)
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
            sys.stdout.write('<You>: ')
            sys.stdout.write(message)
            sys.stdout.flush()

server.close()