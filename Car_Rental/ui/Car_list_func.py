from ui.Universal_func import printer, printline
import ui.Universal_func as un_func
from services.CarService import CarService
#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "h"
Home_2 = "main menu"

def car_list_printer(car_list):
    for line in car_list:
        print("Licence plate: {} - {} {} - Year: {} ".format(line[0], line[1], line[2], line[3]))
    un_func.printline()
    input("Press Enter to continue: ")
    un_func.printline()

    
def Carlist():
    car_service = CarService()
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
        elif Choice == "2":
            unavailable_car_list = car_service.get_unavailable_cars()
            car_list_printer(unavailable_car_list)
