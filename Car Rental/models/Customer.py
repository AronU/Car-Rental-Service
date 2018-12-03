class Customer:
    def __init__(self, name, ssn, address, phone, birthday):
        self.__name = name
        self.__ssn = ssn
        self.__address = address
        self.__phone = phone
        self.__birthday = birthday

    def __str__(self):
        return "{},{},{},{},{}".format(self.__name, self.__ssn, 
        self.__address, self.__phone, self.__birthday)
    
    def __repr__(self):
        return self.__str__()
    
    def get_name(self):
        return self.__name

    def get_ssn(self):
        return self.__ssn

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_birthday(self):
        return self.__birthday

Aron = Customer("Aron Úlfarsson", 2904972649, "Furugrund", 8620273, "29/04/1997")
print(Aron)
