from services.CustomerService import CustomerService

customer_service = CustomerService()
while True:
    ssn = input("SSN: ")
    check = customer_service.valid_customer_check(ssn)
    if check == True:
        customer_service.remove_customer(ssn)
