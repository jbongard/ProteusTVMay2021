import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

p.loadSDF("box.sdf")

for t in range(0,1000):

   p.stepSimulation()

   timeInSecondsToSleepFor = 1. / 600.

   time.sleep( timeInSecondsToSleepFor )

   # print('Timestep: ' , t )

p.disconnect()

