from models.Customer import Customer
import csv

class CustomerRepository:

    def __init__(self):
        self.__customers = []
    
    def add_customer(self, customer):
<<<<<<< HEAD
        with open("Car_Rental/data/customers.csv", "a+") as customers_file:
=======
        with open("./data/customers.csv", "a+") as customers_file:
            customers_file.write('\n' + customer.__repr__())
    
    def remove_customer(self, customer):
        with open("./data/customer.csv", "a") as customers_file:
>>>>>>> 51ae59cd609f3005097f32ee8a2131e667890cf7

            csv_writer = csv.writer(customers_file)
            csv_writer.writerow(Customer.__repr__() + '\n')

    def get_customer_name(self, name):
        with open("Car-Rental-Service/Car_Rental/data/customers.csv", "r") as customers_file:
            csv_reader = csv.reader(customers_file)
            next(csv_reader)
            for line in csv_reader:
                if name in line[0]:
                    return line
                

    def get_customer_ssn(self, ssn):
        with open("Car-Rental-Service/Car_Rental/data/customers.csv", "r") as customers_file:
            csv_reader = csv.reader(customers_file)
            next(csv_reader)
            for line in csv_reader:
                if line[1] == ssn:
                    return line
                    
    
<<<<<<< HEAD
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
=======
    def get_customers(self):
        customers = []
        with open("./data/customer.csv", "r") as customers_file:
            for line in customers_file.readlines():
                customer = eval(line.strip())
                customers.append(customer)
        return customers
>>>>>>> 51ae59cd609f3005097f32ee8a2131e667890cf7
