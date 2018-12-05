from services.CustomerService import CustomerService
from models.Customer import Customer

Quit_1 = "q"
Quit_2 = "quit"

<<<<<<< HEAD
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

=======
Quit = "q"
ONE = "1"
#test Thelma
>>>>>>> 5f9b2bf70e96cc57946b745627899431caa83a11
class SalesmanUI:

    def __init__(self):
        self.__customer_service = CustomerService()

    def main_menu(self):

        action = ""
        while(action != Quit_1 or action != Quit_2):
            print("Welcome to the central hub of the program.\n")
            print("1.  Register User")
            print("2.  Car list")
            print("3.  Search User")
            print("4.  Search order")
            print("5.  Make order")
            print("6.  Calculate cost")
            print("7.  Return a car")
            print("8.  Price list\n")
            print("Press q to Quit")
            print("--"*25)
            action = input("Choose an option: ").lower()

            if action == ONE_1 or action == ONE_2:
                name = input("Full name: ")
                ssn = input("SSN: ")
                address = input("Home address: ")
                phone = input("Phone number: ")
                birthday = input("Birthday: ")
                new_customer = Customer(name, ssn, address, phone, birthday)
                self.__customer_service.add_customer(new_customer)

            #elif action == "2":
            #    videos = self.__video_service.get_videos()
            #    print(videos)
                    