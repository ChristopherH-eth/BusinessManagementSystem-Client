import socket

# file: client.py
# author: 0xChristopher

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("127.0.0.1")
port = 54000

def main():
    print(host)

    s.connect((host, port))
    s.send(b'Hello')
    print(s.recv(4096))
    s.close()

main()