from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import os
import math


client = RemoteAPIClient()
sim = client.require('sim')
sim.setStepping(True)

# Chargement et enregistrement des fichiers scene .ttt : chargement du fichier CAO tricycle et enregistrement du modèle dynamique.

current_path = os.getcwd()
print(current_path)
print(os.path.join(current_path, "perserverance-lab-v0-2.ttt"))
sim.loadScene(os.path.join(current_path, "perserverance-lab-v0-2.ttt"))
# do some work to create the dynamic model
sim.saveScene(os.path.join(current_path, "perserverance-lab-v0-2-dyn.ttt"))

# Fonction pour rendre une forme primitive ou un objet : dynamique, détectable, "collisionnable" et mesurable

def set_object_dyn(handle):
    special_properties = sim.objectspecialproperty_collidable + sim.objectspecialproperty_measurable + sim.objectspecialproperty_detectable
    sim.setObjectSpecialProperty(handle, special_properties)
    sim.setObjectInt32Param(handle, sim.shapeintparam_respondable, 1)
    sim.setObjectInt32Param(handle, sim.shapeintparam_static, 0)

### Question 1 ###

# Afficher les caractéristiques d’un élément de CAO (ex pneu avant)

print("Body's position")

handle = sim.getObject("/Body")
position = sim.getObjectPosition(handle, sim.handle_world)
print(position)

print("Body's orientation")

orientation = sim.getObjectOrientation(handle, sim.handle_world)
print(orientation)

print("Wheel's dimensions")

handle = sim.getObject("/WheelRearRight")
bbox = sim.getShapeBB(handle)
print(bbox)
