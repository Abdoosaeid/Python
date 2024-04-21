import socket

server_name = "localhost"
server_port = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Input lowercase sentence: ")
client_socket.sendto(message.encode('utf-8'), (server_name, server_port))

modified_message, server_address = client_socket.recvfrom(2048)
print("From Server:", modified_message.decode('utf-8'))

client_socket.close()
