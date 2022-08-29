from robotAPI import Robot
import time


# test camera
instance = Robot()

instance.camera_move("up", duration=2)

instance.camera_move("down", duration=2)

instance.camera_move("left", duration=2)

instance.camera_move("right", duration=2)

# test motor at different speed plus a wrong parameter
speeds = {"slow", "med", "fast"}

for speed_i in speeds:
    print(speed_i)
    instance = Robot(speed=speed_i)

    instance.motor_move("forward", duration=2)

    instance.motor_move("backward", duration=2)

    instance.motor_move("left", duration=2)

    instance.motor_move("right", duration=2)

# test wrong ip
instance = Robot("172.16.42.254")

