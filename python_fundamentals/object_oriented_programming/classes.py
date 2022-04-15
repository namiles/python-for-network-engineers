"""
Everything in Python is an object - classes can be used to define an object.
There are built-in classes in Python. A string, for example, is one of them.

Classes are defined using the "class" keyword, and class names follow the CamelCase convention
"""

class Router:
    """Class used to describe routers"""

    # Class Attributes are associated with every instances of a class and are not unqiue for each class instance
    device_type = "network_device"

    # __init__ is a magic method, AKA as dunder method
    # Magic methods can be created
    def __init__(self, model, swversion, ip_address, location):
        # Instance Attributes (below) are attributes that can be different for every instance of a class
        self.model = model
        self.swversion = swversion
        self.ip_address = ip_address
        self.location = location

    # Functions defined inside of a class are known as methods.
    def getInfo(self):
        """Returns information about router"""
        info = (
            f"Router Model:       {self.model}\n"
            f"Software Version:   {self.swversion}\n"
            f"IP Address:         {self.ip_address}\n"
            f"Location:           {self.location}"
        )
        return info

    def set_ip_address(self, s):
        """Set the IP address of the device"""
        self.ip_address = s


class Switch(Router):
    """ Switch class is derived from Router class """

    def getInfo(self):
        """Returns information about Switch"""
        info = (
            f"Switch Model:       {self.model}\n"
            f"Software Version:   {self.swversion}\n"
            f"IP Address:         {self.ip_address}\n"
            f"Location:           {self.location}"
        )
        return info


def main():
    print()

    r1 = Router("Cisco 2911", "15.6.7", "10.1.1.135", "Rack 24")
    print(r1.getInfo())
    print()
    r2 = Router("Cisco 1911", "12.2", "10.1.1.136", "Rack 25")
    print(r2.getInfo())

    print()
    s1 = Switch("Cisco Catalyst 3750", "16.1", "10.1.1.137", "Rack 28")
    print(s1.getInfo())
    s1.set_ip_address("192.168.200.120")
    print("Updated IP address:")
    print(s1.getInfo())

    print()

    print(dir(Router))


if __name__ == "__main__":
    main()
