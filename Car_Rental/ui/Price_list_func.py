# Gives the function access to the printline function in Universal_func named un_func
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from services.PriceService import PriceService

# Constant variables used as commands in the input.
Back_1 = "b"
Back_2 = "back"
Home_1 = "h"
Home_2 = "main menu"

def price_list_printer(price_list):
    for line in price_list:
        print("Licence plate: {} - {} {} - Year: {} Price: {} ".format(line[0], line[1], line[2], line[3], line[5]))
    un_func.printline()
    input("Press Enter to continue: ")
    un_func.printline()

    
def Pricelist():
    price_service = PriceService()
    count = True
    while count == True:
        print("1.  Low prices\n2.  Medium prices\n3.  High prices\n4.  All prices\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            count = False
        elif Choice == "1":
            low_price_list = price_service.get_LowPrice()
            price_list_printer(low_price_list)
        elif Choice == "2":
            medium_price_list = price_service.get_MediumPrice()
            price_list_printer(medium_price_list)
        elif Choice == "3":
            high_price_list = price_service.get_HighPrice()
            price_list_printer(high_price_list)
        elif Choice == "4":
            all_prices_list = price_service.get_all_prices()
            price_list_printer(all_prices_list)