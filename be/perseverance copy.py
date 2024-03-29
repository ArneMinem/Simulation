from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import os
import math
from numpy import *
client = RemoteAPIClient()
sim = client.require('sim')

def simu() :
   sim.setStepping(True)
   sim.startSimulation()
   while (t := sim.getSimulationTime()) < 3:
       print(f'Simulation time: {t:.2f} [s]')
       sim.step()
   sim.stopSimulation()

def info(object) :
   handle = sim.getObject(object)
   position = sim.getObjectPosition(handle, sim.handle_world)
   print("position", position)
   eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
   for i in range(3):
       eulerAngles[i] = math.degrees(eulerAngles[i])
       print(i, eulerAngles[i])
   bbox = sim.getShapeBB(handle)
   print("bbox", bbox)

def set_object_dyn(handle):
   special_properties = sim.objectspecialproperty_collidable | sim.objectspecialproperty_measurable | sim.objectspecialproperty_detectable
   sim.setObjectSpecialProperty(handle, special_properties)
   sim.setObjectInt32Param(handle, sim.shapeintparam_respondable, 1)
   sim.setObjectInt32Param(handle, sim.shapeintparam_static, 0)

# Programme principal   
current_path = os.getcwd()
sim.loadScene(os.path.join(current_path, "perserverance-lab-v0-2-desert.ttt"))

# Récupérer la position du corps :
handle_body_cao = sim.getObject("/Body")
position_body = sim.getObjectPosition(handle_body_cao, sim.handle_world)
euler_angles_body = sim.getObjectOrientation(handle_body_cao, sim.handle_world)
# Récupérer la dimension du corps
bbox = sim.getShapeBB(handle_body_cao)
# Créer un objet dyamique pour le corps
options = 0
body_handle_dyn = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [bbox[0],bbox[1],bbox[2]], options)
sim.setObjectPosition(body_handle_dyn, position_body, sim.handle_world)
sim.setObjectOrientation(body_handle_dyn, euler_angles_body, sim.handle_world)
sim.setObjectAlias(body_handle_dyn, "/Body" + "_dyn")
set_object_dyn(body_handle_dyn)

# Récupérer la dimension des 6 roues : 
handles_wheels = ["/WheelRearRight", "/WheelRearLeft", "/WheelFrontRight", "/WheelFrontLeft", "/WheelMidRight", "/WheelMidLeft"]
for name in handles_wheels:
   handle = sim.getObject(name)
   bbox = sim.getShapeBB(handle)
   position = sim.getObjectPosition(handle, sim.handle_world)
   euler_angles = sim.getObjectOrientation(handle, sim.handle_world)
   options = 0
   wheel_handle_dyn = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [bbox[1], bbox[1], bbox[0]], options)
   sim.setObjectPosition(wheel_handle_dyn, position, sim.handle_world)
   sim.setObjectOrientation(wheel_handle_dyn, [0, math.radians(90), 0], sim.handle_world)
   sim.setObjectAlias(wheel_handle_dyn, name + "_dyn")
   set_object_dyn(wheel_handle_dyn)