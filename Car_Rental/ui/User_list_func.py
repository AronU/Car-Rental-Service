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

from ui.Delete_user_func import Delete_User
import ui.Delete_user_func as Delete_u

from ui.User_history_func import User_history
import ui.User_history_func as User_h

# constant variables to be used to take in commands through the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"



def Search_menu():
    count = True
    while count == True:
        print("1.  Search by Name, SSN or leave empty for full list\n2.  Edit customer by SSN\n3.  Delete customer by SSN\n4.  Search user by SSN to show User history\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            count = False
        elif Choice == "1":
            count = search_u.search_user()
        elif Choice == "2":
            count = edit_u.edit_user()
        elif Choice == "3":
            count = Delete_u.Delete_User()
        elif Choice == "4":
            count = User_h.User_history()