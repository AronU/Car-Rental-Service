from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from datetime import date, datetime

from services.CarService import CarService

from ui.calc_cost_with_extra import car_list_printer
import ui.calc_cost_with_extra as calc_cost

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def get_car():
    car_service = CarService()
    all_car_list = car_service.get_all_cars()
    
    count = True
    while count == True:
        calc_cost.car_list_printer(all_car_list)
        print("Input Licence plate from one of the cars above like this: XX XXX\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2:
            return False
        elif Choice == Back_1 or Choice == Back_2:
            return True
        elif len(Choice) == 6:
            Choice = Choice.upper()
            Tester = False
            try:
                if (' ' in Choice) == True:
                    Tester = True
            except:
                Tester = False
                print("\nERROR: Something went wrong with your input, please try again\n")
                un_func.printline()
            if Tester == True:
                licence_plate_check = car_service.valid_check_licence_plate(Choice)
                if licence_plate_check == True:  
                    Choice = Choice.upper()
                    car_licence_plate_list = car_service.get_licence_plate(Choice)
                    cost = calculate_cost_without_extra(car_licence_plate_list)
                    car_licence_plate_list.clear()
                    if cost == False:
                        return False
                    elif cost == True:
                        pass
                    else:
                        return cost
                else:
                    print("\nERROR: Please enter a licence plate number like this:\nXX XXX\n")
                    un_func.printline()
        else:
            print("\nERROR: Please enter a licence plate number like this:\nXX XXX\n")
            un_func.printline()

def calculate_cost_without_extra(car_licence_plate):
    count = 1
    present = datetime.now().date()
    price = car_licence_plate[0][4]
    while count != 3:
        if count == 1:
            start_date = un_func.Start_date()
            if start_date == False:
                count = 3
                return False
            elif start_date == True:
                count = 1
            elif type(start_date) == date:
                if present < start_date:
                    count += 1
                else:
                    print("\nERROR: You can't rent a car in the past\n")
                    un_func.printline()
            # else:
            #     print("\nERROR: Something went wrong with your input please try again\n")
            #     un_func.printline()
        if count == 2:
            end_date = un_func.End_date(start_date)
            if end_date == False:
                count += 1
                return False
            elif end_date == True:
                count -= 1
            else:
                d = end_date - start_date
                print("\nThe price for renting this car for " + str(d.days) + " days is: " + str(d.days*int(price)) + " Kr.\n")
                count += 1
                un_func.printline()
                input("Press Enter to continue")

        # extra insurence er 2500 auka per dag