from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from services.CarService import CarService

from ui.Car_list_func import car_list_printer
import ui.Car_list_func as car_func

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"


def car_history_printer(history_list):
    print("The order history for {}: \n".format(history_list[0][1]))

    for line in history_list:
        print("ID: {} - Start date: {} - End date: {}\n".format(line[0], line[4], line[5]))
    un_func.printline()
    input("Press Enter to coninue: ")
    un_func.printline()
    return False

def dontShowCarHistory():
    count = 3
    licence_plate = '0'
    Counter = False
    return count, licence_plate, Counter

def car_history():
    car_service = CarService()
    count = 1
    while count != 3:
        if count == 1:
            print("Input the licence plate of the car you want see the history of\nor leave it empty to see a list of all cars.\n")
            un_func.printer()
            licence_plate = input("Choice: ").lower()
            un_func.printline()
            if licence_plate == Home_1 or licence_plate == Home_2:
                count, licence_plate, Counter = dontShowCarHistory()
            elif licence_plate == Back_1 or licence_plate == Back_2:
                count = 3
                Counter = True
            elif licence_plate == "":
                car_list = car_service.get_all_cars()
                car_func.car_list_printer(car_list)
                car_list.clear()
            else:
                if car_service.valid_check_licence_plate(licence_plate) == False:
                    print("\nERROR: This licence plate does not exist in the system.\n")
                    un_func.printline()
                    input("Press Enter to coninue: ")
                    un_func.printline()
                    count = 1
                else:
                    count += 1
        elif count == 2:
            history_list = car_service.get_car_history(licence_plate)
            if history_list == []:
                print("\nThe history for {} is empty.\n".format(licence_plate))
                un_func.printline()
            else:
                car_history_printer(history_list)
                history_list.clear()
            count = 1
    return Counter