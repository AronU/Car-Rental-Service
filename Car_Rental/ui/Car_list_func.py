# Gets acces to the printline funcson in the Universal_func named un_func in the code
# All over the place in the ui
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func
#Gets access to the CarService class in the services folder. Used to get the available car lists.
from services.CarService import CarService

# from services.OrderService import OrderService

from datetime import date, datetime
#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def car_list_printer(car_list):
    # This function takes a nested list of car available or unavailable and prints them out 
    # in a presentable way
    for line in car_list:
        print("Licence plate: {} - {} {} - Year: {} ".format(line[0], line[1], line[2], line[3]))
    un_func.printline()
    input("Press Enter to continue: ")
    un_func.printline()

    
def Carlist():
    # This function gives user a choice and calls the the appropriate list. 
    car_service = CarService()
    # order_service = OrderService()
    count = True
    while count == True:
        print("1.  Available cars\n2.  Unavailable cars\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            count = False
        elif Choice == "1":
            available_car_list = car_service.get_available_cars()
            car_list_printer(available_car_list)
            # present = datetime.now().date()
            # newYear = present.day + 1
            # print(newYear)
            # available_cars = order_service.available_cars(present, newYear)
            # car_list_printer(available_cars)
        elif Choice == "2":
            unavailable_car_list = car_service.get_unavailable_cars()
            car_list_printer(unavailable_car_list)
