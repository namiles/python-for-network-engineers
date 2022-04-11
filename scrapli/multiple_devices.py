from scrapli.driver.core import IOSXEDriver

"""
This example uses three Cisco csr1000v devices I have in a simulated lab.

R1 = 192.168.40.99
R2 = 192.168.40.148
R3 = 192.168.40.227
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

    for device in devices:
        with IOSXEDriver(**device) as conn:
            prompt = conn.get_prompt()
            response = conn.send_command("show ip int brief")
        print(prompt)
        print(response.result)
        print()


if __name__ == "__main__":
    main()
