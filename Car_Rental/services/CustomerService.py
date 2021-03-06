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

    def valid_customer_check(self, ssn):
        '''Verifies if the user exists, returns True if he does, False if not. -Aron'''
        user_list_ssn = self.__customer_repo.get_customer_ssn(ssn)
        if user_list_ssn == []:
            return False
        else:
            return True
    
    def remove_customer(self, ssn):
        '''Sends over the ssn to the repo to delete the user. - Aron'''
        self.__customer_repo.remove_customer(ssn)

    def edit_customer(self, ssn, choice, new_input):
        self.__customer_repo.edit_user(ssn, choice, new_input)

    def user_history(self, ssn):
        return self.__customer_repo.get_user_history(ssn)
