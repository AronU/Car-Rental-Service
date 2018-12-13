
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from services.CustomerService import CustomerService

from ui.Search_user_func import user_list_printer
import ui.Search_user_func as Search_user_f

from ui.Edit_user_func import Donteditcustomer, exit_f
import ui.Edit_user_func as edit_u

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"


def User_history_printer(history_list):
    print("The order history for {}: \n".format(history_list[0][3]))

    for line in history_list:
        print("ID: {} - Licence plate: {} - Start date: {} - End date: {} - Payment way: {} - Additional insurence: {}\n".format(line[0], line[1], line[4], line[5], line[6], line[7]))
    un_func.printline()
    input("Press Enter to coninue: ")
    un_func.printline()
    return False

def User_history():
    customer_service = CustomerService()
    count = 1
    while count != 3:
        if count == 1:
            print("Input the SSN of the customer you see the history of\nor leave it empty to see a list of users\n")
            un_func.printer()
            SSN = input("Choice: ").lower()
            un_func.printline()
            if SSN == Home_1 or SSN == Home_2:
                count, SSN, Counter = edit_u.Donteditcustomer()
            elif SSN == Back_1 or SSN == Back_2:
                count = 3
                Counter = edit_u.exit_f()
            elif SSN == "":
                customer_name_list = customer_service.get_customer_name(SSN)
                Search_user_f.user_list_printer(customer_name_list)
                customer_name_list.clear()
            else:
                if customer_service.valid_customer_check(SSN) == False:
                    print("ERROR: This SSN does not belong to a user")
                    count = 1
                else:
                    count += 1
        elif count == 2:
            history_list = customer_service.user_history(SSN)
            User_history_printer(history_list)
            history_list.clear()
            count = 1
    return Counter