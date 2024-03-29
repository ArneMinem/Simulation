#python
import socket
import pyproj
from pyproj import Proj 


def sysCall_thread():
    sim.setThreadAutomaticSwitch(True)
    while True: # infinite call to server
        server()

def server():
    host = "127.0.0.1" # IP of server (here localhost as we stay on the same computer)
    port = 6000  # initiate port number (above 1024)
    print ("host: %s:%d"%(host,port)) # debug (print in CoppeliaSim bottom window)

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)

    # warning : this is blocking !!!
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address)) # debug
    
    # communication loop
    while True:
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
            # and apply these commands to the actuators
            sim.setJointTargetPosition(sim.getObject("/Steering"),steering)
            sim.setJointTargetVelocity(sim.getObject("/FrontMotor"),speed)

            # get sensor data
            simu_time = sim.getSimulationTime() # sim time
            front_sonar = sim.getObject("/FrontSonar") # get sonar handle
            result, distance, detected_point, detected_object_handle, detected_object_normal = sim.handleProximitySensor (front_sonar)
            # and send these sensor data to the client 
            sensor_data = "%.3f;%.2f"%(simu_time, distance)
            # conn.send(sensor_data.encode())  # send data to the client (encode string to bytes)

            # get position
            robot = sim.getObject("/Tricycle")
            position = sim.getObjectPosition(robot, sim.handle_world)
            pos_data = "%.3f;%.2f;%.2f;%.2f"%(simu_time, position[0], position[1], position[2])
            # conn.send(pos_data.encode())  # send data to the client (encode string to bytes)

            # position in latitude, longitude and altitude from x, y, z
            # Define the coordinate systems
            # P = Proj(proj='latlong', datum='WGS84', lat_0=0, lon_0=0)
            # lat, lon = P(position[0], position[1], inverse=True)
            # pos3_data = "%.3f;%.6f;%.6f"%(simu_time, lat, lon)
            # conn.send(pos3_data.encode())

            
            wgs84 = pyproj.CRS("EPSG:4326")  # WGS84 coordinate system (latitude, longitude)
            utm = pyproj.CRS("EPSG:32632")  # UTM coordinate system (x, y, z)

            # Create the transformer
            transformer = pyproj.Transformer.from_crs(utm, wgs84, always_xy=True)

            # Transform the position
            lat, lon, alt = transformer.transform(position[0], position[1], position[2])

            # Print the transformed position
            pos2_data = "%.3f;%.6f;%.6f;%.2f"%(simu_time, lat, lon, alt)

            # Print the transformed position
            conn.send(pos2_data.encode())

            sim.switchThread() # resume in next simulation step
    conn.close()  # close the connection 
