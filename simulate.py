import pybullet as p
import time

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

for t in range(0,1000):

   p.stepSimulation()

   timeInSecondsToSleepFor = 1. / 60.

   time.sleep( timeInSecondsToSleepFor )

   print('Timestep: ' , t )

p.disconnect()

