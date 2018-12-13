import csv
import os
from datetime import date, datetime

class CarRepository:

    def __init__(self):
        self.__available_cars = []
        self.__unavailable_cars = []
        self.__all_cars = []
        self.__licence_plate = []

    def get_current_cars_by_status(self, choice):
        '''This is the main car list function. It handles both available and unavailable cars at the same time.
        It gets the choice of available or unavailable cars from the service layer. - Aron'''
        with open("./data/orders.csv", "r") as orders_file:
            unavailable_car_by_order_list = []

            all_cars = []
            available_cars = []
            unavailable_cars = []

            csv_reader = csv.reader(orders_file)
            current_date = datetime.now().date()
            next(csv_reader)
            for line in csv_reader:
                year, month, day = line[4].split("-")
                check_start_date = date(int(year), int(month), int(day))
                year2, month2, day2 = line[5].split("-")
                check_end_date = date(int(year2), int(month2), int(day2))
                if check_start_date <= current_date and current_date <= check_end_date:
                    unavailable_car_by_order_list.append(line[1])

        with open("./data/cars.csv", "r") as car_file:
            csv_reader = csv.reader(car_file)
            next(csv_reader)
            for line in csv_reader:
                all_cars.append(line)

        for x in range(len(all_cars)):
            if len(unavailable_car_by_order_list) > 0:
                for y in range(len(unavailable_car_by_order_list)):
                    if unavailable_car_by_order_list[y] == all_cars[x][0]:
                        unavailable_cars.append(all_cars[x])
                    else:
                        available_cars.append(all_cars[x])
            else:
                available_cars.append(all_cars[x])

        if choice == 0:
            return unavailable_cars
        else:
            return available_cars


    def get_all_cars(self):
        '''Reads the data file. splits each line up into the cars attributes,
        and returns all cars regardless of availability.'''
        with open("./data/cars.csv", "r") as car_file:
            all_cars = []
            csv_reader = csv.reader(car_file)
            next(csv_reader)
            for line in csv_reader:
                all_cars.append(line)
            return all_cars


    def get_car_licence_plate(self, licence_plate):
        '''Reads the data file. splits each line up into the cars
        attributes. and returns the car with the matching licence 
        plate '''
        with open("./data/cars.csv", "r") as licence_plate_file:
            csv_reader = csv.reader(licence_plate_file)
            next(csv_reader)
            for line in csv_reader:
                if line[0] == licence_plate:
                    self.__licence_plate.append(line)
            return self.__licence_plate

    
    def return_car(self, licence_plate):
        '''This function changes the end date of a order to communicate the fact that the car in 
        question has been returned prematurely/canceled. - Aron'''
        with open('./data/orders.csv', 'r') as inp, open('./data/temp.csv', 'w', newline='') as out:
            writer = csv.DictWriter(out, fieldnames=['id', 'licence plate', 'SSN', 'name', 'start date', 
            'end date', 'payment info', 'additional insurance'])
            writer.writeheader()
            current_date = datetime.now().date()
            for row in csv.DictReader(inp):
                if row['licence plate'] == licence_plate:
                    year, month, day = row['start date'].split("-")
                    check_start_date = date(int(year), int(month), int(day))
                    year2, month2, day2 = row['end date'].split("-")
                    check_end_date = date(int(year2), int(month2), int(day2))
                    if check_start_date <= current_date and current_date <= check_end_date:
                        row['end date'] = current_date
                        writer.writerow(row)
                    else:
                        writer.writerow(row)
                else:
                    writer.writerow(row) 
        os.remove('./data/orders.csv')
        os.rename('./data/temp.csv', './data/orders.csv')

    def verify_licence_plate(self, licence_plate):
        '''Verifies that the car given exists. - Aron'''
        with open('./data/cars.csv', 'r') as car_file:
            csv_reader = csv.reader(car_file)
            next(csv_reader)
            for row in csv_reader:
                if row[0] == licence_plate:
                    return True
            return False
                
    def car_price(self, licence_plate):
        '''Returns the day price of the car requested as an integer. - Aron'''  
        with open('./data/cars.csv', 'r') as car_file:
            price = ""
            for row in csv.DictReader(car_file):
                if row['Licence plate'] == licence_plate:
                    price = row['Price']
                    price = int(price)
                    return price   

    def car_history(self, licence_plate):
        '''Takes in a cars licence plate. From that the function gathers all 
        orders from the orders data file that matches with that licence plate. 
        Returns it in a list. - Aron'''
        car_history = []
        with open("./data/orders.csv", "r") as order_file:
            csv_reader = csv.reader(order_file)
            next(csv_reader)
            for line in csv_reader:
                if line[1] == licence_plate:
                    car_history.append(line)    
            return car_history
        