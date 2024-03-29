from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import os
import math
from numpy import *
client = RemoteAPIClient()
sim = client.require('sim')


sim.setStepping(True)


sim.startSimulation()


# Prendre le contrôle du moteur


motor_right = sim.getObject('/wmr_motor')
motor_right_front = sim.getObject('/wfr_motor')
motor_left = sim.getObject('/wml_motor')
motor_left_front = sim.getObject('/wfl_motor')
motor_left_rear = sim.getObject('/wrl_motor')
motor_right_rear = sim.getObject('/wrr_motor')


# Contrôler le moteur avec une vitesse angulaire
sim.setObjectInt32Param(motor_right, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)
sim.setObjectInt32Param(motor_left, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)
sim.setObjectInt32Param(motor_right_front, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)
sim.setObjectInt32Param(motor_left_front, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)
sim.setObjectInt32Param(motor_left_rear, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)
sim.setObjectInt32Param(motor_right_rear, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)


# Définir une vitesse angulaire cible
target_velocity = math.radians(-30)  # rad/s
motion_params = []  # Paramètres par défaut


# Avancer pendant 2 secondes
sim.setJointTargetVelocity(motor_right, target_velocity, motion_params)
sim.setJointTargetVelocity(motor_left, target_velocity, motion_params)
sim.setJointTargetVelocity(motor_left_front, target_velocity, motion_params)
sim.setJointTargetVelocity(motor_right_front, target_velocity, motion_params)
sim.setJointTargetVelocity(motor_left_rear, target_velocity, motion_params)
sim.setJointTargetVelocity(motor_right_rear, target_velocity, motion_params)


t0 = sim.getSimulationTime()
while (sim.getSimulationTime() - t0) < 5:
   sim.step()
sim.setJointTargetVelocity(motor_right, 0, motion_params)
sim.setJointTargetVelocity(motor_left, 0, motion_params)
sim.setJointTargetVelocity(motor_left_front, 0, motion_params)
sim.setJointTargetVelocity(motor_right_front, 0, motion_params)
sim.setJointTargetVelocity(motor_left_rear, 0, motion_params)
sim.setJointTargetVelocity(motor_right_rear, 0, motion_params)


# Attendre 5 secondes
t0 = sim.getSimulationTime()
while (sim.getSimulationTime() - t0) < 5:
   sim.step()


# Tourner à gauche pendant 2 secondes
sim.setJointTargetVelocity(motor_right, target_velocity, motion_params)
sim.setJointTargetVelocity(motor_left, -target_velocity, motion_params)
sim.setJointTargetVelocity(motor_left_front, -target_velocity, motion_params)
sim.setJointTargetVelocity(motor_right_front, target_velocity, motion_params)
sim.setJointTargetVelocity(motor_left_rear, -target_velocity, motion_params)
sim.setJointTargetVelocity(motor_right_rear, target_velocity, motion_params)


t0 = sim.getSimulationTime()
while (sim.getSimulationTime() - t0) < 10:
   sim.step()
sim.setJointTargetVelocity(motor_right, 0, motion_params)
sim.setJointTargetVelocity(motor_left, 0, motion_params)
sim.setJointTargetVelocity(motor_left_front, 0, motion_params)
sim.setJointTargetVelocity(motor_right_front, 0, motion_params)
sim.setJointTargetVelocity(motor_left_rear, 0, motion_params)
sim.setJointTargetVelocity(motor_right_rear, 0, motion_params)



sim.stopSimulation()