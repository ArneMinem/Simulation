from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import os
import math


client = RemoteAPIClient()
sim = client.require('sim')
sim.setStepping(True)

# Chargement et enregistrement des fichiers scene .ttt : chargement du fichier CAO tricycle et enregistrement du modèle dynamique.

current_path = os.getcwd()
sim.loadScene(os.path.join(current_path, "tricycle-cad.ttt"))
# do some work to create the dynamic model
sim.saveScene(os.path.join(current_path, "tricycle-dyn-td3.ttt"))

# Fonction pour rendre une forme primitive ou un objet : dynamique, détectable, "collisionnable" et mesurable

def set_object_dyn(handle):
    special_properties = sim.objectspecialproperty_collidable + sim.objectspecialproperty_measurable + sim.objectspecialproperty_detectable
    sim.setObjectSpecialProperty(handle, special_properties)
    sim.setObjectInt32Param(handle, sim.shapeintparam_respondable, 1)
    sim.setObjectInt32Param(handle, sim.shapeintparam_static, 0)

# Afficher les caractéristiques d’un élément de CAO (ex pneu avant)

print("Front tyre")

handle = sim.getObject("/FrontTyre")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique de la roue avant

options = 0
wheel_diameter = 0.45
wheel_thickness = 0.08
front_wheel_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wheel_diameter, wheel_diameter, wheel_thickness], options)
sim.setObjectOrientation(front_wheel_handle, [0, math.radians(90), 0], sim.handle_world)
sim.setObjectPosition(front_wheel_handle, [0, 0.225, 0.225], sim.handle_world)
sim.setObjectAlias(front_wheel_handle, "front_wheel_dyn")
set_object_dyn(front_wheel_handle)

# Afficher les caractéristiques d’un élément de CAO (ex pneu arrière gauche)

print("\nRear left tyre")

handle = sim.getObject("/RearLeftWheel")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique de la roue avant

options = 0
wheel_diameter = 0.27
wheel_thickness = 0.0745
rear_left_wheel_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wheel_diameter, wheel_diameter, wheel_thickness], options)
sim.setObjectOrientation(rear_left_wheel_handle, [0, math.radians(90), 0], sim.handle_world)
sim.setObjectPosition(rear_left_wheel_handle, [-0.206, -0.412, 0.1354], sim.handle_world)
sim.setObjectAlias(rear_left_wheel_handle, "rear_left_wheel_dyn")
set_object_dyn(rear_left_wheel_handle)

# Afficher les caractéristiques d’un élément de CAO (ex pneu arrière droite)

print("\nRear right tyre")

handle = sim.getObject("/RearRightWheel")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique de la roue avant

options = 0
wheel_diameter = 0.27
wheel_thickness = 0.0745
rear_right_wheel_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wheel_diameter, wheel_diameter, wheel_thickness], options)
sim.setObjectOrientation(rear_right_wheel_handle, [0, math.radians(90), 0], sim.handle_world)
sim.setObjectPosition(rear_right_wheel_handle, [0.206, -0.412, 0.1354], sim.handle_world)
sim.setObjectAlias(rear_right_wheel_handle, "rear_right_wheel_dyn")
set_object_dyn(rear_right_wheel_handle)

# Afficher les caractéristiques d’un élément de CAO (ex cadre)

print("\nMain body tube")

handle = sim.getObject("/MainBodyTube")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique de la roue avant

options = 0
wheel_diameter = 0.08
wheel_thickness = 0.722
main_body_tube_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wheel_diameter, wheel_diameter, wheel_thickness], options)
sim.setObjectOrientation(main_body_tube_handle, [math.radians(-46.093740412014895), math.radians(0), math.radians(-24.389794933852382)], sim.handle_world)
sim.setObjectPosition(main_body_tube_handle, [0, -0.20826, 0.398548], sim.handle_world)
sim.setObjectAlias(main_body_tube_handle, "main_body_tube_dyn")
set_object_dyn(main_body_tube_handle)

# Afficher les caractéristiques d’un élément de CAO (ex poignets)

print("\nGrippers")

handle = sim.getObject("/Grippers")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique de la roue avant

options = 0
wheel_diameter = 0.04505698724520585*2
wheel_thickness = 0.7389752268790792
grippers_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wheel_diameter, wheel_diameter, wheel_thickness], options)
sim.setObjectOrientation(grippers_handle, [math.radians(0.0), math.radians(89.99998056844193), math.radians(179.25022417382897)], sim.handle_world)
sim.setObjectPosition(grippers_handle, [-2.3543834686279297e-06, 0.02240690588951111, 0.8452675151824951], sim.handle_world)
sim.setObjectAlias(grippers_handle, "grippers_dyn")
set_object_dyn(grippers_handle)

# Afficher les caractéristiques d’un élément de CAO (ex fourche)

print("\nFork")

handle = sim.getObject("/Fork")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique de la roue avant

options = 0
wheel_diameter = 0.06341355437199944
wheel_thickness = 0.4092986631975696
fork_left_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wheel_diameter, wheel_diameter, wheel_thickness], options)
sim.setObjectOrientation(fork_left_handle, [math.radians(23.666333769325128), math.radians(0.009068372188585293), math.radians(92.14215838080936)], sim.handle_world)
sim.setObjectPosition(fork_left_handle, [0.00015035271644592285 - 0.08, 0.14679130911827087, 0.3814055919647217], sim.handle_world)
sim.setObjectAlias(fork_left_handle, "fork_left_dyn")
set_object_dyn(fork_left_handle)

# Créer une forme primitive de représentation dynamique de la roue avant

options = 0
wheel_diameter = 0.06341355437199944
wheel_thickness = 0.4092986631975696
fork_right_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wheel_diameter, wheel_diameter, wheel_thickness], options)
sim.setObjectOrientation(fork_right_handle, [math.radians(23.666333769325128), math.radians(0.009068372188585293), math.radians(92.14215838080936)], sim.handle_world)
sim.setObjectPosition(fork_right_handle, [0.00015035271644592285 + 0.08, 0.14679130911827087, 0.3814055919647217], sim.handle_world)
sim.setObjectAlias(fork_right_handle, "fork_right_dyn")
set_object_dyn(fork_right_handle)

# Les deux tubes sont regroupés en créant un tableau d’objets à regrouper

group_handles = []
group_handles.append(fork_left_handle)
group_handles.append(fork_right_handle)  # last added represents the group
fork_handle = sim.groupShapes(group_handles, False)
sim.setObjectAlias(fork_handle, "fork_dyn")

# Les deux tubes sont regroupés en créant un tableau d’objets à regrouper

group_handles = []
group_handles.append(grippers_handle)
group_handles.append(fork_handle)  # last added represents the group
fork_handle = sim.groupShapes(group_handles, False)
sim.setObjectAlias(fork_handle, "fork_dyn")

# Création d'une articulation pivot horizontale : moteur de la roue avant

options = 0
sizes = [0.15, 0.02]
front_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(front_motor_handle, "front_motor")
sim.setObjectOrientation(front_motor_handle, [0, -math.pi/2.0, 0], front_motor_handle)
position = sim.getObjectPosition(front_wheel_handle, sim.handle_world)
sim.setObjectPosition(front_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur des roues arrières

options = 0
sizes = [0.15, 0.02]
rear_left_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(rear_left_motor_handle, "rear_left_motor")
sim.setObjectOrientation(rear_left_motor_handle, [0, -math.pi/2.0, 0], rear_left_motor_handle)
position = sim.getObjectPosition(rear_left_wheel_handle, sim.handle_world)
sim.setObjectPosition(rear_left_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur des roues arrières

options = 0
sizes = [0.15, 0.02]
rear_right_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(rear_right_motor_handle, "rear_right_motor")
sim.setObjectOrientation(rear_right_motor_handle, [0, -math.pi/2.0, 0], rear_right_motor_handle)
position = sim.getObjectPosition(rear_right_wheel_handle, sim.handle_world)
sim.setObjectPosition(rear_right_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur des roues arrières

options = 0
sizes = [0.15, 0.02]
fork_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(fork_motor_handle, "fork_motor")
sim.setObjectOrientation(fork_motor_handle, [math.radians(23.666333769325128), math.radians(0.009068372188585293), math.radians(92.14215838080936)], fork_motor_handle)
position = sim.getObjectPosition(fork_handle, sim.handle_world)
position[0] = 0
sim.setObjectPosition(fork_motor_handle, position, sim.handle_world)

# Assemblage du robot, création de l’arbre de description

keep_in_place = True
sim.setObjectParent(front_motor_handle, fork_handle, keep_in_place)
sim.setObjectParent(front_wheel_handle, front_motor_handle, keep_in_place)

sim.setObjectParent(fork_motor_handle, main_body_tube_handle, keep_in_place)
sim.setObjectParent(fork_handle, fork_motor_handle, keep_in_place)

sim.setObjectParent(rear_left_motor_handle, main_body_tube_handle, keep_in_place)
sim.setObjectParent(rear_right_motor_handle, main_body_tube_handle, keep_in_place)
sim.setObjectParent(rear_left_wheel_handle, rear_left_motor_handle, keep_in_place)
sim.setObjectParent(rear_right_wheel_handle, rear_right_motor_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/RearLeftWheel"), rear_left_wheel_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/RearRightWheel"), rear_right_wheel_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/FrontTyre"), front_wheel_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/FrontWheel"), front_wheel_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/MainBodyTube"), main_body_tube_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/Grippers"), fork_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/Fork"), fork_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/Crankset"), front_wheel_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/PedalLeft"), front_wheel_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/PedalRight"), front_wheel_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/BackBox"), main_body_tube_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/BackBoxFixation"), main_body_tube_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/FrontFender"), fork_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/HandleBar"), fork_motor_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/Saddle"), main_body_tube_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/RearAxis"), main_body_tube_handle, keep_in_place)

# Rendre des objets invisibles

sim.setObjectInt32Param(main_body_tube_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(front_wheel_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(rear_left_wheel_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(rear_right_wheel_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(fork_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(front_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(rear_left_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(rear_right_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(fork_motor_handle,sim.objintparam_visibility_layer,0)

# Définition du mode de contôle (ex .vitesse)

# get handle of the motor
front_motor_handle = sim.getObject("/front_motor")
# control motor with angular velocity
sim.setObjectInt32Param(front_motor_handle, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)

#  Consigne du moteur (ex 90 degrés/s)

# set velocity to 90 degrees /s
target_velocity = math.radians(90)  # rad/s
motion_params = []  # default!
sim.setJointTargetVelocity(front_motor_handle, target_velocity, motion_params)

# Définition du mode de contôle (ex .vitesse)

# get handle of the motor
fork_motor_handle = sim.getObject("/fork_motor")
# control motor with angular velocity
sim.setObjectInt32Param(fork_motor_handle, sim.jointintparam_dynctrlmode, sim.jointdynctrl_position)

#  Consigne du moteur (ex 90 degrés/s)

# set velocity to 90 degrees /s
target_position = math.radians(45)  # rad/s
motion_params = []  # default!
sim.setJointTargetPosition(fork_motor_handle, target_position, motion_params)

sim.startSimulation()
while (t := sim.getSimulationTime()) < 30:
    print(f'Simulationtime: {t:.2f} [s]')
    sim.step()
sim.stopSimulation()
