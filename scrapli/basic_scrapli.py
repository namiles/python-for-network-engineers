from scrapli.driver.core import IOSXEDriver

"""
This example shows basic Scrapli usage without using a context manager.
"""


def main():
    # Device
    ios_xe = {
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "auth_username": "developer",
        "auth_password": "C1sco12345",  # This password is publicly available.
        "auth_strict_key": False,
    }

    conn = IOSXEDriver(**ios_xe)

    # Open the connection
    conn.open()

    # Issue the "show ip int brief" command and print its output
    response = conn.send_command("show ip int brief")
    print(response.result)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()
