import socket

server_port = 12000

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('',server_port))
print("The server is ready to receicve")

while True:
    data ,client_Address = server_socket.recvfrom(2048)
    message = data.decode('UTF-8')
    print(message)
    new_message = message.upper()

    server_socket.sendto(new_message.encode("UTF-8"),client_Address)