import socket
import math
import time

from navpy import lla2ned

# Reference coordinates (lat_ref, lon_ref) of the fixed point
lat_ref = 48.418467
lon_ref = -4.473927
alt_ref = 89

max_speed = 5.0

def client_gnss():
    host = "127.0.0.1" # IP of server
    port_stsp = 1024  # socket server port number for steering and speed commands
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port_stsp))  # connect to the server
    
    # comunication loop
    while True:
        message = "%.2f;%.2f"%(0,1)
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # debug: show in terminal
        if len(data) > 0:
            sdata = data.split(";")
            lat_tricycle = float(sdata[0])
            lon_tricycle = float(sdata[1])
            alt_tricycle = float(sdata[2])
            x_tricycle, y_tricycle, z_tricycle = lla2ned(lat_tricycle, lon_tricycle, alt_tricycle, lat_ref, lon_ref, alt_ref)
            print("Tricycle position: lat=%.6f, lon=%.6f, alt=%.2f"%(lat_tricycle, lon_tricycle, alt_tricycle))
            print("Tricycle position: x=%.2f, y=%.2f, z=%.2f"%(x_tricycle, y_tricycle, z_tricycle))
        time.sleep(0.1)
    client_socket.close()  # close the connection (not used, stop with Ctrl-C)

def sysCall_init():
    pass

if __name__ == '__main__':
    #client_stsp()
    client_gnss()