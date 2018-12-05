class Car:
    def __init__(self, licence_plate, brand, model, year, availability=1):
        self.__licence_plate = licence_plate
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__availability = availability

    def __str__(self):
        return "{},{},{},{},{}".format(self.__licence_plate, self.__brand, self.__model, self.__year, self.__availability)

    def __repr__(self):
        return self.__str__()

    def get_licence_plate(self):
        return self.__licence_plate

    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year

    def get_availability(self):
        return self.__availability
