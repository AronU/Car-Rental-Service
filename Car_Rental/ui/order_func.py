# Gets acces to the printline funcson in the Universal_func named un_func in the code
# All over the place in the ui
from ui.Universal_func import printer, printline, date_chack
import ui.Universal_func as un_func
# Gets access to the OrderService class in the services folder. Used to get the available order lists.
from services.OrderService import OrderService
# Datetime is yous do used to make sure dates that are given are real
from datetime import date, datetime
# Gets access to the CustomerService class in the services folder. Used to get the ssn, name and list of users.
from services.CustomerService import CustomerService
# Used to format the user_list when it needs to be printed
from ui.Search_user_func import user_list_printer
# Gets access to the CarService class in the services folder. Used to get_car_price and valid_check_licence_plate
from services.CarService import CarService
# To give the youser a list of available cars it is better to format them then just printing it straight 
from ui.Car_list_func import car_list_printer
import ui.Car_list_func as Car_list_f
#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"
customer_service = CustomerService()
order_service = OrderService()
car_service = CarService()
End = False

# present is the day to day no matter what you are reading this
present = datetime.now().date()

def DontMakeOrder():
    # The DontMakeOrder function is used to make sure that when the user want to go back to the 
    # mane menu that the system does not place a order.
    ssn = "0"
    name = "0"
    start_date = "0"
    end_date = "0"
    licence_plate = "0"
    additional_insurance = "0"
    payment_way = "0"
    ID = "0"
    END = True
    return ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID, END

def get_customer_info(ssn='0', name='0', start_date='0', end_date='0', licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True): 
##############################################################################################################
    count = 1
    while count == 1:
        print("Search by Name or by SSN\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID, End = DontMakeOrder()
        elif Choice.isdigit() == True:
            customer_ssn_list = customer_service.get_customer_ssn(Choice)
            for line in customer_ssn_list:
                ssn = line[1]
                name = line[0]
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
                    get_customer_info()
                    count = 1
                else:
                    for line in customer_name_list:
                        ssn = line[1]
                        name = line[0]
                    customer_name_list.clear()
                    count += 1
    return ssn, name
##############################################################################################################
def get_start_date(ssn, name, start_date='0', end_date='0', licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True):
    count = 1
    while count == 1:
        print("Example: DD/MM/YYYY\nEnter in the date you want to pick up a car\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2:
            ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID, End = DontMakeOrder()
        elif Choice == Back_1 or Choice == Back_2:
            get_customer_info(ssn='0', name='0', start_date='0', end_date='0', licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True)
            count = 1
        elif len(Choice) == 10:
            try:
                day, month, year = Choice.replace("/", " ").split()
                Tester, start_date = un_func.date_chack(day, month, year)
                if Tester == False:
                    count = 1
            except ValueError:
                Tester = False
                print("\nERROR: Something went wrong with your input please try again\n")
                printline()
            if present > start_date:
                print("\nYou Can't rent a car in the past\n")
                un_func.printline()
                count = 1
            else:
                count += 1
        return start_date
##############################################################################################################
def get_end_date(ssn, name, start_date, end_date='0', licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True):
    count = 1
    while count == 1:
        print("Example: DD/MM/YYYY\nEnter in the date you want to return a car\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2:
            ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID, End = DontMakeOrder()
        elif Choice == Back_1 or Choice == Back_2:
            get_start_date(ssn, name, start_date='0', end_date='0', licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True)
        elif len(Choice) == 10:
            try:
                Tester = True
                day, month, year = Choice.replace("/", " ").split()
                Tester, end_date = un_func.date_chack(day, month, year, Tester)
                if start_date > end_date:
                    print("\nYou Can't return a car you don't have\n")
                    un_func.printline()
                    count = 1
                else:
                    count += 1
            except:
                Tester = False
                print("\nERROR: Something went wrong with your input please try again\n")
                un_func.printline()
    return end_date
##############################################################################################################
def get_licence_plate(ssn, name, start_date, end_date, licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True):
    count = 1
    while count == 1:
        print("Example: XX XXX\nEnter in the the licence plate or leave empty to see available cars\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2:
            ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID, End = DontMakeOrder()
        elif Choice == Back_1 or Choice == Back_2:
            get_end_date(ssn, name, start_date, end_date='0', licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True)    
            count = 1
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
                    licence_plate = Choice
                    count += 1
        elif len(Choice) == 0:
            available_cars = order_service.available_cars(start_date, end_date)
            Car_list_f.car_list_printer(available_cars)
            count = 1
        else:
            print("\nERROR: Please enter a licence plate number like this:\nXX XXX\n")
            un_func.printline()
            count = 1
    return licence_plate
##############################################################################################################
def prompt_for_additional_insurance(ssn, name, start_date, end_date, licence_plate, additional_insurance='0', payment_way='0', ID='0', End=True):
    count = 1
    while count == 1:
        print("Do you want additional car insurance (Y/N)?\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2:
            ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID, End = DontMakeOrder()
        elif Choice == Back_1 or Choice == Back_2:
            get_licence_plate(ssn, name, start_date, end_date, licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True)
            count = 1
        elif Choice == "y":
            additional_insurance = "Yes"
            count += 1
        elif Choice == "n":
            additional_insurance = "No"
            count += 1
        else:
            print("\nERROR: Something went wrong with your input please try again\n")
            un_func.printline()
            count = 1
    return additional_insurance
##############################################################################################################
def what_to_edit(ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way='0', ID='0', End=True):
    count = 1
    while count == 1:
        price = car_service.get_car_price(licence_plate)
        d = end_date - start_date
        print("How would you like to pay for the car?\nPrice: " + str(d.days*price) +"Kr.\n\n1.  Credit card\n2.  Debit card\n3.  Cash\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2:
            ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID, End = DontMakeOrder()
        elif Choice == Back_1 or Choice == Back_2:
            prompt_for_additional_insurance(ssn, name, start_date, end_date, licence_plate, additional_insurance='0', payment_way='0', ID='0', End=True)
            count = 1
        elif Choice == "1":
            payment_way = "Credit card"
            count += 1
        elif Choice == "2":
            payment_way = "Debit card"
            count += 1
        elif Choice == "3":
            payment_way = "Cash"
            count += 1
        else:
            print("\nERROR: Something went wrong with your input please try again\n")
            un_func.printline()
            count = 1
    return payment_way
##############################################################################################################
def confirm_order(ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID='0', End=True):
    count = 1
    while count == 1:
        print("Please confirm your order (Y/N):\n\nSSN: {} \nName: {} \n".format(ssn, name))
        print("Start date: {} \nEnd date: {} \nLicence_plate: {} \n".format(start_date, end_date, licence_plate))
        print("Additional insurance: {} \nPayment way: {} \n".format(additional_insurance, payment_way))
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == "n":
            ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID, End = DontMakeOrder()
        elif Choice == Back_1 or Choice == Back_2:
            what_to_edit(ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way='0', ID='0', End=True)
            count = 1
        elif Choice == "y":
            ID = order_service.get_random_id()
            count += 1
        else:
            count = 1
    return ID

while not End:
    ssn, name = get_customer_info(ssn='0', name='0', start_date='0', end_date='0', licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True)
    start_date = get_start_date(ssn, name, start_date='0', end_date='0', licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True)
    end_date = get_end_date(ssn, name, start_date, end_date='0', licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True)
    licence_plate = get_licence_plate(ssn, name, start_date, end_date, licence_plate='0', additional_insurance='0', payment_way='0', ID='0', End=True)
    additional_insurance = prompt_for_additional_insurance(ssn, name, start_date, end_date, licence_plate, additional_insurance='0', payment_way='0', ID='0', End=True)
    payment_way = what_to_edit(ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way='0', ID='0', End=True)
    order_confirm = confirm_order(ssn, name, start_date, end_date, licence_plate, additional_insurance, payment_way, ID='0', End=True)