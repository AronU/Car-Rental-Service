# Gets acces to the printline funcson in the Universal_func named un_func in the code
# All over the place in the ui
from ui.Universal_func import printer, printline, date_chack
import ui.Universal_func as un_func
#Gets access to the OrderService class in the services folder. Used to get the available order lists.
from services.OrderService import OrderService
#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def order_menu():
    def User():
        count = True
        while count == True:
            print("Search by Name or by SSN\n")
            un_func.printer()
            Choice = input("Choice: ").lower()
            un_func.printline()
            if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
                count = False
            elif Choice.isdigit() == True:
                ##########################Breita hér#################################
                Name = Choice
                SSN = Choice
                count = False
                ##########################Breita hér#################################
                # customer_ssn_list = customer_service.get_customer_ssn(Choice)
                # user_list_printer(customer_ssn_list)
                # customer_ssn_list.clear()
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
                    ##########################Breita hér#################################
                    SSN = Choice
                    Name = Choice
                    count = False
                    ##########################Breita hér#################################
                    # customer_name_list = customer_service.get_customer_name(Choice)
                    # user_list_printer(customer_name_list)
                    # customer_name_list.clear()    
        return SSN, Name
    def dates():
        count = 1
        while count != 4:
            if count = 1:
                print("\nEnter in the date you whant to pick up a car\n")
                un_func.printer()
                Choice = input("Choice: ").lower()
                un_func.printline()
                if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
                    count = 4
                elif len(Choice) == 10:
                    try:
                        day, month, year = Choice.replace("/", " ").split()
                        Tester, start_date = un_func.date_chack(day, month, year, Tester)
                        count += 1
                    except ValueError:
                        Tester = False
                        print("\nERROR: Something went wrong with your input please try again\n")
                        printline()
            elif count = 2:
                print("\nEnter in the date you whant to return a car\n")
                un_func.printer()
                Choice = input("Choice: ").lower()
                un_func.printline()
                if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
                    count = 4
                elif len(Choice) == 10:
                    try:
                        day, month, year = Choice.replace("/", " ").split()
                        Tester, end_date = un_func.date_chack(day, month, year, Tester)
                        count += 1
                    except ValueError:
                        Tester = False
                        print("\nERROR: Something went wrong with your input please try again\n")
                        printline()
            elif count = 3:
                pass
        return start_date, end_date
    # def availabel_cars():
    #     return licence_plate, additional_insurance
    # def paymant():
    #     return paymant_way
    SSN, Name = User()
    start_date, end_date = dates()
    # licence_plate, additional_insurance = availabel_cars()
    # paymant_way = paymant()
    print(SSN)
    print(Name)
    print(start_date)
    print(end_date)