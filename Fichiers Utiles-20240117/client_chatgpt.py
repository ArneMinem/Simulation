import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(("localhost", 12345))

# Receive data from the server
print(s.recv(1024))

# Close the connection
s.close()
