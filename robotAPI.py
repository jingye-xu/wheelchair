import requests
import time
import os
import sys


def check_connections(ip: str) -> bool:
    res = os.system("ping -c 1 " + ip)
    return True if res == 0 else False


class Robot:
    def __init__(self, ip: str = "192.168.0.250", speed: str = "med"):

        if not check_connections(ip):
            print("Cannot")
            sys.exit(1)
        print("Pass")


if __name__ == "__main__":
    instance = Robot()
    param = {
        "action": "command",
        "command": "move_command",
        "value": "537575426",
    }
    res = requests.get("http://192.168.0.250:8080/", params=param)
    print(res)
    time.sleep(2)
    res = requests.get("http://192.168.0.250:8080/?action=command&command=move_command&value=0")
    print(res)
