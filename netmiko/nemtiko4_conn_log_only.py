from netmiko import (
    ConnectHandler,
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)
from netmiko import ConnLogOnly


def main():

    device = {
        "device_type": "cisco_xe",
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco123456",
        "port": 22,
    }

    """
    - ConLogOnly is a new factory function in Netmiko 4.x that allows the use to catch common Netmiko errors
      without using a large try..except block.
    - ConnLogOnly can replace ConnectHandler.
    - ConnLogOnly either returns a Netmiko object, or None if the connection fails
    - Generate a log file when failures occur
    """

    # Before:
    # try:
    #     conn = ConnectHandler(**device)
    #     print(conn.find_prompt())
    # except NetMikoAuthenticationException:
    #     # do something / log failure
    #     return
    # except NetMikoTimeoutException:
    #     # do something / log failure
    #     return
    # except Exception:
    #     # Unknown exception: do something / log failure
    #     return

    # With ConnLogOnly:
    ssh = ConnLogOnly(**device)
    if ssh is not None:
        print("Logging into the device succeeded")
        print(ssh.find_prompt())

        # ConnLogOnly does not current support context managers
        # You must explicity call the disconnect method compared to ConnectHandler
        ssh.disconnect()
    if ssh is None:
        print("Logging into the device failed.")


if __name__ == "__main__":
    main()
