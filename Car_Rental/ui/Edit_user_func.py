from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from services.CustomerService import CustomerService

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def Donteditcustomer():
    count = 3
    SSN = "0"
    return count, SSN

def edit_user():
    customer_service = CustomerService()
    count = 1
    while count != 3:
        if count == 1:
            print("Input the SSN of the customer you want to edit\n")
            un_func.printer()
            SSN = input("Choice: ").lower()
            un_func.printline()
            if SSN == Home_1 or SSN == Home_2 or SSN == Back_1 or SSN == Back_2:
                count, SSN = Donteditcustomer()
            elif customer_service.valid_customer_check(SSN):
                count += 1
            else:
                print("\nERROR: The SSN you entered is not in the system\n")
                un_func.printline()
        elif count == 2:
            print("Do you want to edit the Name(1), Address(2), Phone(3) or date of birth(4) of the user: " + SSN + "?\n")
            un_func.printer()
            Choice = input("Choice: ")
            un_func.printline()
            if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
                count, SSN = Donteditcustomer()
            elif Choice == "1":
                new_name = input("New name: ")
                customer_service.edit_customer(SSN, Choice, new_name)
            elif Choice == "2":
                new_address = input("New address: ")
                customer_service.edit_customer(SSN, Choice, new_address)
            elif Choice == "3":
                new_phone = input("New phone number: ")
                customer_service.edit_customer(SSN, Choice, new_phone)
            elif Choice == "4":
                new_birthday = input("New date of birth: ")
                customer_service.edit_customer(SSN, Choice, new_birthday)