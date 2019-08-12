import socket
from threading import Thread

HOST = 'localhost'
PORT = 9009

def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            pass
def runChat():
    with socket.socket(socket.AF_INET, socket.SOCKET_STREAM) as sock:
        socket.connect((HOST, PORT))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True
        t.start()

        while True:
            msg = input()
            if msg == '/quit':
                sock.send(msg.encode())
                break

                sock.send(msg.encode())
    runChat()
