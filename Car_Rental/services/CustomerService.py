from repositories.CustomerRepo import CustomerRepository

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)
    
    def get_customer_name(self, name):
        user_list = self.__customer_repo.get_customer(name)
        return user_list

    def is_valid_customer(self, customer):
        #Validation checks, could check if customers already 
        #exists etc. 
        return True