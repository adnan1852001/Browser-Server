import socket     
from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while True:
            clientsocket, address = serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])

            request_line = pieces[0].split(" ")
            page_address = request_line[1].split("?")[0]

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"

            with open(page_address, 'r') as file:
                data += file.read()
            
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down....\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    
    serversocket.close()

print('Access http://localhost:9000')
createServer()
