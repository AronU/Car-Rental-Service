from services.CustomerService import CustomerService #Gains access to the CustomerService class in /services folder.
from models.Customer import Customer #Gets acces to the Customer class in /models folder. Used to create a user.
from ui.Register_User_func import RegisterUser
import ui.Register_User_func as reg_func
from ui.Universal_func import printline
import ui.Universal_func as un_func
from ui.Car_list_func import Carlist
import ui.Car_list_func as car_func

Quit_1 = "q"

ONE_1 = "1"
ONE_2 = "register user"

Two_1 = "2"
Two_2 = "car list"

Three_1 = "3"
Three_2 = "search user"

Four_1 = "4"
Four_2 = "search order"

Five_1 = "5"
Five_2 = "make order"

Six_1 = "6"
Six_2 = "calculate cost"

Seven_1 = "7"
Seven_2 = "return a car"

Eight_1 = "8"
Eight_2 = "price list"

class SalesmanUI:

    def __init__(self):
        self.__customer_service = CustomerService()

    def main_menu(self):

        action = ""
        while(action != Quit_1):
            print("Welcome to the central hub of the program.\n")
            print("1.  Register User\n2.  Car list\n3.  Search User\n4.  Search order\n5.  Make order")
            print("6.  Calculate cost\n7.  Return a car\n8.  Price list\n\nPress q to Quit")
            un_func.printline()
            action = input("Choose an option: ").lower()
            un_func.printline()

            if action == ONE_1 or action == ONE_2:
                name, ssn, address, phone, birthday = reg_func.RegisterUser()
                # make sure if the user dissident to go back to the mane menu 
                # halfway through that a have made user is not created 
                if name != "0" and ssn != "0" and address != "0" and phone != "0" and birthday != "0":
                    new_customer = Customer(name, ssn, address, phone, birthday)
                    self.__customer_service.add_customer(new_customer)

            elif action == Two_1 or action == Two_2:
                car_func.Carlist()