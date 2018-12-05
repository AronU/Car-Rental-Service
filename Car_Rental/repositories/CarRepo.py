from models.Car import Car
import csv

class CarRepository:

    def __init__(self):
        #self.__cars = []
        self.__available_cars = []

    def get_available_cars(self):
    '''Reads the data file. Splits each line up into the cars
        attributes, although we only care about availability this time.
        If the availability is 1, then it puts it into the list. This list
        will therefore be containing all available cars. -Aron 05/12/2018'''

        with open("./data/cars.csv") as car_file:
            csv_reader = csv.reader(car_file)
            next(csv_reader)
            for line in csv_reader:
                #licence_plate, brand, model, year, availability = line.split(",")
                if line[3] == 1:
                    self.__available_cars.append(line)    
        
        return self.__available_cars

    def get_unavailable_cars(self):
    '''Reads the data file. Splits each line up into the cars
        attributes, although we only care about availability this time.
        If the availability is 0, then it puts it into the list. This list
        will therefore be containing all unavailable cars. -Aron 05/12'''

        with open("./data/Cars.txt", "r") as car_file:
            for line in car_file.readlines():
                licence_plate, brand, model, year, availability = line.split(",")
                if availability == 0:
                    unavailable_car = Car(licence_plate, brand, model, year, availability)
                    self.__unavailable_cars.append(unavailable_car)    
        
        return self.__unavailable_cars