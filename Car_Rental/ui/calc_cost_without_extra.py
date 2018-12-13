from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from datetime import date, datetime

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
    
    un_func.printline()
    count = True
    while count == True:
        car_list_printer(all_car_list)
        print("Input Licence plate from one of the cars above\n")
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
            cost = calculate_cost_without_extra(car_licence_plate_list)
            car_licence_plate_list.clear()
            if cost == False:
                return False
            elif cost == True:
                #return True
                pass
            else:
                return cost
            
        elif Choice.isdigit() == False:
            print("Please enter a valid licence plate\n")
        else:
            print("Order does not exist\n")

def calculate_cost_without_extra(car_licence_plate):
    count = 1
    price = car_licence_plate[0][4]
    while count != 3:
        if count == 1:
            start_date = un_func.Start_date()
            if start_date == False:
                count = 3
                return False
            elif start_date == True:
                count = 3
                return True
            else:
                count += 1
        if count == 2:
            end_date = un_func.End_date(start_date)
            if end_date == False:
                count += 1
                return False
            elif end_date == True:
                count -= 1
                #return True
            else:
                d = end_date - start_date
                print("\nThe price for renting this car for " + str(d.days) + " days is: " + str(d.days*int(price)) + " Kr.\n")
                count += 1
                un_func.printline()
                input("Press Enter to continue")


        # extra insurence er 2500 auka per dag