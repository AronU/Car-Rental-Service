from models.Customer import Customer
import csv

class CustomerRepository:

    def __init__(self):
        self.__customers = []
    
    def add_customer(self, customer):
        with open("./data/customers.csv", "a+") as customers_file:

            csv_writer = csv.writer(customers_file)
            csv_writer.writerow(Customer.__repr__() + '\n')
    
    # Delete user class unfinished

    # def remove_customer(self, deleted_ssn):     
    #     with open('./data/customers.csv', 'r') as inp, open('temp.csv', 'w') as out:
    #         writer = csv.DictWriter(out, fieldnames=['name', 'SSN', 'Address','phone','DoB'])
    #         writer.writeheader()
    #         for row in csv.DictReader(inp):
    #             if row['SSN'] != :
    #                 writer.writerow(row)           
            
            

        #     name = customer.get_name()
        #     ssn = customer.get_ssn()
        #     address = customer.get_address()
        #     phone = customer.get_phone()
        #     birthday = customer.get_birthday()
        #     customers_file.write("{},{},{},{},{}\n".format(name, ssn, 
        # address, phone, birthday))
