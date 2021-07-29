import socket

# Creates a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds the socket to the port
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.bind(server_address)

sock.listen(1)

while True:
    # Waits for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print(f'connection from {client_address}')

        data = connection.recv(1024)
        print(f'received "{data}"')

    finally:
        # Cleans up the connection
        connection.close()