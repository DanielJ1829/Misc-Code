import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.204.251.143', 55555))
message = s.recv(1024)
s.close()

print(message.decode())
