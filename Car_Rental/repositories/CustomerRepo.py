# This gives the class in this file access to the Customer class which is stored in the models folder.
from models.Customer import Customer
# This imports the CSV module, which includes all the necessary built-in functions, and allows this file(the class) to parse CSV files.
import csv
import os

class CustomerRepository:

    def __init__(self):
        self.__customers = []
        self.__customer_name = []
        self.__customer_ssn = []
    
    def add_customer(self, customer):
        ''' This function opens the csv file and appends the new customer that was input into the file. '''
        with open("./data/customers.csv", "a+") as customers_file:
            customers_file.write('\n' + customer.__repr__())
    
    def remove_customer(self, ssn):
        '''Function removes the customer based on the ssn given. -Aron'''
        with open("./data/customers.csv", "r") as customers_file, open('./data/temp.csv', 'w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=['name', 'ssn', 'address', 'phone', 'birthday'])
            writer.writeheader()
            for row in csv.DictReader(customers_file):
                if row['ssn'] != ssn:
                    writer.writerow(row)

        os.remove('./data/customers.csv')
        os.rename('./data/temp.csv', './data/customers.csv')
    
    # Find customer according to their name
    def get_customer_name(self, name):
        with open("./data/customers.csv", "r") as customers_file:
            csv_reader = csv.reader(customers_file)
            next(csv_reader)
            for line in csv_reader:
                # Check if the input is equal to the name in the list, the only part of the name that is checked is the part
                # that is equal to the lenght of the input. For example if the input is "ar" then the only part of the string 
                # that is checked is equal to the len(name)
                try:
                    if name.lower() == line[0][:len(name)].lower():
                        self.__customer_name.append(line)
                except IndexError:
                    pass
            return self.__customer_name
                
    # Find customer according to their SSN
    def get_customer_ssn(self, ssn):
        with open("./data/customers.csv", "r") as customers_file:
            csv_reader = csv.reader(customers_file)
            next(csv_reader)
            for line in csv_reader:
                # See if the SSN list item is equal to the input
                try:
                    if ssn == line[1][:len(ssn)]:
                        self.__customer_ssn.append(line)
                except IndexError:
                    pass
            return self.__customer_ssn

    def edit_user(self, ssn, choice, new_input):
        '''This function is used to edit the user that has the SSN that is
            inputted '''
        with open('./data/customers.csv', 'r') as inp, open('./data/temp.csv', 'w', newline='') as out:
            writer = csv.DictWriter(out, fieldnames=['name', 'ssn', 'address', 'phone', 'birthday'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['ssn'] == ssn:
                    if choice == "1":
                        row['name'] = new_input
                        writer.writerow(row)
                    elif choice == "2":
                        row['address'] = new_input
                        writer.writerow(row)
                    elif choice == "3":
                        row['phone'] = new_input
                        writer.writerow(row)
                    elif choice == "4":
                        row['birthday'] = new_input
                        writer.writerow(row)
                else:
                    writer.writerow(row)
        os.remove('./data/customers.csv')
        os.rename('./data/temp.csv', './data/customers.csv')

    def get_user_history(self, ssn):
        '''Takes in a customers SSN. From that the function gathers all 
        orders from the orders data file that matches with that SSN. 
        Returns it in a list. - Aron'''
        user_history = []
        with open("./data/orders.csv", "r") as order_file:
            csv_reader = csv.reader(order_file)
            next(csv_reader)
            for line in csv_reader:
                try:
                    if line[2] == ssn:
                        user_history.append(line)    
                except IndexError:
                    pass
            return user_history
