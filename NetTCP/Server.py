import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 10000
server_addr = ('localhost', port)
print("Listen on port: ", port)

sock.bind(server_addr)

sock.listen(1)

while True:
    # Wait for connect
    print("Waiting for connection")
    connection, client_addr = sock.accept()

    try:
        print("Connection from: ", client_addr)

        while True:
            data = connection.recv(255)
            print("Received: ", data)
            if data:
                print("Echo back")
                connection.sendall(data)
            else:
                print("Connection closed")
                break
    finally:
        connection.close()