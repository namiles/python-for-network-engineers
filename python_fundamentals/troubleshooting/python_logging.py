"""
Logging is great for logging information about what is happening when running a script. 

Logging Levels (decreasing severity order)
- Critical
- Error
- Warning
- Info
- Debug

When loggig with logging levels, logs will be created at the speciied level AND everythig above.
For exampling, logging at Critical will ONLY log criticals. Logging at debug will be everything.

"""

import logging
from scrapli.driver.core import IOSXEDriver
from scrapli.driver.core import JunosDriver


def main():
    logging.basicConfig(filename="logging_example.txt", level=logging.DEBUG)

    ios_xe = {
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "auth_username": "developer",
        "auth_password": "C1sco12345",  # This password is publicly available.
        "auth_strict_key": False,
    }

    try:
        # Using the wrong drvier on purpose to use with logging
        with IOSXEDriver(**ios_xe) as conn:
            prompt = conn.get_prompt()
            response = conn.send_command("show ip int brief")

        print(prompt)
        print(response.result)

    except Exception:
        print("Something went wrong. Check log file.")


if __name__ == "__main__":
    main()
