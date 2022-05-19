from classes import Switch, Router

def main():
    s1 = Switch("3750G", "15.2", "192.168.32.2", "Floor2")
    
    print(s1.location)
    s1.location = "new location"
    print(s1.location)

    print("\n--- Generated Router Object using Static Method ---")
    my_router = Router.random_router()
    print(my_router.getInfo())

if __name__ == "__main__":
    main()