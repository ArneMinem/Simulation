from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import os
import math
import time


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
sim.computeMassAndInertia(body_handle, 1)

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
sim.setObjectPosition(wrr_handle, [-1.0624862909317017, 1.164980173110962, 0.27345884799957275], sim.handle_world)
sim.setObjectAlias(wrr_handle, "wrr_dyn")
set_object_dyn(wrr_handle)
sim.computeMassAndInertia(wrr_handle, 1)



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
sim.setObjectPosition(wrl_handle, [1.0624865293502808, 1.164986491203308, 0.27424795389175415], sim.handle_world)
sim.setObjectAlias(wrl_handle, "wrl_dyn")
set_object_dyn(wrl_handle)
sim.computeMassAndInertia(wrl_handle, 1)



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
sim.computeMassAndInertia(wfr_handle, 1)



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
sim.computeMassAndInertia(wfl_handle, 1)



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
sim.computeMassAndInertia(wmr_handle, 1)



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
sim.computeMassAndInertia(wml_handle, 1)



handle = sim.getObject("/SuspensionRearRight")
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
srr_diameter = 0.434/2
srr_thickness = 1.306514
srr_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [srr_diameter, srr_diameter, srr_thickness], options)
sim.setObjectOrientation(srr_handle, [math.radians(112.67314680986536), math.radians(0.9008132484742495), math.radians(151.81799298369745)], sim.handle_world)
sim.setObjectPosition(srr_handle, [-0.9769465923309326, 0.6021621823310852, 0.596157431602478], sim.handle_world)
sim.setObjectAlias(srr_handle, "srr_dyn")
set_object_dyn(srr_handle)
sim.computeMassAndInertia(srr_handle, 1)



handle = sim.getObject("/SuspensionRearLeft")
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
srl_diameter = 0.434/2
srl_thickness = 1.306514
srl_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [srl_diameter, srl_diameter, srl_thickness], options)
sim.setObjectOrientation(srl_handle, [math.radians(112.67314680986536), math.radians(0.9008132484742495), math.radians(151.81799298369745)], sim.handle_world)
sim.setObjectPosition(srl_handle, [0.9769465923309326, 0.6021621823310852, 0.596157431602478], sim.handle_world)
sim.setObjectAlias(srl_handle, "srl_dyn")
set_object_dyn(srl_handle)
sim.computeMassAndInertia(srl_handle, 1)


handle = sim.getObject("/SuspensionFrontRight")
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
sfr_diameter = 0.389/2
sfr_thickness = 1.821
sfr_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [sfr_diameter, sfr_diameter, sfr_thickness], options)
sim.setObjectOrientation(sfr_handle, [math.radians(-92.39560379813177), math.radians(7.605833825459014), math.radians(-169.4107417321115)], sim.handle_world)
sim.setObjectPosition(sfr_handle, [-0.8669474720954895, -0.2909966707229614, 0.802253782749176], sim.handle_world)
sim.setObjectAlias(sfr_handle, "sfr_dyn")
set_object_dyn(sfr_handle)
sim.computeMassAndInertia(sfr_handle, 1)


handle = sim.getObject("/SuspensionFrontLeft")
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
sfl_diameter = 0.389/2
sfl_thickness = 1.821
sfl_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [sfl_diameter, sfl_diameter, sfl_thickness], options)
sim.setObjectOrientation(sfl_handle, [math.radians(87.60438482676204), math.radians(7.605747404266133), math.radians(10.589331500171427)], sim.handle_world)
sim.setObjectPosition(sfl_handle, [0.8669472932815552, -0.2909965515136719, 0.802253782749176], sim.handle_world)
sim.setObjectAlias(sfl_handle, "sfl_dyn")
set_object_dyn(sfl_handle)
sim.computeMassAndInertia(sfl_handle, 1)


handle = sim.getObject("/WheelAttachRearRight")
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
warr_diameter = 0.1
warr_thickness = 0.3437/2
warr_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [warr_diameter, warr_diameter, warr_thickness], options)
sim.setObjectOrientation(warr_handle, [math.radians(0), math.radians(-0.46338811018134884), math.radians(0.7933965215763155)], sim.handle_world)
sim.setObjectPosition(warr_handle, [-1.0624862909317017, 1.164980173110962, 0.67345884799957275], sim.handle_world)
sim.setObjectAlias(warr_handle, "warr_dyn")
set_object_dyn(warr_handle)
sim.computeMassAndInertia(warr_handle, 1)


handle = sim.getObject("/WheelAttachRearLeft")
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
walr_diameter = 0.1
walr_thickness = 0.3437/2
warl_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [walr_diameter, walr_diameter, walr_thickness], options)
sim.setObjectOrientation(warl_handle, [math.radians(0), math.radians(-0.46338811018134884), math.radians(0.7933965215763155)], sim.handle_world)
sim.setObjectPosition(warl_handle, [1.0624865293502808, 1.164986491203308, 0.67345860958099365], sim.handle_world)
sim.setObjectAlias(warl_handle, "walr_dyn")
set_object_dyn(warl_handle)
sim.computeMassAndInertia(warl_handle, 1)


handle = sim.getObject("/WheelAttachFrontRight")
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
wafr_diameter = 0.1
wafr_thickness = 0.3437/2
wafr_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wafr_diameter, wafr_diameter, wafr_thickness], options)
sim.setObjectOrientation(wafr_handle, [math.radians(0), math.radians(-0.46338811018134884), math.radians(0.7933965215763155)], sim.handle_world)
sim.setObjectPosition(wafr_handle, [-1.0624862909317017, -1.0949854850769043, 0.66345860958099365], sim.handle_world)
sim.setObjectAlias(wafr_handle, "wafr_dyn")
set_object_dyn(wafr_handle)
sim.computeMassAndInertia(wafr_handle, 1)


handle = sim.getObject("/WheelAttachFrontLeft")
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
wafl_diameter = 0.1
wafl_thickness = 0.3437/2
wafl_handle = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [wafl_diameter, wafl_diameter, wafl_thickness], options)
sim.setObjectOrientation(wafl_handle, [math.radians(0), math.radians(-0.46338811018134884), math.radians(0.7933965215763155)], sim.handle_world)
sim.setObjectPosition(wafl_handle, [1.0624865293502808, -1.0949794054031372, 0.66424771547317505], sim.handle_world)
sim.setObjectAlias(wafl_handle, "wafl_dyn")
set_object_dyn(wafl_handle)
sim.computeMassAndInertia(wafl_handle, 1)




# Création d'une articulation pivot horizontale : moteur de la roue arrière droite


options = 0
sizes = [0.15, 0.02]
wrr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wrr_motor_handle, "wrr_motor")
sim.setObjectOrientation(wrr_motor_handle, [0, -math.pi/2.0, 0], wrr_motor_handle)
position = sim.getObjectPosition(wrr_handle, sim.handle_world)
sim.setObjectPosition(wrr_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue arrière gauche


options = 0
sizes = [0.15, 0.02]
wrl_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wrl_motor_handle, "wrl_motor")
sim.setObjectOrientation(wrl_motor_handle, [0, -math.pi/2.0, 0], wrl_motor_handle)
position = sim.getObjectPosition(wrl_handle, sim.handle_world)
sim.setObjectPosition(wrl_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue avant droite


options = 0
sizes = [0.15, 0.02]
wfr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wfr_motor_handle, "wfr_motor")
sim.setObjectOrientation(wfr_motor_handle, [0, -math.pi/2.0, 0], wfr_motor_handle)
position = sim.getObjectPosition(wfr_handle, sim.handle_world)
sim.setObjectPosition(wfr_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue avant gauche


options = 0
sizes = [0.15, 0.02]
wfl_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wfl_motor_handle, "wfl_motor")
sim.setObjectOrientation(wfl_motor_handle, [0, -math.pi/2.0, 0], wfl_motor_handle)
position = sim.getObjectPosition(wfl_handle, sim.handle_world)
sim.setObjectPosition(wfl_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue milieu droite


options = 0
sizes = [0.15, 0.02]
wmr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wmr_motor_handle, "wmr_motor")
sim.setObjectOrientation(wmr_motor_handle, [0, -math.pi/2.0, 0], wmr_motor_handle)
position = sim.getObjectPosition(wmr_handle, sim.handle_world)
sim.setObjectPosition(wmr_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : moteur de la roue milieu gauche


options = 0
sizes = [0.15, 0.02]
wml_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wml_motor_handle, "wml_motor")
sim.setObjectOrientation(wml_motor_handle, [0, -math.pi/2.0, 0], wml_motor_handle)
position = sim.getObjectPosition(wml_handle, sim.handle_world)
sim.setObjectPosition(wml_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : pivot de la suspension arrière droite


options = 0
sizes = [0.15, 0.02]
srr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(srr_motor_handle, "srr_motor")
sim.setObjectOrientation(srr_motor_handle, [0, -math.pi/2.0, 0], srr_motor_handle)
position = sim.getObjectPosition(srr_handle, sim.handle_world)
position[1] = position[1] - 0.07
position[2] = position[2] + 0.07
sim.setObjectPosition(srr_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : pivot de la suspension arrière gauche


options = 0
sizes = [0.15, 0.02]
srl_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(srl_motor_handle, "srl_motor")
sim.setObjectOrientation(srl_motor_handle, [0, -math.pi/2.0, 0], srl_motor_handle)
position = sim.getObjectPosition(srl_handle, sim.handle_world)
position[1] = position[1] - 0.07
position[2] = position[2] + 0.07
sim.setObjectPosition(srl_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : pivot de la suspension avant droite


options = 0
sizes = [0.15, 0.02]
sfr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(sfr_motor_handle, "sfr_motor")
sim.setObjectOrientation(sfr_motor_handle, [0, -math.pi/2.0, 0], sfr_motor_handle)
position = sim.getObjectPosition(sfr_handle, sim.handle_world)
position[1] = position[1] + 0.075
position[2] = position[2] + 0.125
sim.setObjectPosition(sfr_motor_handle, position, sim.handle_world)

# Création d'une articulation pivot horizontale : pivot de la suspension avant gauche


options = 0
sizes = [0.15, 0.02]
sfl_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(sfl_motor_handle, "sfl_motor")
sim.setObjectOrientation(sfl_motor_handle, [0, -math.pi/2.0, 0], sfl_motor_handle)
position = sim.getObjectPosition(sfl_handle, sim.handle_world)
position[1] = position[1] + 0.075
position[2] = position[2] + 0.125
sim.setObjectPosition(sfl_motor_handle, position, sim.handle_world)


# Création d'une articulation pivot horizontale : pivot2 de la roue arrière droite


options = 0
sizes = [0.15, 0.02]
warr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(warr_motor_handle, "warr_motor")
sim.setObjectOrientation(warr_motor_handle, [0, 0, 0], warr_motor_handle)
position = sim.getObjectPosition(warr_handle, sim.handle_world)
sim.setObjectPosition(warr_motor_handle, position, sim.handle_world)


# Création d'une articulation pivot horizontale : pivot2 de la roue arrière gauche


options = 0
sizes = [0.15, 0.02]
walr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(walr_motor_handle, "walr_motor")
sim.setObjectOrientation(walr_motor_handle, [0, 0, 0], walr_motor_handle)
position = sim.getObjectPosition(warl_handle, sim.handle_world)
sim.setObjectPosition(walr_motor_handle, position, sim.handle_world)


# Création d'une articulation pivot horizontale : pivot2 de la roue avant droite


options = 0
sizes = [0.15, 0.02]
wafr_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wafr_motor_handle, "wafr_motor")
sim.setObjectOrientation(wafr_motor_handle, [0, 0, 0], wafr_motor_handle)
position = sim.getObjectPosition(wafr_handle, sim.handle_world)
sim.setObjectPosition(wafr_motor_handle, position, sim.handle_world)


# Création d'une articulation pivot horizontale : pivot2 de la roue avant gauche


options = 0
sizes = [0.15, 0.02]
wafl_motor_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wafl_motor_handle, "wafl_motor")
sim.setObjectOrientation(wafl_motor_handle, [0, 0, 0], wafl_motor_handle)
position = sim.getObjectPosition(wafl_handle, sim.handle_world)
sim.setObjectPosition(wafl_motor_handle, position, sim.handle_world)


# Création d'une articulation pivot horizontale : Attache de la roue arrière droite


options = 0
sizes = [0.15, 0.02]
warr_pivot_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(warr_pivot_handle, "warr_pivot")
sim.setObjectOrientation(warr_pivot_handle, [0, -math.pi/2.0, 0], warr_pivot_handle)
position = sim.getObjectPosition(warr_handle, sim.handle_world)
sim.setObjectPosition(warr_pivot_handle, position, sim.handle_world)


# Création d'une articulation pivot horizontale : Attache de la roue arrière gauche


options = 0
sizes = [0.15, 0.02]
walr_pivot_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(walr_pivot_handle, "walr_pivot")
sim.setObjectOrientation(walr_pivot_handle, [0, -math.pi/2.0, 0], walr_pivot_handle)
position = sim.getObjectPosition(warl_handle, sim.handle_world)
sim.setObjectPosition(walr_pivot_handle, position, sim.handle_world)


# Création d'une articulation pivot horizontale : Attache de la roue avant droite


options = 0
sizes = [0.15, 0.02]
wafr_pivot_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wafr_pivot_handle, "wafr_pivot")
sim.setObjectOrientation(wafr_pivot_handle, [0, -math.pi/2.0, 0], wafr_pivot_handle)
position = sim.getObjectPosition(wafr_handle, sim.handle_world)
sim.setObjectPosition(wafr_pivot_handle, position, sim.handle_world)


# Création d'une articulation pivot horizontale : Attache de la roue avant gauche


options = 0
sizes = [0.15, 0.02]
wafl_pivot_handle = sim.createJoint(sim.joint_revolute_subtype, sim.jointmode_dynamic, options, sizes)
sim.setObjectAlias(wafl_pivot_handle, "wafl_pivot")
sim.setObjectOrientation(wafl_pivot_handle, [0, -math.pi/2.0, 0], wafl_pivot_handle)
position = sim.getObjectPosition(wafl_handle, sim.handle_world)
sim.setObjectPosition(wafl_pivot_handle, position, sim.handle_world)


# Assemblage du robot, création de l’arbre de description

keep_in_place = True

sim.setObjectParent(sfr_motor_handle, body_handle, keep_in_place)
sim.setObjectParent(sfl_motor_handle, body_handle, keep_in_place)

sim.setObjectParent(sfr_handle, sfr_motor_handle, keep_in_place)
sim.setObjectParent(sfl_handle, sfl_motor_handle, keep_in_place)

sim.setObjectParent(srr_motor_handle, sfr_handle, keep_in_place)
sim.setObjectParent(srl_motor_handle, sfl_handle, keep_in_place)
sim.setObjectParent(wfr_motor_handle, sfr_handle, keep_in_place)
sim.setObjectParent(wfl_motor_handle, sfl_handle, keep_in_place)

sim.setObjectParent(srr_handle, srr_motor_handle, keep_in_place)
sim.setObjectParent(srl_handle, srl_motor_handle, keep_in_place)

sim.setObjectParent(wrr_motor_handle, srr_handle, keep_in_place)
sim.setObjectParent(wrl_motor_handle, srl_handle, keep_in_place)
sim.setObjectParent(wmr_motor_handle, srr_handle, keep_in_place)
sim.setObjectParent(wml_motor_handle, srl_handle, keep_in_place)

sim.setObjectParent(wrr_handle, wrr_motor_handle, keep_in_place)
sim.setObjectParent(wrl_handle, wrl_motor_handle, keep_in_place)
sim.setObjectParent(wfr_handle, wfr_motor_handle, keep_in_place)
sim.setObjectParent(wfl_handle, wfl_motor_handle, keep_in_place)
sim.setObjectParent(wmr_handle, wmr_motor_handle, keep_in_place)
sim.setObjectParent(wml_handle, wml_motor_handle, keep_in_place)

sim.setObjectParent(warr_pivot_handle, srr_handle, keep_in_place)
sim.setObjectParent(walr_pivot_handle, srl_handle, keep_in_place)
sim.setObjectParent(wafr_pivot_handle, sfr_handle, keep_in_place)
sim.setObjectParent(wafl_pivot_handle, sfl_handle, keep_in_place)

sim.setObjectParent(warr_handle, warr_pivot_handle, keep_in_place)
sim.setObjectParent(warl_handle, walr_pivot_handle, keep_in_place)
sim.setObjectParent(wafr_handle, wafr_pivot_handle, keep_in_place)
sim.setObjectParent(wafl_handle, wafl_pivot_handle, keep_in_place)

sim.setObjectParent(warr_motor_handle, warr_handle, keep_in_place)
sim.setObjectParent(walr_motor_handle, warl_handle, keep_in_place)
sim.setObjectParent(wafr_motor_handle, wafr_handle, keep_in_place)
sim.setObjectParent(wafl_motor_handle, wafl_handle, keep_in_place)



sim.setObjectParent(sim.getObject("/WheelRearRight"), wrr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelRearLeft"), wrl_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelFrontRight"), wfr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelFrontLeft"), wfl_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelMidRight"), wmr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelMidLeft"), wml_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/Body"), body_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/SuspensionTop"), body_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/SuspensionRearRight"), srr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/SuspensionRearLeft"), srl_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/SuspensionFrontRight"), sfr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/SuspensionFrontLeft"), sfl_handle, keep_in_place)

sim.setObjectParent(sim.getObject("/WheelAttachRearRight"), warr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelAttachRearLeft"), warl_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelAttachFrontRight"), wafr_handle, keep_in_place)
sim.setObjectParent(sim.getObject("/WheelAttachFrontLeft"), wafl_handle, keep_in_place)

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

sim.setObjectInt32Param(srr_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(srl_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(sfr_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(sfl_handle,sim.objintparam_visibility_layer,0)

sim.setObjectInt32Param(srr_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(srl_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(sfr_motor_handle,sim.objintparam_visibility_layer,0)
sim.setObjectInt32Param(sfl_motor_handle,sim.objintparam_visibility_layer,0)

