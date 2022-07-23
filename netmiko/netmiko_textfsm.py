import json
from netmiko import ConnectHandler


def main():
    # Create a device dictionary
    ios_xe = {
        "device_type": "cisco_xe",
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22,
    }

    with ConnectHandler(**ios_xe) as net_connect:
        # textfsm is built into netmiko, and can be used to parse command output into structured data
        output = net_connect.send_command("show ip int brief", use_textfsm=True)

    # Print in pretty format
    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
