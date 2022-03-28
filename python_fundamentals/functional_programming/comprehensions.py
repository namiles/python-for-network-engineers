"""
Comprehensions are used to create new sequences using already defined sequences.
This can be done with lists, dcts, or sets.

This is an example of using list and Dict comprehensions.
"""


def main():

    # Using List Comprehensions - Creating a new list the traditional way
    interface_list = [
        "Loopback0",
        "Loopback1",
        "GigabitEthernet0/0",
        "GigabitEthernet0/1",
    ]

    # gig_interfaces = []
    # loopback_interfaces = []

    # for interface in interface_list:
    #     if interface.startswith("Gig"):
    #         gig_interfaces.append(interface)
    # print(gig_interfaces)

    # Using the list comprehension method to create a new list
    # This method is much more efficient and concise
    gig_interfaces = [interface for interface in interface_list if interface.startswith("Gig")]
    loopback_interfaces = [interface for interface in interface_list if interface.startswith("Loop")]
    print(gig_interfaces)
    print(loopback_interfaces)

    # Using Dict. Comprehensions
    device_ips = {
        "R1": "192.168.1.254",
        "R2": "192.168.1.253",
        "S1": "10.1.1.250",
        "S2": "10.1.1.251",
    }
    # for k,v in device.items(), if key starts with R, add to router_ips dict
    router_ips = {k: v for (k, v) in device_ips.items() if k.startswith("R")}
    # for k,v in device.items(), if key starts with S, add to switch_ips dict
    switch_ips = {k: v for (k, v) in device_ips.items() if k.startswith("S")}
    print(router_ips)
    print(switch_ips)


if __name__ == "__main__":
    main()
