from classes import Switch

def main():
    s1 = Switch("3750G", "15.2", "192.168.32.2", "Floor2")
    
    print(s1.location)
    s1.location = "new location"
    print(s1.location)

if __name__ == "__main__":
    main()