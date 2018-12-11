# Gets access to the printline function in the Universal_func named
# un_func in the code
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

# Gets access to the CustomerService class in the service folder
from services.CustomerService import CustomerService

# Gets access to the CarService class in the service folder
from services.CarService import CarService

from ui.Search_order_ssn import search_order_ssn
import ui.Search_order_ssn as search_ssn


# constant variables to be used to take in commands through the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def Search_order_menu():
    count = True
    while count == True:
        print("You can search for an order from user's SSN or by rental car licence plate.\n")
        print("1.  Search by SSN\n2.  Search by licence plate\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            count = False
        elif Choice == "1":
            count = search_ssn.search_order_ssn()
        elif Choice == "2":
            pass