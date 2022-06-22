from multiprocessing import Process
from time import perf_counter
from netmiko import ConnectHandler
from devices import network_devices


def send_commands_to_devices(device):
    device_dict = {
        "device_type": "cisco_ios",
        "host": f"{device['ip']}",
        "username": "nmiles",
        "password": "cisco",
        "port": 22,
    }

    with ConnectHandler(**device_dict) as net_connect:
        net_connect.enable()
        output = net_connect.send_command("show ip int brief")
        print(output)


def main():
    start = perf_counter()
    processes = []

    for device in network_devices:
        # send_commands_to_devices(device=device)
        # vs.
        # Because the send_commands_to_devices function takes an argument, we must specify that in the Process class arguments.
        proc = Process(target=send_commands_to_devices, args=(device,))
        processes.append(proc)

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()

    end = perf_counter()
    total_time = end - start
    print(total_time)


if __name__ == "__main__":
    main()