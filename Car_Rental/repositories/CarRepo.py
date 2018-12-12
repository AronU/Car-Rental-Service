#from models.Car import Car
import csv
import os

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
        with open("./data/cars.csv", "r") as car_file:
            self.__available_cars = []
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
        with open("./data/cars.csv", "r") as car_file:
            self.__unavailable_cars = []
            csv_reader = csv.reader(car_file)
            next(csv_reader)
            for line in csv_reader:
                if line[4] == "0":
                    self.__unavailable_cars.append(line)    
            return self.__unavailable_cars

    
    def get_all_cars(self):
        '''Reads the data file. splits each line up into the cars attributes,
        and returns all cars regardless of availability.'''
        with open("./data/cars.csv", "r") as car_file:
            self.__all_cars = []
            csv_reader = csv.reader(car_file)
            next(csv_reader)
            for line in csv_reader:
                self.__all_cars.append(line)
            return self.__all_cars

    
    def return_car(self, licence_plate):
        '''this function is used to switch the availability of the car it
        is given over to 'available' instead of unavailable.'''
        with open('./data/cars.csv', 'r') as inp, open('./data/temp.csv', 'w', newline='') as out:
            writer = csv.DictWriter(out, fieldnames=['Licence plate', 'Brand', 'Model', 'Year', 'Availability', 'Price'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['Licence plate'] == licence_plate:
                    if row['Availability'] == "0":
                        row['Availability'] = "1"
                        writer.writerow(row)
                else:
                    writer.writerow(row)
        # Til að eyða gömlu skránni og gera nýju skránna samnefnda gömlu skránni  
        os.remove('./data/cars.csv')
        os.rename('./data/temp.csv', './data/cars.csv')

    def verify_licence_plate(self, licence_plate):
        '''Verifies if the licence plate given is in the database and in a unavailable state. -Aron'''
        
        with open('./data/cars.csv', 'r') as car_file:
            #writer = csv.DictWriter(car_file, fieldnames=['Licence plate', 'Brand', 'Model', 'Year', 'Availability', 'Price'])
            #writer.writeheader()
            for row in csv.DictReader(car_file):
                if row['Licence plate'] == licence_plate:
                    if row['Availability'] == "1":
                        return True
                    elif row['Availability'] == "0":
                        return False


    def car_price(self, licence_plate):
        '''Verifies if the licence plate given is in the database and in a unavailable state. -Aron'''
        
        with open('./data/cars.csv', 'r') as car_file:
            #writer = csv.DictWriter(car_file, fieldnames=['Licence plate', 'Brand', 'Model', 'Year', 'Availability', 'Price'])
            #writer.writeheader()
            price = ""
            for row in csv.DictReader(car_file):
                if row['Licence plate'] == licence_plate:
                    price = row['Price']
                    price = int(price)
                    return price   
        