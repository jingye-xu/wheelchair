import requests
import time
import sys


motor_param = {
    "action": "command",
    "command": "move_command",
    "value": "",
}


camera_param = {
    "action": "command",
    "command": "",
}


speed_values = {
    "slow": {
        "forward": "65536",
        "backward": "536903680",
        "left": "10",
        "right": "81929",
    },
    "med": {
        "forward": "655360",
        "backward": "537575426",
        "left": "65566",
        "right": "114712",
    },
    "fast": {
        "forward": "6553600",
        "backward": "548339722",
        "left": "98429",
        "right": "536985728",
    },
}


class Robot:
    def __init__(self, ip: str = "192.168.0.250", speed: str = "med", retry: int = 3):
        """
        initialization, check access to robot server, set motor speed
        :param ip: server ip
        :param speed: define motor speed: fast, med, slow
        :param retry: retry times
        """

        self.url = f"http://{ip}:8080/"
        self.retry = retry

        try:
            res = requests.get(self.url)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print("Connection error! Make sure connect to the right Wi-Fi.")
            print(e)
            sys.exit(1)

        speeds = {"slow", "med", "fast"}
        if speed not in speeds:
            sys.exit(1)

        self.speed = speed_values[speed]

    def camera_stop(self):
        """
        stop camera
        """

        # pass parameters
        camera_param_stop = camera_param
        camera_param_stop["command"] = "cam_stop_up"
        res = requests.get(self.url, params=camera_param_stop)

        # retry
        current_try = 0
        while not res.ok and current_try < self.retry:
            print(f"retry to stop camera")
            res = requests.get(self.url, params=camera_param_stop)
            current_try += 1

    def camera_move(self, direction: str, duration: int = 0):
        """
        move camera up, down, left, and right
        :param direction: camera move direction, must be in {"up", "down", "left", "right"}
        :param duration: 0 for continuously move, not 0 for duration in seconds
        """

        # valid inputs of direction
        directions = {"up", "down", "left", "right"}

        # check input validation
        if direction not in directions:
            return

        # pass parameters
        camera_param_move = camera_param
        camera_param_move["command"] = f"cam_{direction}_up"

        # GET
        res = requests.get(self.url, params=camera_param_move)

        # retry
        current_try = 0
        while not res.ok and current_try < self.retry:
            print(f"retry to move camera")
            res = requests.get(self.url, params=camera_param_move)
            current_try += 1

        # if defined a duration
        if duration > 0:
            time.sleep(duration)
            self.camera_stop()

    def motor_stop(self):
        """
        stop the motor
        """

        motor_param_stop = motor_param
        motor_param_stop["value"] = "0"
        res = requests.get(self.url, params=motor_param_stop)

        current_try = 0
        while not res.ok and current_try < self.retry:
            print(f"retry to stop motor")
            res = requests.get(self.url, params=motor_param_stop)
            current_try += 1

    def motor_move(self, direction: str, duration: int = 0):
        """
        move robot forward, backward, left, and right
        :param direction: robot move directions, must be in {"forward", "backward", "left", "right"}
        :param duration: 0 for continuously move, not 0 for duration in seconds
        """

        # valid inputs of direction
        directions = {"forward", "backward", "left", "right"}

        # check input validation
        if direction not in directions:
            return

        # pass parameters
        motor_param_move = motor_param
        motor_param_move["value"] = self.speed[direction]

        # GET
        res = requests.get(self.url, params=motor_param_move)

        # retry
        current_try = 0
        while not res.ok and current_try < self.retry:
            print(f"retry to move motor")
            res = requests.get(self.url, params=motor_param_move)
            current_try += 1

        # if defined a duration
        if duration > 0:
            time.sleep(duration)
            self.motor_stop()


if __name__ == "__main__":
    instance = Robot()

    instance.camera_move("up")
    time.sleep(2)
    instance.camera_stop()

    instance.camera_move("down")
    time.sleep(2)
    instance.camera_stop()

    instance.camera_move("left")
    time.sleep(2)
    instance.camera_stop()

    instance.camera_move("right", 2)

    instance.motor_move("forward")
    time.sleep(2)
    instance.motor_stop()

    instance.motor_move("backward")
    time.sleep(2)
    instance.motor_stop()

    instance.motor_move("left")
    time.sleep(2)
    instance.motor_stop()

    instance.motor_move("right")
    time.sleep(2)
    instance.motor_stop()

    instance.motor_move("forward", 2)
