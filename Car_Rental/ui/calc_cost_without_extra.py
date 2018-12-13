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
            calculate_cost_without_extra(car_licence_plate_list)
            input("Press Enter to continue")
            car_licence_plate_list.clear()
        elif Choice.isdigit() == False:
            print("Please enter a valid licence plate\n")
        else:
            print("Order does not exist\n")

def calculate_cost_without_extra(car_licence_plate):
        price = car_licence_plate[0][4]
        start_date = un_func.Start_date()
        end_date = un_func.End_date(start_date)
        d = end_date - start_date
        print("The price for renting this car for " + str(d.days) + " days is: " + str(d.days*int(price)) + " Kr.")



# def Start_date():
#     present = datetime.now().date()
#     print("Example: DD/MM/YYYY\nEnter in the date you want to pick up a car\n")
#     un_func.printer()
#     Choice = input("Choice: ").lower()
#     un_func.printline()
#     if Choice == Home_1 or Choice == Home_2:
#         return False
#     elif Choice == Back_1 or Choice == Back_2:
#         return True
#     elif len(Choice) == 10:
#         try:
#             day, month, year = Choice.replace("/", " ").split()
#             Tester, start_date = un_func.date_chack(day, month, year)
#             if Tester == True:
#                 return start_date
#             else:
#                 message = "ERROR"
#                 return message
#         except ValueError:
#             Tester = False
#             print("\nERROR: Something went wrong with your input please try again\n")
#             un_func.printline()
#             if present < start_date:
#                 return True
#             else:
#                 print("\nYou can't rent a car in the past\n")
#                 un_func.printline()



# def End_date(start_date):
#     print("Example: DD/MM/YYYY\nEnter in the date you want to return a car\n")
#     un_func.printer()
#     Choice = input("Choice: ").lower()
#     un_func.printline()
#     if Choice == Home_1 or Choice == Home_2:
#         return False
#     elif Choice == Back_1 or Choice == Back_2:
#         return True
#     elif len(Choice) == 10:
#         try:
#             Tester = True
#             day, month, year = Choice.replace("/", " ").split()
#             Tester, end_date = un_func.date_chack(day, month, year, Tester)
#             if start_date > end_date:
#                 print("\nYou can't return a car you don't have\n")
#                 un_func.printline()
#                 return True
#             else:
#                 return end_date
#         except:
#             Tester = False
#             print("\nERROR: Something went wrong with your input please try again\n")
#             un_func.printline()




        # extra insurence er 2500 auka per dag