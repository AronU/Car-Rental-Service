# Gets acces to the printline funcson in the Universal_func named un_func in the code
# All over the place in the ui
from ui.Universal_func import printer, printline, date_chack
import ui.Universal_func as un_func
#Gets access to the OrderService class in the services folder. Used to get the available order lists.
from services.OrderService import OrderService

from datetime import date, datetime
from services.CustomerService import CustomerService

from ui.Search_user_func import user_list_printer

from services.CarService import CarService


#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"
END = 11

present = datetime.now().date()

def DontMakeOrder():
    SSN = "0"
    Name = "0"
    start_date = "0"
    end_date = "0"
    licence_plate = "0"
    additional_insurance = "0"
    paymant_way = "0"
    ID = "0"
    count = END
    return SSN, Name, start_date, end_date, licence_plate, additional_insurance, paymant_way, ID, count

def order_menu():
    customer_service = CustomerService()
    order_service = OrderService()
    car_service = CarService()
    count = 1
    while count != END:
        if count == 1:
            print("Search by Name or by SSN\n")
            un_func.printer()
            Choice = input("Choice: ").lower()
            un_func.printline()
            if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
                SSN, Name, start_date, end_date, licence_plate, additional_insurance, paymant_way, ID, count = DontMakeOrder()
            elif Choice.isdigit() == True:
                customer_ssn_list = customer_service.get_customer_ssn(Choice)
                for line in customer_ssn_list:
                    SSN = line[1]
                    Name = line[0]
                user_list_printer(customer_ssn_list)
                customer_ssn_list.clear()
                count += 1 
            elif Choice.isdigit() == False:
                Tester = False
                for letter in Choice:
                    T_or_F = letter.isdigit()
                    if T_or_F == True:
                        Tester = True
                if Tester == True:
                    print("\nERROR: Number can't be used in Name\n")
                    printline()
                else:
                    customer_name_list = customer_service.get_customer_name(Choice)
                    user_list_printer(customer_name_list)
                    if len(customer_name_list) > 1:
                        customer_name_list.clear()
                        count = 1
                    else:
                        for line in customer_name_list:
                            SSN = line[1]
                            Name = line[0]
                        customer_name_list.clear() 
                        count += 1 
        elif count == 2:
            print("Example: DD/MM/YYYY\nEnter in the date you want to pick up a car\n")
            un_func.printer()
            Choice = input("Choice: ").lower()
            un_func.printline()
            if Choice == Home_1 or Choice == Home_2:
                SSN, Name, start_date, end_date, licence_plate, additional_insurance, paymant_way, ID, count = DontMakeOrder()
            elif Choice == Back_1 or Choice == Back_2:
                count -= 1
            elif len(Choice) == 10:
                try:
                    day, month, year = Choice.replace("/", " ").split()
                    Tester, start_date = un_func.date_chack(day, month, year)
                    if Tester == False:
                        count = 2
                except ValueError:
                    Tester = False
                    print("\nERROR: Something went wrong with your input please try again\n")
                    printline()
                if present < start_date:
                    count += 1
                else:
                    print("\nYou Can't rent a car in the past\n")
                    un_func.printline()
        elif count == 3:
            print("Example: DD/MM/YYYY\nEnter in the date you want to return a car\n")
            un_func.printer()
            Choice = input("Choice: ").lower()
            un_func.printline()
            if Choice == Home_1 or Choice == Home_2:
                SSN, Name, start_date, end_date, licence_plate, additional_insurance, paymant_way, ID, count = DontMakeOrder()
            elif Choice == Back_1 or Choice == Back_2:
                count -= 1
            elif len(Choice) == 10:
                try:
                    day, month, year = Choice.replace("/", " ").split()
                    Tester, end_date = un_func.date_chack(day, month, year, Tester)
                except ValueError:
                    Tester = False
                    print("\nERROR: Something went wrong with your input please try again\n")
                    un_func.printline()
                if start_date < end_date:
                    count += 1
                else:
                    print("\nYou Can't return a car you don't have\n")
                    un_func.printline()
        elif count == 4:
            
            print("Example: XX XXX\nEnter in the the licence plate of the car you want to rent or leave empty for full list of Available cars\n")
            un_func.printer()
            Choice = input("Choice: ").upper()
            un_func.printline()
            if Choice == Home_1 or Choice == Home_2:
                SSN, Name, start_date, end_date, licence_plate, additional_insurance, paymant_way, ID, count = DontMakeOrder()
            elif Choice == Back_1 or Choice == Back_2:
                count -= 1
            elif len(Choice) == 6:
                Tester = False
                try:
                    (' ' in Choice) == True
                    Tester = True
                except ValueError:
                    print("\nERROR: Something went wrong with your input, please try again\n")
                    un_func.printline()
                if Tester == True:
                    licence_plate_check = car_service.valid_check_licence_plate(Choice)
                    if licence_plate_check == True:  
                        licence_plate = Choice
                        count += 1
                    else:
                        print("\nThe car you want is not available. Please enter another licence plate.\n")
                        count = 4
                        un_func.printline()
            
        elif count == 5:
            count += 1

        elif count == 6:
            count += 1

        elif count == 7:
            count += 1
            
        elif count == 8:
            count = END
        ###############Get radom ID###############
            # if Yes_or_no == "Y":
            #     ID = order_service.get_random_id()
####################################################################################################
    print(SSN)
    print(Name)
    print(start_date)
    print(end_date)
    ####################
    print(licence_plate)
    #print(additional_insurance)
    ##############################
    #print(paymant_way)
