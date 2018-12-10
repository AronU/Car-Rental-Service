from repositories.CustomerRepo import CustomerRepository

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        self.__customer_repo.add_customer(customer)
    
    def get_customer_name(self, name):
        user_list_name = self.__customer_repo.get_customer_name(name)
        return user_list_name

    def get_customer_ssn(self, ssn):
        user_list_ssn = self.__customer_repo.get_customer_ssn(ssn)
        return user_list_ssn

    def is_valid_customer(self, customer):
        #Validation checks, could check if customers already 
        #exists etc. 
        return True

    def valid_check_ssn(self, ssn):
        '''Verifies if the ssn it is given is real or not.'''
        valid_check = self.__customer_repo.verify_ssn(ssn)
        return valid_check
