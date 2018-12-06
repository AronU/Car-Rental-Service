from models.Car import Car
import csv

class CarRepository:

    def __init__(self):
        #self.__cars = []
        self.__available_cars = []
        self.__unavailable_cars = []

    def get_available_cars(self):
        '''Reads the data file. Splits each line up into the cars attributes,
        although we only care about availability this time. If the availability
        is 1, then it puts it into the list. This list will therefore be 
        containing all available cars. -Aron'''
<<<<<<< HEAD
        with open("Car-Rental-Service/Car_rental/data/cars.csv", "r") as car_file:
=======
        with open("./data/cars.csv", "r") as car_file:
>>>>>>> 25799a71f319ea4e38156986e4b994c547b47629
            csv_reader = csv.reader(car_file)
            next(csv_reader)
            for line in csv_reader:
                if line[4] == "1":
                    self.__available_cars.append(line)    
            return self.__available_cars

    def get_unavailable_cars(self):
        '''Reads the data file. Splits each line up into the cars attributes,
        although we only care about availability this time. If the availability
        is 0, then it puts it into the list. This list will therefore be 
        containing all unavailable cars. -Aron'''
        with open("Car-Rental-Service/Car_rental/data/cars.csv", "r") as car_file:
            csv_reader = csv.reader(car_file)
            next(csv_reader)
            for line in csv_reader:
                if line[4] == "0":
                    self.__unavailable_cars.append(line)    
            return self.__unavailable_cars

