import socket 
import time


HOST = 'localhost'
PORT = 8080


s = socket.socket()
s.connect((HOST,PORT))


while True:
    data = s.recv(1024)
    print(data.decode('utf-8'))
    time.sleep(2)
