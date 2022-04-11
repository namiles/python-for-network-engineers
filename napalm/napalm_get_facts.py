from dbm import dumb
import json
from textwrap import indent
from napalm import get_network_driver

"""
Napalm Getters

Can be used to get information from a multi-vendor stacl of devices.
Does not have show commands for everything

"""


def main():
    devices = [
        {  # R1
            "hostname": "192.168.40.99",
            "username": "cisco",
            "password": "cisco123",
            "driver": "ios",
        },
        {  # R2
            "hostname": "192.168.40.148",
            "username": "cisco",
            "password": "cisco123",
            "driver": "ios",
        },
        {  # R3
            "hostname": "192.168.40.227",
            "username": "cisco",
            "password": "cisco123",
            "driver": "ios",
        },
    ]

    for device in devices:
        driver = get_network_driver(device["driver"])
        with driver(
            username=device["username"],
            password=device["password"],
            hostname=device["hostname"],
        ) as device:
            result = device.get_facts()
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
