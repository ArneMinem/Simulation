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
sim.saveScene(os.path.join(current_path, "perserverance-q2.ttt"))

# Fonction pour rendre une forme primitive ou un objet : dynamique, détectable, "collisionnable" et mesurable

def set_object_dyn(handle):
    special_properties = sim.objectspecialproperty_collidable + sim.objectspecialproperty_measurable + sim.objectspecialproperty_detectable
    sim.setObjectSpecialProperty(handle, special_properties)
    sim.setObjectInt32Param(handle, sim.shapeintparam_respondable, 1)
    sim.setObjectInt32Param(handle, sim.shapeintparam_static, 0)

### Question 1 ###

## Afficher les caractéristiques d’un élément de CAO (ex pneu avant)
# 
# print("Body's position")
# 
# handle = sim.getObject("/Body")
# position = sim.getObjectPosition(handle, sim.handle_world)
# print(position)
# 
# print("Body's orientation")
# 
# orientation = sim.getObjectOrientation(handle, sim.handle_world)
# print(orientation)
# 
# print("Wheel's dimensions")
# 
# handle = sim.getObject("/WheelRearRight")
# bbox = sim.getShapeBB(handle)
# print(bbox)
# 
### Question 2 ###

print("Forme primitive pour body")

handle = sim.getObject("/Body")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique du body

options = 0
body_diameter = 1.616
body_thickness = 4.089
body_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [body_diameter, body_diameter, body_thickness], options)
sim.setObjectOrientation(body_handle, [math.radians(90), 0, -math.radians(90)], sim.handle_world)
sim.setObjectPosition(body_handle, [-0.06710752844810486, -0.3080650568008423, 1.4252123832702637], sim.handle_world)
sim.setObjectAlias(body_handle, "body_dyn")
set_object_dyn(body_handle)

print("Forme primitive pour wheels")

handle = sim.getObject("/WheelRearRight")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique du body

options = 0
wrr_diameter = 0.524785
wrr_thickness = 0.3437
wrr_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wrr_diameter, wrr_diameter, wrr_thickness], options)
sim.setObjectOrientation(wrr_handle, [math.radians(23.746522210072314), math.radians(-90.46338811018134884), math.radians(0.7933965215763155)], sim.handle_world)
sim.setObjectPosition(wrr_handle, [-1.0624862909317017, 1.164980173110962, 0.26345884799957275], sim.handle_world)
sim.setObjectAlias(wrr_handle, "wrr_dyn")
set_object_dyn(wrr_handle)



handle = sim.getObject("/WheelRearLeft")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique du body

options = 0
wrl_diameter = 0.524785
wrl_thickness = 0.3437
wrl_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wrl_diameter, wrl_diameter, wrl_thickness], options)
sim.setObjectOrientation(wrl_handle, [math.radians(45.25791834482287), math.radians(-90.14023667813975074), math.radians(0.9081195167575136)], sim.handle_world)
sim.setObjectPosition(wrl_handle, [1.0624865293502808, 1.164986491203308, 0.26424795389175415], sim.handle_world)
sim.setObjectAlias(wrl_handle, "wrl_dyn")
set_object_dyn(wrl_handle)



handle = sim.getObject("/WheelFrontRight")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique du body

options = 0
wfr_diameter = 0.524785
wfr_thickness = 0.3437
wfr_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wfr_diameter, wfr_diameter, wfr_thickness], options)
sim.setObjectOrientation(wfr_handle, [math.radians(23.746522210072314), math.radians(-90.46338811018134884), math.radians(0.7933965215763155)], sim.handle_world)
sim.setObjectPosition(wfr_handle, [-1.0624862909317017, -1.0949854850769043, 0.26345860958099365], sim.handle_world)
sim.setObjectAlias(wfr_handle, "wfr_dyn")
set_object_dyn(wfr_handle)



handle = sim.getObject("/WheelFrontLeft")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique du body

options = 0
wfl_diameter = 0.524785
wfl_thickness = 0.3437
wfl_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wfl_diameter, wfl_diameter, wfl_thickness], options)
sim.setObjectOrientation(wfl_handle, [math.radians(23.746522210072314), math.radians(-90.46338811018134884), math.radians(0.7933965215763155)], sim.handle_world)
sim.setObjectPosition(wfl_handle, [1.0624865293502808, -1.0949794054031372, 0.26424771547317505], sim.handle_world)
sim.setObjectAlias(wfl_handle, "wfl_dyn")
set_object_dyn(wfl_handle)



handle = sim.getObject("/WheelMidRight")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique du body

options = 0
wmr_diameter = 0.524785
wmr_thickness = 0.3437
wmr_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wmr_diameter, wmr_diameter, wmr_thickness], options)
sim.setObjectOrientation(wmr_handle, [math.radians(23.746522210072314), math.radians(-90.46338811018134884), math.radians(0.7933965215763155)], sim.handle_world)
sim.setObjectPosition(wmr_handle, [-1.184484839439392, 0.09000296890735626, 0.2638533115386963], sim.handle_world)
sim.setObjectAlias(wmr_handle, "wmr_dyn")
set_object_dyn(wmr_handle)



handle = sim.getObject("/WheelMidLeft")
position = sim.getObjectPosition(handle, sim.handle_world)
print("position", position)
eulerAngles = sim.getObjectOrientation(handle, sim.handle_world)
for i in range(3):
    eulerAngles[i] = math.degrees(eulerAngles[i])
    print(i, eulerAngles[i])
bbox = sim.getShapeBB(handle)
print("bbox", bbox)

# Créer une forme primitive de représentation dynamique du body

options = 0
wml_diameter = 0.524785
wml_thickness = 0.3437
wml_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wml_diameter, wml_diameter, wml_thickness], options)
sim.setObjectOrientation(wml_handle, [math.radians(23.746522210072314), math.radians(-90.46338811018134884), math.radians(0.7933965215763155)], sim.handle_world)
sim.setObjectPosition(wml_handle, [1.184484839439392, 0.09000296890735626, 0.2638533115386963], sim.handle_world)
sim.setObjectAlias(wml_handle, "wml_dyn")
set_object_dyn(wml_handle)


# Création d'une articulation pivot horizontale : moteur de la roue arrière droite

print("Création d'une articulation pivot horizontale : moteur de la roue avant")

options = 0
sizes = [0.15, 0.02]
wrr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wrr_motor_handle, "front_motor")
sim.setObjectOrientation(wrr_motor_handle, [0, -math.pi/2.0, 0], wrr_motor_handle)
position = sim.getObjectPosition(wrr_handle, sim.handle_world)
sim.setObjectPosition(wrr_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue arrière gauche

print("Création d'une articulation pivot horizontale : moteur de la roue avant")

options = 0
sizes = [0.15, 0.02]
wrl_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wrl_motor_handle, "front_motor")
sim.setObjectOrientation(wrl_motor_handle, [0, -math.pi/2.0, 0], wrl_motor_handle)
position = sim.getObjectPosition(wrl_handle, sim.handle_world)
sim.setObjectPosition(wrl_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue avant droite

print("Création d'une articulation pivot horizontale : moteur de la roue avant")

options = 0
sizes = [0.15, 0.02]
wfr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wfr_motor_handle, "front_motor")
sim.setObjectOrientation(wfr_motor_handle, [0, -math.pi/2.0, 0], wfr_motor_handle)
position = sim.getObjectPosition(wfr_handle, sim.handle_world)
sim.setObjectPosition(wfr_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue avant gauche

print("Création d'une articulation pivot horizontale : moteur de la roue avant")

options = 0
sizes = [0.15, 0.02]
wfl_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wfl_motor_handle, "front_motor")
sim.setObjectOrientation(wfl_motor_handle, [0, -math.pi/2.0, 0], wfl_motor_handle)
position = sim.getObjectPosition(wfl_handle, sim.handle_world)
sim.setObjectPosition(wfl_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue milieu droite

print("Création d'une articulation pivot horizontale : moteur de la roue milieu droite")

options = 0
sizes = [0.15, 0.02]
wmr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wmr_motor_handle, "front_motor")
sim.setObjectOrientation(wmr_motor_handle, [0, -math.pi/2.0, 0], wmr_motor_handle)
position = sim.getObjectPosition(wmr_handle, sim.handle_world)
sim.setObjectPosition(wmr_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue milieu gauche

print("Création d'une articulation pivot horizontale : moteur de la roue milieu gauche")

options = 0
sizes = [0.15, 0.02]
wml_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wml_motor_handle, "front_motor")
sim.setObjectOrientation(wml_motor_handle, [0, -math.pi/2.0, 0], wml_motor_handle)
position = sim.getObjectPosition(wml_handle, sim.handle_world)
sim.setObjectPosition(wml_motor_handle, position, sim.handle_world)

# Assemblage du robot, création de l’arbre de description

keep_in_place = True
sim.setObjectParent(wrr_motor_handle, body_handle, keep_in_place)
sim.setObjectParent(wrl_motor_handle, body_handle, keep_in_place)
sim.setObjectParent(wfr_motor_handle, body_handle, keep_in_place)
sim.setObjectParent(wfl_motor_handle, body_handle, keep_in_place)
sim.setObjectParent(wmr_motor_handle, body_handle, keep_in_place)
sim.setObjectParent(wml_motor_handle, body_handle, keep_in_place)

sim.setObjectParent(wrr_handle, wrr_motor_handle, keep_in_place)
sim.setObjectParent(wrl_handle, wrl_motor_handle, keep_in_place)
sim.setObjectParent(wfr_handle, wfr_motor_handle, keep_in_place)
sim.setObjectParent(wfl_handle, wfl_motor_handle, keep_in_place)
sim.setObjectParent(wmr_handle, wmr_motor_handle, keep_in_place)
sim.setObjectParent(wml_handle, wml_motor_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/WheelRearRight"), wrr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelRearLeft"), wrl_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelFrontRight"), wfr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelFrontLeft"), wfl_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelMidRight"), wmr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelMidLeft"), wml_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/Body"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/SuspensionTop"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/SuspensionRearRight"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/SuspensionRearLeft"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/SuspensionFrontRight"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/SuspensionFrontLeft"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelAttachRearRight"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelAttachRearLeft"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelAttachFrontRight"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelAttachFrontLeft"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/Body"), body_handle, keep_in_place)

# Rendre des objets invisibles

sim.setObjectInt32Param(body_handle,sim.objintparam_visibility_layer,0)

sim.setObjectInt32Param(wrr_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wrl_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wfr_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wfl_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wmr_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wml_handle,sim.objintparam_visibility_layer,0)

sim.setObjectInt32Param(wrr_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wrl_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wfr_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wfl_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wmr_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(wml_motor_handle,sim.objintparam_visibility_layer,0)