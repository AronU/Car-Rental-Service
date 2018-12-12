from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from services.CarService import CarService

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def car_list_printer(car_list):
    for line in car_list:
        print("Licence plate: {} - {} {} - Year: {}".format(line[0], line[1], line[2], line[3]))


def calculate_cost_menu():
    car_service = CarService()
    count = 1
    all_car_list = car_service.get_all_cars()
    car_list_printer(all_car_list)
    print("\nSelect a car from the list above by typing in the licence plate\n")
    un_func.printer()
    Choice = input("Choice: ").lower()
    un_func.printline()
    while count != 3:
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            count = False
        elif Choice == ""