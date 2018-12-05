from models.Car import Car

class CarRepository:

    def __init__(self):
        #self.__cars = []
        self.__available_cars = []

    def get_available_cars(self):
    '''Reads the data file. Splits each line up into the cars
        attributes, although we only care about availability this time.
        If the availability is 1, then it puts it into the list. This list
        will therefore be containing all available cars. -Aron 05/12/2018'''

        with open("./data/Cars.txt", "r") as car_file:
            for line in car_file.readlines():
                licence_plate, brand, model, year, availability = line.split(",")
                if availability == 1:
                    available_car = Car(licence_plate, brand, model, year, availability)
                    self.__available_cars.append(available_car)    
        
        return self.__available_cars