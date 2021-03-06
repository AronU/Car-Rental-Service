import datetime
class Order:
    def __init__(self, ID, licence_plate, ssn, name, start_date, end_date, payment_way, additional_insurance="No"):
        self.__ID = ID
        self.__licence_plate = licence_plate
        self.__ssn = ssn    
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__payment_way = payment_way
        self.__additional_insurance = additional_insurance

    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(self.__ID, self.__licence_plate, self.__ssn, 
        self.__name, self.__start_date, self.__end_date, self.__payment_way, self.__additional_insurance)

    def __repr__(self):
        return self.__str__()

    def get_ID(self):
        return self.__ID
    
    def get_licence_plate(self):
        return self.__licence_plate

    def get_ssn(self):
        return self.__ssn
    
    def get_name(self):
        return self.__name

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date
    
    def get_payment_method(self):
        return self.__payment_way
    
    def get_additional_insurance(self):
        return self.__additional_insurance