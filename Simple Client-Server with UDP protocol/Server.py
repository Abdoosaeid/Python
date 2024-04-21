import socket

server_host = "localhost"
server_port = 12000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_host, server_port))

print("Server is ready to receive")

while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode('utf-8').upper()
    server_socket.sendto(modified_message.encode('utf-8'), client_address)
