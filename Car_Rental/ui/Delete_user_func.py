# Gets access to the printline function in the Universal_func named
# un_func in the code
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from services.CustomerService import CustomerService

Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def Delete_User():
    customer_service = CustomerService()
    count = True
    while count == True:
        print("Enter in the SSN of the User you whant to Delete\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2:
            return False
        elif Choice == Back_1 or Choice == Back_2:
            return True
        else:
            T_or_F = customer_service.valid_customer_check(Choice)
            if T_or_F == True:
                print("Are you sure you want to delete the user: "+ Choice +" (Y/N)?\n")
                un_func.printer()
                Yes_or_no = input("Choice: ").lower()
                un_func.printline()
                if Yes_or_no == Home_1 or Yes_or_no == Home_2:
                    count = False
                elif Yes_or_no == Back_1 or Yes_or_no == Back_2 or Yes_or_no == "n":
                    count = True
                elif Yes_or_no == "y":
                    customer_service.remove_customer(Choice)
                    print("Customer Has been deleted.")
                    un_func.printline()
                    count = False
            else:
                print("\nERROR: SSN you entered is not currently in the system\n")
                un_func.printline()