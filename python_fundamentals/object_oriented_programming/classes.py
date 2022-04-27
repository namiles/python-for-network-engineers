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
        self._location = location

    # Commonly used to make a readable representation of an object
    def __str__(self):
        return "I am an instance of the router class"

    # Functions defined inside of a class are kno wn as methods.
    def getInfo(self):
        """Returns information about router"""
        info = (
            f"Router Model:       {self.model}\n"
            f"Software Version:   {self.swversion}\n"
            f"IP Address:         {self.ip_address}\n"
            f"Location:           {self._location}"
        )
        return info

    def set_ip_address(self, s):
        """Set the IP address of the device"""
        self.ip_address = s

    """
    Private Membership

    Python implements the idea of private members a little differently.
    Traditionally, private members can only be accessed from within a class.
    In Python, we can only make that intended but cannot be enforced.

    Private memberships are indicdated with an underscore at the beginning of the method/attrbute:
    Ex: _get_info()

    We can use this to indicate to a user that the method/attribute is not meant to be modified

    Keep in mind that Python does NOT enforce this, and they can still be modified and accessed outside the class.
    """

    # Setters - standard way of setting the value of a "private" attribute
    def set_location(self, loc):
        """Set the Location of the device"""
        self._location = loc
        
    # Getters - standard way of getting the value of a "prviate" attribute
    def get_location(self):
        return self._location

    """
    Property Decorators

    A decorator is a function that takes another function as an argument, and returns another function.
    Indicated with an @ symbol.
    """

    # As an example, we could replace the above getter and setter functions with the following:
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_loc):
        if len(new_loc) < 2:
            raise ValueError("Location must be at least 2 characters.")
        self._location = new_loc


"""
Inheritance
"""


class Switch(Router):
    """Switch class is derived from Router class"""

    # Overrides the getInfo method from the Router class
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
    print("\n------- Router Class -------")
    r1 = Router("Cisco 2911", "15.6.7", "10.1.1.135", "Rack 24")
    print(r1)  # Prints what is returned in the __Str__ method
    print(r1.getInfo())
    print()
    r2 = Router("Cisco 1911", "12.2", "10.1.1.136", "Rack 25")
    print(r2.getInfo())

    print("\n------- Switch Class -------")
    s1 = Switch("Cisco Catalyst 3750", "16.1", "10.1.1.137", "Rack 28")
    print(s1.getInfo())
    s1.set_ip_address("192.168.200.120")
    print("\nUpdated IP address using set_ip_address() method:")
    print(s1.getInfo())

    print()

    print(dir(Router))


if __name__ == "__main__":
    main()
