from repositories.CustomerRepo import CustomerRepository

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        self.__customer_repo.add_customer(customer)
    
    def get_customer_name(self, name):
<<<<<<< HEAD
        user_list = self.__customer_repo.get_customers(name)
=======
        user_list = self.__customer_repo.get_customer_name(name)
>>>>>>> 628fb40f614e79a78ffa3b37ee8b252297e87d39
        return user_list

    def get_customer_ssn(self, ssn):
        user_list_ssn = self.__customer_repo.get_customer_ssn(ssn)
        return user_list_ssn

    def is_valid_customer(self, customer):
        #Validation checks, could check if customers already 
        #exists etc. 
        return True
