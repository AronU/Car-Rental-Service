from models.Customer import Customer
import csv

class CustomerRepository:

    def __init__(self):
        self.__customers = []
        self.__customer_name = []
        self.__customer_ssn = []
    
    def add_customer(self, customer):
        with open("Car_Rental/data/customers.csv", "a+") as customers_file:

            csv_writer = csv.writer(customers_file)
            csv_writer.writerow(Customer.__repr__() + '\n')

    def get_customer_name(self, name):
        with open("Car-Rental-Service/Car_Rental/data/customers.csv", "r") as customers_file:
            csv_reader = csv.reader(customers_file)
            next(csv_reader)
            for line in csv_reader:
                if name.lower() == line[0][:len(name)].lower():
                    self.__customer_name.append(line)
            return self.__customer_name
                

    def get_customer_ssn(self, ssn):
        with open("Car-Rental-Service/Car_Rental/data/customers.csv", "r") as customers_file:
            csv_reader = csv.reader(customers_file)
            next(csv_reader)
            for line in csv_reader:
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
