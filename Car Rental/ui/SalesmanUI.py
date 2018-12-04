from services.CustomerService import CustomerService
from models.Customer import Customer

class SalesmanUI:

    def __init__(self):
        self.__customer_service = CustomerService()

    def main_menu(self):

        action = ""
        while(action != "q"):
            print("You can do the following: ")
            print("1. Add a customer")
            #print("2. List all videos")
            print("press q to quit")

            action = input("Choose an option: ").lower()

            if action == "1":
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
                    