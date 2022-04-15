from scrapli.driver.core import IOSXEDriver

"""
Sending configuration commands with Scrapli

send_config - Acepts a string
send_configs - Accepts a list of strings
send_configs_from_file - Accepts a path to a file

"""


def main():
    devices = [
        {  # R1
            "host": "192.168.40.99",
            "auth_username": "cisco",
            "auth_password": "cisco123",
            "auth_strict_key": False,
        },
        {  # R2
            "host": "192.168.40.148",
            "auth_username": "cisco",
            "auth_password": "cisco123",
            "auth_strict_key": False,
        },
        {  # R3
            "host": "192.168.40.227",
            "auth_username": "cisco",
            "auth_password": "cisco123",
            "auth_strict_key": False,
        },
    ]

    ospf_config = [
        "router ospf 1",
        "passive-interface GigabitEthernet 1",
        "network 0.0.0.0 0.0.0.0 area 0"
    ]

    for device in devices:
        with IOSXEDriver(**device) as conn:
            response = conn.send_configs(ospf_config)
        print(response.result)


if __name__ == "__main__":
    main()
