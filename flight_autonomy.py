from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

vehicle = connect('/dev/ttyAMA0', baud=57600, wait_ready=True)

def arm_and_takeoff(altitude):
    print("Arming motors...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed:
        time.sleep(1)
    print("Taking off...")
    vehicle.simple_takeoff(altitude)
    while True:
        print(f"Altitude: {vehicle.location.global_relative_frame.alt}")
        if vehicle.location.global_relative_frame.alt >= altitude * 0.95:
            print("Target altitude reached")
            break
        time.sleep(1)

def land_drone():
    print("Landing...")
    vehicle.mode = VehicleMode("LAND")
    time.sleep(5)
    vehicle.close()

arm_and_takeoff(10)
time.sleep(10)
land_drone()
