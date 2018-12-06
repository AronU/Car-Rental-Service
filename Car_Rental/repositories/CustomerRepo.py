from models.Customer import Customer
import csv

class CustomerRepository:

    def __init__(self):
        self.__customers = []
    
    def add_customer(self, customer):
        with open("Car_Rental/data/customers.csv", "a+") as customers_file:
            customers_file.writer('\n' + customer.__repr__())
    
    def remove_customer(self, customer):
        with open("Car_Rental/data/customer.csv", "a") as customers_file:

            csv_writer = csv.writer(customers_file)
            for row in csv_writer:
                if row == csv_writer:
                    row = 0
    
    def get_customers(self):
        customers = []
        with open("Car_Rental/data/customer.csv", "r") as customers_file:
            for line in customers_file.readlines():
                customer = eval(line.strip())
                customers.append(customer)
        return customers
