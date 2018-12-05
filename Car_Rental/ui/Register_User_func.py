#Constant variable 
Back_1 = "b"
Back_2 = "back"
Home_1 = "h"
Home_2 = "main menu"

def printer():
        print("B.  Back one window")
        print("H.  Main menu")
        print("--"*25)

def DontMakeUser():
    count = 6
    name = "0"
    ssn = "0"
    address = "0"
    phone = "0"
    birthday = "0"

    return count, name, ssn, address, phone, birthday

def RegisterUser():
    count = 1
    while count != 6:
        if count == 1:
            print("Full name: \n")
            printer()
            name = input("Choice: ").lower()
            count += 1
            if name == Home_1 or name == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif name == Back_1 or name == Back_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            
        elif count == 2:
            print("SSN: \n")
            printer()
            ssn = input("Choice: ").lower()
            count += 1
            if ssn == Home_1 or ssn == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif ssn == Back_1 or ssn == Back_2:
                count -= 2

        elif count == 3:
            print("Home address: \n")
            printer()
            address = input("Choice: ").lower()
            count += 1
            if address == Home_1 or address == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif address == Back_1 or address == Back_2:
                count -= 2

        elif count == 4:
            print("Phone number: \n")
            printer()
            phone = input("Choice: ").lower()
            count += 1
            if phone == Home_1 or phone == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif phone == Back_1 or phone == Back_2:
                count -= 2

        elif count == 5:
            print("Birthday: \n")
            printer()
            birthday = input("Choice: ").lower()
            count += 1
            if birthday == Home_1 or birthday == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif birthday == Back_1 or birthday == Back_2:
                count -= 2

    return name, ssn, address, phone, birthday

