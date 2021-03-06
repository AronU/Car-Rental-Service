# Gets acces to the printline funcson in the Universal_func named un_func in the code
# All over the place in the ui
from ui.Universal_func import printer, printline, Full_name_input_chack
import ui.Universal_func as un_func

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def DontMakeUser():
    # The DontMakeUser function is used to make sure that when the user want to go back to the 
    # mane menu that the system does not create a user.
    count = 7
    name = "0"
    ssn = "0"
    address = "0"
    phone = "0"
    birthday = "0"

    return count, name, ssn, address, phone, birthday

def RegisterUser():
    # The RegisterUser function is used to Register User and 
    # to go back and forward through the function
    count = 1
    while count != 7:
        # Takes in full name and allows user to go back one window or go to the mane menu
        if count == 1:
            print("Full name: \n")
            un_func.printer()
            name = input("Name: ")
            un_func.printline()
            count += 1
            if name == Home_1 or name == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif name == Back_1 or name == Back_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            else:
                Tester, name = un_func.Full_name_input_chack(name)
                if Tester == False:
                    count = 1

        elif count == 2:
            # Takes in SSN and allows user to go back one window or go to the mane menu
            print("SSN: \n")
            un_func.printer()
            ssn = input("SSN: ").lower()
            un_func.printline()
            count += 1
            if ssn == Home_1 or ssn == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif ssn == Back_1 or ssn == Back_2:
                count -= 2
            else:
                Tester, ssn = un_func.ssn_input_chack(ssn)
                if Tester == False:
                    count = 2

        elif count == 3:
            # Takes in Home address and allows user to go back one window or go to the mane menu
            print("Home address: \n")
            un_func.printer()
            address = input("Home address: ")
            un_func.printline()
            count += 1
            if address == Home_1 or address == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif address == Back_1 or address == Back_2:
                count -= 2
            else:
                Tester, address = un_func.address_input_chack(address)
                if Tester == False:
                    count = 3

        elif count == 4:
            # Takes in Phone number and allows user to go back one window or go to the mane menu
            print("Phone number: \n")
            un_func.printer()
            phone = input("Phone number: ").lower()
            un_func.printline()
            count += 1
            if phone == Home_1 or phone == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif phone == Back_1 or phone == Back_2:
                count -= 2
            else:
                Tester, phone = un_func.phone_input_chack(phone)
                if Tester == False:
                    count = 4

        elif count == 5:
            # Takes in Birthday and allows user to go back one window or go to the mane menu
            print("DD/MM/YYYY\nBirthday: \n")
            un_func.printer()
            birthday = input("Birthday: ").lower()
            un_func.printline()
            count += 1
            if birthday == Home_1 or birthday == Home_2:
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif birthday == Back_1 or birthday == Back_2:
                count -= 2
            else:
                Tester, birthday = un_func.birthday_input_chack(birthday)
                if Tester == False:
                    count = 5

        elif count == 6:
            # makes the user confirm what user he is making 
            # and allows user to go back one window or go to the mane menu
            print("Is this the user you whant to make (Y/N) ?\n")
            print("Full name: {:>2}\nSSN: {:>2}\nHome address: {:>2}".format(name, ssn, address))
            print("Phone number: {:>2}\nBirthday: {}\n".format(phone, birthday))
            un_func.printer()
            confirm = input("Choice: ").lower()
            un_func.printline()
            if confirm == "y":
                count += 1
            if confirm == Home_1 or confirm == Home_2 or confirm =="n":
                count, name, ssn, address, phone, birthday = DontMakeUser()
            elif confirm == Back_1 or confirm == Back_2:
                count -= 1

    return name, ssn, address, phone, birthday

