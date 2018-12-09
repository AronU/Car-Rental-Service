# This gives the class in this file access to the 
from models.Customer import Customer
import csv

class CustomerRepository:

    def __init__(self):
        self.__customers = []
    
    def add_customer(self, customer):
        with open("./data/customers.csv", "a+") as customers_file:
            customers_file.write('\n' + customer.__repr__())
    
    # def remove_customer(self, customer):
    #     with open("./data/customer.csv", "a") as customers_file:

    #         csv_writer = csv.writer(customers_file)
    #         for row in csv_writer:
    #             if row == csv_writer:
    #                 row = 0
    
    # def get_customers(self):
    #     customers = []
    #     with open("./data/customer.csv", "r") as customers_file:
    #         for line in customers_file.readlines():
    #             customer = eval(line.strip())
    #             customers.append(customer)
    #     return customers

    # Find customer according to their name
    def get_customer_name(self, name):
        with open("Car-Rental-Service/Car_Rental/data/customers.csv", "r") as customers_file:
            csv_reader = csv.reader(customers_file)
            next(csv_reader)
            for line in csv_reader:
                # Check if the input is equal to the name in the list, the only part of the name that is checked is the part
                # that is equal to the lenght of the input. For example if the input is "ar" then the only part of the string 
                # that is checked is equal to the len(name)
                if name.lower() == line[0][:len(name)].lower():
                    self.__customer_name.append(line)
            return self.__customer_name
                
    # Find customer according to their SSN
    def get_customer_ssn(self, ssn):
        with open("Car-Rental-Service/Car_Rental/data/customers.csv", "r") as customers_file:
            csv_reader = csv.reader(customers_file)
            next(csv_reader)
            for line in csv_reader:
                # See if the SSN list item is equal to the input
                if line[1] == ssn:
                    self.__customer_ssn.append(line)
            return self.__customer_ssn
                    
    
    # Delete user class unfinished
    ###############################################
    # def remove_customer(self, deleted_ssn):     
    #     with open('./data/customers.csv', 'r') as inp, open('temp.csv', 'w') as out:
    #         writer = csv.DictWriter(out, fieldnames=['name', 'SSN', 'Address','phone','DoB'])
    #         writer.writeheader()
    #         for row in csv.DictReader(inp):
    #             if row['SSN'] != :
    #                 writer.writerow(row)           
    ###############################################       
            

        #     name = customer.get_name()
        #     ssn = customer.get_ssn()
        #     address = customer.get_address()
        #     phone = customer.get_phone()
        #     birthday = customer.get_birthday()
        #     customers_file.write("{},{},{},{},{}\n".format(name, ssn, 
        # address, phone, birthday))
