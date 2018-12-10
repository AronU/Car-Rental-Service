# Gets access to the printline function in the Universal_func named
# un_func in the code
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func
# Gets access to the CustomerService class in the service folder
from services.CustomerService import CustomerService

from ui.Search_user_func import search_user
import ui.Search_user_func as search_u

from ui.Edit_user_func import edit_user
import ui.Edit_user_func as edit_u

# constant variables to be used to take in commands through the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"


def Search_menu():
    count = True
    while count == True:
        print("1.  Search by Name or by SSN or leave empty for full list\n2.  Edit customer by name or SSN\n3.  Delete customer by SSN")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            count = False
        elif Choice == "1":
            search_u.search_user()
        elif Choice == "2":
            edit_u.edit_user()