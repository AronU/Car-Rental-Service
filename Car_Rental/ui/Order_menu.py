# Gets access to the printline function in the Universal_func named
# un_func in the code
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

# Gets access to the CustomerService class in the service folder
from services.CustomerService import CustomerService

# Gets access to the CarService class in the service folder
from services.CarService import CarService

from services.OrderService import OrderService

# constant variables to be used to take in commands through the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def order_list_printer(order_list, lp_or_ssn=1):
    if lp_or_ssn == 1:
        print("The order where this user: {} was involved: \n".format(order_list[0][3]))

        for line in order_list:
            print("ID: {} - Licence plate: {} - Start date: {} - End date: {} - Payment way: {} - Additional insurence: {}\n".format(line[0], line[1], line[4], line[5], line[6], line[7]))
        un_func.printline()
        input("Press Enter to coninue: ")
        un_func.printline()
    elif lp_or_ssn == 2:
        print("The order where {} whas rented out: \n".format(order_list[0][1]))
        for line in order_list:
            print("ID: {} - SSN: {} - Name: {} - Start date: {} - End date: {} - Payment way: {}- Additional insurence: {}\n".format(line[0], line[2], line[3], line[4], line[5], line[6], line[7]))
        un_func.printline()
        input("Press Enter to coninue: ")
        un_func.printline()
    return False

def Search_order_menu():
    order_service = OrderService()
    customer_service = CustomerService()
    count = True
    while count == True:
        print("You can search for an order from user's SSN or by rental car licence plate.\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            count = False
        elif Choice == "":
            print("\nERROR: You have to search for something!\n")
            un_func.printline()
        elif Choice.isdigit() == True:
            if customer_service.valid_customer_check(Choice) == True:
                order_ssn_list = order_service.get_order_ssn(Choice)
                order_list_printer(order_ssn_list)
                order_ssn_list.clear()
        elif Choice.isdigit() == False:
            Choice = Choice.upper()
            order_licence_plate_list = order_service.get_order_licence_plate(Choice)
            order_list_printer(order_licence_plate_list, 2)
            order_licence_plate_list.clear()
        elif Choice.isdigit() == False:
            print("Please enter a valid licence plate.\n")
        else:
            print("Order does not exist!\n")
