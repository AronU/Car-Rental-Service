from ui.Universal_func import printer, printline, Full_name_input_chack
import ui.Universal_func as un_func

from services.CustomerService import CustomerService

from ui.Search_user_func import user_list_printer
import ui.Search_user_func as Search_user_f
#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def Donteditcustomer():
    count = 3
    SSN = "0"
    Counter = False
    return count, SSN, Counter

def exit_f():
    Counter = True
    return Counter

def edit_user():
    customer_service = CustomerService()
    count = 1
    while count != 3:
        if count == 1:
            print("Please provide the SSN of the customer you want to edit\nor leave it empty to see a list of users\n")
            un_func.printer()
            SSN = input("SSN: ").lower()
            un_func.printline()
            if SSN == Home_1 or SSN == Home_2:
                count, SSN, Counter = Donteditcustomer()
            elif SSN == Back_1 or SSN == Back_2:
                count = 3
                Counter = exit_f()
            elif SSN == "":
                customer_name_list = customer_service.get_customer_name(SSN)
                Search_user_f.user_list_printer(customer_name_list)
                customer_name_list.clear()
            else:
                quest, SSN = un_func.ssn_input_chack(SSN, 1)
                if quest == True:
                    count += 1

        elif count == 2:
            print("Do you want to edit the Name(1), Address(2), Phone(3) or date of birth(4) of the user: " + SSN + "?\n")
            un_func.printer()
            Choice = input("Choice: ").lower()
            un_func.printline()
            if Choice == Home_1 or Choice == Home_2:
                count, SSN, Counter = Donteditcustomer()
            elif Choice == Back_1 or Choice == Back_2:
                count -= 1
            elif Choice == "1" or Choice == "name":
                back = False
                while not back:
                    print("Enter in the new name of the user\n")
                    un_func.printer()
                    new_name = input("New name: ")
                    un_func.printline()
                    if new_name == Home_1 or new_name == Home_2:
                        count, SSN, Counter = Donteditcustomer()
                        back = True
                    elif new_name == Back_1 or new_name == Back_2:
                        back = True
                        count -= 1
                    else:
                        Tester, new_name = un_func.Full_name_input_chack(new_name)
                        if Tester == True:
                            customer_service.edit_customer(SSN, Choice, new_name)
                            back = True
                            count -= 1
            elif Choice == "2" or Choice == "address":
                back = False
                while not back:
                    print("Enter in the new address of the user\n")
                    un_func.printer()
                    new_address = input("New address: ")
                    un_func.printline()
                    if new_address == Home_1 or new_address == Home_2:
                        count, SSN, Counter = Donteditcustomer()
                        back = True
                    elif new_address == Back_1 or new_address == Back_2:
                        back = True
                        count = 1
                    else:
                        Tester, new_address = un_func.address_input_chack(new_address)
                        if Tester == True:
                            customer_service.edit_customer(SSN, Choice, new_address)
                            back = True
                            count = 1
            elif Choice == "3" or Choice == "phone":
                back = False
                while not back:
                    print("Enter in the new phone of the user\n")
                    un_func.printer()
                    new_phone = input("New phone: ").lower()
                    un_func.printline()
                    if new_phone == Home_1 or new_phone == Home_2:
                        count, SSN, Counter = Donteditcustomer()
                        back = True
                    elif new_phone == Back_1 or new_phone == Back_2:
                        back = True
                        count = 1
                    else:
                        Tester, new_phone = un_func.phone_input_chack(new_phone)
                        if Tester == True:
                            customer_service.edit_customer(SSN, Choice, new_phone)
                            back = True
                            count = 1
            elif Choice == "4" or Choice == "date of birth":
                back = False
                while not back:
                    print("Enter in the new date of birth of the user\n")
                    un_func.printer()
                    new_date_of_birth = input("New date of birth: ").lower()
                    un_func.printline()
                    if new_date_of_birth == Home_1 or new_date_of_birth == Home_2:
                        count, SSN, Counter = Donteditcustomer()
                        back = True
                    elif new_date_of_birth == Back_1 or new_date_of_birth == Back_2:
                        back = True
                        count = 1
                    else:
                        Tester, new_date_of_birth = un_func.birthday_input_chack(new_date_of_birth)
                        if Tester == True:
                            customer_service.edit_customer(SSN, Choice, new_date_of_birth)
                            back = True
                            count = 1
    return Counter