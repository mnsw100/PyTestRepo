import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 10000
serv_addr = ('localhost', port)

print("Connecting to %s port %s", serv_addr)

sock.connect(serv_addr)

try:

    # Send data
    message = 'This is the message'
    print("Sending: ", message)
    sock.sendall(message.encode())

    amount_recv = 0
    amount_expect = len(message)

    all_data = ''

    while amount_recv < amount_expect:
        data = sock.recv(1)
        amount_recv += len(data)
        all_data += data.decode()
        print("Received: ", len(data))

    print("Received: %s", all_data)

finally:
    sock.close()