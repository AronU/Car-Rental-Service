# Gets acces to the printline funcson in the Universal_func named un_func in the code
# All over the place in the ui
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func
#Gets access to the OrderService class in the services folder. Used to get the available order lists.
from services.OrderService import OrderService

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "h"
Home_2 = "main menu"

def order_menu():
    order_service = OrderService()
    count = True
    while count == True:
        print("1.  Make order\n2.  ")