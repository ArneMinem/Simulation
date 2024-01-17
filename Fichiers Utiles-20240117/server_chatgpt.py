import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
s.bind(("localhost", 12345))

# Listen for incoming connections
s.listen(5)

while True:
    # Establish connection with client
    c, addr = s.accept()
    print("Got connection from", addr)

    # Send a message to the client
    c.send(b"Thank you for connecting")

    # Close the connection
    c.close()
