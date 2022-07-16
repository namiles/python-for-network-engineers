import asyncio
from types import coroutine
from black import out
from netmiko import ConnectHandler
from time import perf_counter
from devices import network_devices

start = perf_counter()

# def run_commands(device):
#     with ConnectHandler(**device) as ssh:
#         output = ssh.send_command("show interfaces description")
#         print(output)

# await keyword can be used anywhere where an I/O task is happening, such as running commands on a device
async def run_commands(device):
    device_dict = {
        "device_type":"cisco_ios",
        "host":f"{device['ip']}",
        "username":"nmiles",
        "password":"cisco"
    }
    with ConnectHandler(**device_dict) as ssh:
        output = ssh.send_command("show interfaces description")
        print(output)

async def main():
    start = perf_counter()

    coroutines = [run_commands(device) for device in network_devices]
    await asyncio.gather(*coroutines)

    end = perf_counter()
    print("Total time taken:",end-start)

if __name__ == "__main__":
    asyncio.run(main())


