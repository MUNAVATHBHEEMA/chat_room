#clientpage
import socket
from threading import Thread

name =input("enter your name:")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",9999))
client.send(name.encode())

def send(client):
    while True:
        data = f'{name}:{input("")}'
        client.send(data.encode())

def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()
        except:
            client.close()
            break
thread1=Thread(target=receive,args=(client,))
thread1.start()
thread2=Thread(target=receive,args=(client,))
thread2.start()


