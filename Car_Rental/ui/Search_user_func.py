from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from services.CustomerService import CustomerService


#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def user_list_printer(user_list):
    for line in user_list:
        print("Name: {} - SSN: {} - Address: {} - Phone: {} - Date of birth: {}"
                .format(line[0], line[1], line[2], line[3], line[4]))
    un_func.printline()
    input("Press Enter to continue: ")
    un_func.printline()

def search_user():
    customer_service = CustomerService()
    count = True
    while count == True:
        print("Please provide a name, SSN or leave empty for a list of all users\n")
        un_func.printer()
        Choice = input("Name/SSN: ").lower()
        un_func.printline
        if Choice == Home_1 or Choice == Home_2:
            return False
        elif Choice == Back_1 or Choice == Back_2:
            return True
        elif Choice.isdigit() == True:
            customer_ssn_list = customer_service.get_customer_ssn(Choice)
            user_list_printer(customer_ssn_list)
            customer_ssn_list.clear()
        elif Choice.isdigit() == False:
            Tester = False
            for letter in Choice:
                T_or_F = letter.isdigit()
                if T_or_F == True:
                    Tester = True
            if Tester == True:
                print("\nERROR: Number can't be used in name\n")
                printline()
            else:
                customer_name_list = customer_service.get_customer_name(Choice)
                user_list_printer(customer_name_list)
                customer_name_list.clear()
       
       