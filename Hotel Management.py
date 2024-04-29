def Date(date):
    pass

def RoomHub():
    RoomMenu = {
        "View all rooms":Room_Info,
        "Book a Room":Booking
    }

    roomKeys = RoomMenu.keys()
    while True:
        for i, description in enumerate(roomKeys):
            print(f"{i+1}: {description}")

        choice = -1
        while choice < 1 or choice > (i+1):
            print("\nValue must be a number and selectable.")
            try:
                choice = int(input("Select an option: "))
            except ValueError():
                print("Enter a valid option")

        operationName = list(roomKeys)[choice-1]
        print(f"\n-----{operationName}-----")
        RoomMenu[operationName]()

def Booking():
    print("Book")

def Room_Info():
    print("INFO")

def AdminLogin():
    print("Admin Login")

def RoomService():
    print("Room Service")

def Home():
    menu = {
        "Select a room":RoomHub,
        "Contact Roomservice":RoomService,
        "Open admin options":AdminLogin
    }

    menuKeys = menu.keys()
    while True:
        print("\n-----Main Menu-----")
        for i, description in enumerate(menuKeys):
            print(f"{i+1}: {description}")

        choice = -1
        while choice < 1 or choice > (i+1):
            print("\nValue must be a number and selectable.")
            try:
                choice = int(input("Select an option: "))
            except ValueError():
                print("Enter a valid option")

        operationName = list(menuKeys)[choice-1]
        print(f"\n-----{operationName}-----")
        menu[operationName]()

Home()