from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from services.OrderService import OrderService

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def order_list_printer(order_list):
    for line in order_list:
        print("ID: {} - Licence plate: {} - SSN: {} - Start date: {} - End date: {} - Payment info: {} - Additional insurence: {} - Order status: {} "
             .format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]))
        un_func.printline()
        input("Press Enter to coninue: ")
        un_func.printline



def search_order_ssn():
    order_service = OrderService()
    count = True
    while count == True:
        print("Input SSN\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline
        if Choice == Home_1 or Choice == Home_2:
            return False
        elif Choice == Back_1 or Choice == Back_2:
            return True
        elif Choice.isdigit() == True:
            order_ssn_list = order_service.get_order_ssn(Choice)
            order_list_printer(order_ssn_list)
            order_ssn_list.clear()
        elif Choice.isdigit() == False:
            print("Please enter a valid SSN")
        else:
            print("Order does not exist")