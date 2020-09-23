import airsim


client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

print("arming the drone...")
client.armDisarm(True)

state = client.getMultirotorState()
client.takeoffAsync().join()

state = client.getMultirotorState()

# AirSim uses NED coordinates so negative axis is up.
# z of -7 is 7 meters above the original launch point.
z = -3
print("make sure we are hovering at 7 meters...")
client.moveToZAsync(z, 1).join()

print("flying on path...")
client.moveOnPathAsync([airsim.Vector3r(0,0,z),airsim.Vector3r(-5,0,z),airsim.Vector3r(-7,-40,z),airsim.Vector3r(-43,-40,z)], 5).join()
client.moveToPositionAsync(-50,-30,z,2).join()


print("landing...")
client.landAsync().join()