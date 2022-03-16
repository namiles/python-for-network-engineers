from scrapli import Scrapli

def main():
    DEVICE_DICT = {
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "auth_username": "developer",
        "auth_password": "C1sco12345", # This password is publicly available.
        "auth_strict_key": False,
        "platform": "cisco_iosxe"
    }

    with Scrapli(**DEVICE_DICT) as conn:
        prompt = conn.get_prompt()
        response = conn.send_command("show ip int brief")
    
    print(prompt)
    print(response.result)


if __name__ == "__main__":
    main()