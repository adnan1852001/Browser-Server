import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('localhost', 9000))
cmd = 'GET /page.html HTTP/1.0\r\n\r\n'.encode()  
mysock.send(cmd)

while True:
    data = mysock.recv(512).decode()
    if len(data) < 1:
        break
    print(data)

mysock.close()
