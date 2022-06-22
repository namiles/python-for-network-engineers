from concurrent.futures import ProcessPoolExecutor
from time import perf_counter
from netmiko import ConnectHandler
from devices import network_devices

start = perf_counter()

def send_commands_to_devices(device):
    device_dict = {
        "device_type": "cisco_ios",
        "host": f"{device['ip']}",
        "username": "nmiles",
        "password": "cisco"
    }

    with ConnectHandler(**device_dict) as net_connect:
        net_connect.enable()
        output = net_connect.send_command("show ip int brief")
        #print(output)
        return output


if __name__ == "__main__":
    with ProcessPoolExecutor() as exectuor:
        results = exectuor.map(send_commands_to_devices, network_devices)

    for result in results:
        print(result)

    end = perf_counter()
    total_time = end - start
    print(total_time)