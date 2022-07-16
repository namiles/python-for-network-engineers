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

    """
    There is no need to call the disconnect needed when using a context manager.
    It will automatically call the disconnect method when finished.
    """
    with ConnectHandler(**ios_xe) as net_connect:
        output = net_connect.send_command("show ip int brief")

    print(output)


if __name__ == "__main__":
    main()
