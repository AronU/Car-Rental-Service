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
        print("Licence plate: {} - Brand: {} - Model: {} - Year: {} - Price: {}".format(line[0], line[1], line[2], line[3], line[4]))
    printline()
    return False

def get_car():
    car_service = CarService()
    all_car_list = car_service.get_all_cars()
    car_list_printer(all_car_list)
    un_func.printline()
    count = True
    while count == True:
        print("Input Licence plate from the cars above\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2:
            return False
        elif Choice == Back_1 or Choice == Back_2:
            return True
        elif Choice.isdigit() == False:
            Choice = Choice.upper()
            car_licence_plate_list = car_service.get_licence_plate(Choice)
            calculate_cost_without_extra(car_licence_plate_list)
            car_licence_plate_list.clear()
        elif Choice.isdigit() == False:
            print("Please enter a valid licence plate\n")
        else:
            print("Order does not exist\n")

def calculate_cost_without_extra(car_licence_plate):
        print("price: {}".format(car_licence_plate[4]))