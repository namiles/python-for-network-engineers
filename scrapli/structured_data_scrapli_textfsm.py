import json
from scrapli import Scrapli

"""
Scrapli supports both TextFSM and Genie for parsing command output into structured data.

This example uses textfsm to parse the "show ip int brief" command.
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
        response = conn.send_command("show ip int brief")
        parsed_output = response.textfsm_parse_output()

    print(json.dumps(parsed_output, indent=4))

    for interface in parsed_output:
        print(f"{interface['intf']} has an IP Address of {interface['ipaddr']}")


if __name__ == "__main__":
    main()
