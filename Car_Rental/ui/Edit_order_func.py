from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from services.OrderService import OrderService

from services.CustomerService import CustomerService

from services.CarService import CarService

Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def Donteditorder():
    count = END
    ssn = "0"
    order_ID = "0"
    license_plate = "0"
    return count, SSN, order_ID, license_plate

def Exit():
    pass

def edit_order():
    order_service = OrderService()
    customer_service = CustomerService()
    car_services = CarService()
    count = 1
    while count != END:
        if count == 1:
            print("Input the SSN, licence plate or order ID to find the order you want to edit\n")
            un_func.printline()
            Choice = input("Choice: ").upper()
            un_func.printline()
            if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
                count, ssn, order_ID, licence_plate = Donteditorder()
            elif Choice.isdigit() == True:
                if customer_service.valid_customer_check(Choice):
                    order_ssn_list = order_service.get_order_ssn(Choice)
                    for line in order_ssn_list:
                        name = line[3]
                        ssn = line[2]
                        licence_plate = line[1]
                        order_ID = line[0]
                elif 
                else:
                    print("\nERROR: The SSN you entered is not in the system. Please try again.\n")
                    un_func.printline()
                count += 1
            elif Choice.isdigit() == False:
                try:
                    car_services.valid_check_licence_plate(Choice)
                except:
                    print("\nERROR: The licence plate you entered is not in the system. Please try again.\n")
                    un_func.printline()
                order_licence_plate_list = order_service.get_order_licence_plate(Choice)
                for line in licence_plate_list:
                    name = line[3]
                    ssn = line[2]
                    licence_plate = line[1]
                    order_ID = line[0]
                count += 1
        elif count == 2:
            print("\nDo ")

    return name, ssn, order_ID, licence_plate