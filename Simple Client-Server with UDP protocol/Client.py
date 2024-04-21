import socket 

server_name = "localhost"
server_port = "12000"
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = input("Input lowercase sentence: ")
client_socket.sendto(message.encode('UTF-8'),(server_name,server_port))

data ,client_Address = client_socket.recvfrom(2048)
print(data.decode('UTF-8'))
client_socket.close()
message = input('Press enter to exit')

