# Gets access to the printline function in the Universal_func named
# un_func in the code
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func
# Gets access to the CustomerService class in the service folder
from services.CustomerService import CustomerService

# constant variables to be used to take in commands through the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "h"
Home_2 = "main menu"

def user_list_printer(user_list):
    for line in user_list:
        print("Name: {} - SSN: {} - Address: {} - Phone: {} - Date of birth: {}"
                .format(line[0], line[1], line[2], line[3], line[4]))
    un_func.printline()
    input("Press Enter to continue: ")
    un_func.printline()

def Search_User():
    customer_service = CustomerService()
    count = True
    while count == True:
        print("1. Search by name\n2. Search by SSN\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            count = False
        elif Choice == "1":
            customer_name = input("Name: ")
            customer_name_list = customer_service.get_customer_name(customer_name)
            user_list_printer(customer_name_list)
        elif Choice == "2":
            customer_ssn = input("SSN: ")
            customer_ssn_list = customer_service.get_customer_ssn(customer_ssn)
            user_list_printer(customer_ssn_list)
            
