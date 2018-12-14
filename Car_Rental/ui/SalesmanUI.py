# Gains access to the CustomerService class in /services folder.
from services.CustomerService import CustomerService 
# Gets acces to the Customer class in /models folder. Used to create a user.
from models.Customer import Customer 
from models.Order import Order
# Gets acces to the RegisterUser function in the Register_User_func named reg_func in the code
# Used to make user in oppositions one in the mane menu
from ui.Register_User_func import RegisterUser
import ui.Register_User_func as reg_func
# Gets acces to the printline function in the Universal_func named un_func in the code
# All over the place in the ui
from ui.Universal_func import printline
import ui.Universal_func as un_func
# Gets acces to the Carlist function in the Car_list_func named car_func in the code
# Used to list Available and Unavailable cars in oppositions two in the mane menu
from ui.Car_list_func import Carlist
import ui.Car_list_func as car_func

from ui.User_list_func import Search_menu
import ui.User_list_func as user_func

# This gives the function access to the Pricelist function in Price_list_func.
from ui.Price_list_func import Pricelist
# This names the Price_list_func price_func.
import ui.Price_list_func as price_func

from ui.Return_Car_func import returncar
import ui.Return_Car_func as ret_car_func

from services.CarService import CarService

from ui.order_func import order_menu
import ui.order_func as order

from ui.Search_user_func import search_user
import ui.Search_user_func as search_u

from ui.Order_menu import Search_order_menu
import ui.Order_menu as order_m

from ui.Calculate_cost import calculate_cost_menu
import ui.Calculate_cost as calc_cost_m

from services.OrderService import OrderService

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
        self.__order_service = OrderService()

    def main_menu(self):

        action = ""
        while(action != Quit_1):
            un_func.cls()
            print("Welcome to the central hub of the program.\n")
            print("1.  Register user\n2.  Car list\n3.  Customer menu\n4.  Search order\n5.  Make order")
            print("6.  Calculate cost\n7.  Return a car\n8.  Price list\n9.  Car history\n\nPress q to Quit")
            un_func.printline()
            action = input("Choose an option: ").lower()
            un_func.printline()

            if action == ONE_1 or action == ONE_2:
                name, ssn, address, phone, birthday = reg_func.RegisterUser()
                # Make sure if the user doesn't go back to the main menu 
                # halfway through that a have made user is not created 
                if name != "0" and ssn != "0" and address != "0" and phone != "0" and birthday != "0":
                    new_customer = Customer(name, ssn, address, phone, birthday)
                    self.__customer_service.add_customer(new_customer)

            elif action == Two_1 or action == Two_2:
                car_func.Carlist()

            elif action == Three_1 or action == Three_2:
                user_func.Search_menu()

            elif action == Four_1 or action == Four_2:
                order_m.Search_order_menu()

            elif action == Five_1 or action == Five_2:
                ID, licence_plate, ssn, name, start_date, end_date, payment_way, additional_insurance = order.order_menu()
                # make sure if the user dissident to go back to the mane menu 
                # halfway through that a have made order is not place 
                if ssn != "0" and name != "0" and start_date != "0" and end_date != "0" and licence_plate != "0" and additional_insurance != "0" and payment_way != "0" and ID != "0":
                    new_order = Order(ID, licence_plate, ssn, name, start_date, end_date, payment_way, additional_insurance)
                    self.__order_service.add_order(new_order)

            elif action == Six_1 or action == Six_1:
                calc_cost_m.calculate_cost_menu()

            elif action == Seven_1 or action == Seven_2:
                licence_plate = ret_car_func.returncar()
                if licence_plate != "0":
                    car_service = CarService()
                    car_service.return_car(licence_plate)
            
            elif action == Eight_1 or action == Eight_2:
                price_func.Pricelist()
