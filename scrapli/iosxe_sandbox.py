from scrapli import Scrapli

"""
This example uses Scrapli's factory class to dybanically select the approriate driver
(IOSXEDriver, NXOSDriver, etc) based on the platform string in the below dictionary.

Platform options:
- cisco_iosxe
- cisco_nxos
- cisco_iosxr
- arista_eos
- juniper_junos

See iosxe_driver_example.py for an example uisng the IOSXEDriver with the DevNet sandbox.
"""


def main():
    ios_xe = {
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "auth_username": "developer",
        "auth_password": "C1sco12345",  # This password is publicly available.
        "auth_strict_key": False,
        "platform": "cisco_iosxe",
    }

    with Scrapli(**ios_xe) as conn:
        prompt = conn.get_prompt()
        response = conn.send_command("show ip int brief")

    print(prompt)
    print(response.result)


if __name__ == "__main__":
    main()
