#python
import socket
import numpy as np

from navpy import ned2lla

rho = 6371000  # Earth radius in meters

# Reference coordinates (lat_ref, lon_ref) of the fixed point
lat_ref = 48.418467
lon_ref = -4.473927
alt_ref = 89

def sysCall_thread():
    sim=client.require("sim")
    #sim.setStepping(True)
    #sim.setThreadAutomaticSwitch(True)
    while True: # infinite call to server
        server_gnss()

def server_gnss():
    host = "127.0.0.1" # IP of server_stsp (here localhost as we stay on the same computer)
    port_stsp = 1024  # initiate port number (above 1024) for steering and speed commands
    print ("host: %s:%d"%(host,port_stsp)) # debug (print in CoppeliaSim bottom window)

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port_stsp))  # bind host address and port_stsp together

    # configure how many client the server_stsp can listen simultaneously
    server_socket.listen(1)

    # warning : this is blocking !!!
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address)) # debug
    
    # communication loop
    while True:

        # get the position of 'Tricycle' object
        tricycle = sim.getObjectHandle("Tricycle")
        position = sim.getObjectPosition(tricycle, -1)

        # get the position of 'Obstacle' object
        obstacle = sim.getObjectHandle("Obstacle")
        position_obstacle = sim.getObjectPosition(obstacle, -1)

        # compute the position of tricycle relative to the obstacle
        x_tricycle = position[0]-position_obstacle[0]
        y_tricycle = position[1]-position_obstacle[1]
        z_tricycle = position[2]-position_obstacle[2]

        p_tricycle = np.array([x_tricycle, y_tricycle, z_tricycle])

        # convert the position of tricycle to latitude, longitude and altitude
        p_lla = ned2lla(p_tricycle, lat_ref, lon_ref, alt_ref)

        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            print ("close ...") # debug
            # if no data are received, break (client connection lost)
            break
        else:
            # get robot commands (steering and speed)
            print("from connected user: " + str(data))
            sdata = data.split(";")
            steering = float(sdata[0])
            speed = float(sdata[1])

            print("Tricycle position: lat=%.6f, lon=%.6f, alt=%.2f"%(p_lla[0], p_lla[1], p_lla[2]))

            # and send these sensor data to the client 
            sensor_data = "%.6f;%.6f;%.2f"%(p_lla[0], p_lla[1], p_lla[2])
            conn.send(sensor_data.encode())  # send data to the client (encode string to bytes)

            sim.switchThread() # resume in next simulation step
    conn.close()  # close the connection