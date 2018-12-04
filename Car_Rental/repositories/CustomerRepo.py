from models.Customer import Customer

class CustomerRepository:

    def __init__(self):
        self.__customers = []
    
    def add_customer(self, customer):
        with open("./data/customers.txt", "a+") as customers_file:
            name = customer.get_name()
            ssn = customer.get_ssn()
            address = customer.get_address()
            phone = customer.get_phone()
            birthday = customer.get_birthday()
            customers_file.write("{},{},{},{},{}\n".format(name, ssn, 
        address, phone, birthday))
