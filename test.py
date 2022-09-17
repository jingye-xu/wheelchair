from robotAPI import Robot, xy2value, value2xy
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

# test transform between x, y and value
values = [65536, 655360, 6553600, 536903680, 537575426, 548339722, 10, 65566, 98429, 81929, 114712, 536985728]

for i in values:
    x, y = value2xy(i)
    print(f"x, y: {x, y}")
    value = xy2value(x, y)
    print(f"value: {value}")

# test wrong ip
instance = Robot("172.16.42.254")