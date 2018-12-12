from models.Order import Order
import csv
import random
from datetime import date, datetime

class OrderRepository:

    def __init__(self):
        self.__order_ssn = []
        self.__order_licence_plate = []

    def add_order(self, order):
        with open("./data/orders.csv", "a+") as orders_file:
            orders_file.write('\n' + order.__repr__())

    def set_random_id(self):
        id_list = self.get_all_ids()
        while True:
            hit = False
            random_id = random.randint(1, 100000)
            for i in id_list:
                if int(i[0]) == random_id:
                    hit = True
            if hit == True:
                pass
            else:
                with open("./data/IDs.csv", "a+", newline='') as IDs_file:
                    IDs_file.write('\n' + str(random_id))
                return random_id

    def get_all_ids(self):
        id_list = []
        with open('./data/IDs.csv', 'r') as id_file:
            csv_reader = csv.reader(id_file)
            next(csv_reader)
            for row in csv_reader:
                id_list.append(row)
            return id_list
    
    def cancel_order_status(self, ssn, licence_plate):
        '''This function switches the order given based on ssn or licence plate to 0. 
        Making the order "inactive". - Aron'''
        with open('./data/orders.csv', 'r') as inp, open('./data/temp.csv', 'w', newline='') as out:
            writer = csv.DictWriter(out, fieldnames=['id', 'licence plate', 'SSN', 'name', 'start date', 'end date', 'additional insurance', 'order status'])
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
                elif row['SSN'] == ssn:
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

    def catch_unavailable_cars(self, start_date, end_date):
        '''Function takes in start date and end date for a new order in the making. The function 
        compares these dates with already placed orders and gives a list of cars that are 
        UNAVAILABLE during these times. - Aron'''
        with open("./data/orders.csv", "r") as orders_file:
            unavailable_car_list = []
            csv_reader = csv.reader(orders_file)
            next(csv_reader)
            for line in csv_reader:
                year, month, day = line[4].split("-")
                check_start_date = date(int(year), int(month), int(day))
                year2, month2, day2 = line[5].split("-")
                check_end_date = date(int(year2), int(month2), int(day2))
                if check_start_date <= start_date and start_date <= check_end_date:
                    unavailable_car_list.append(line[1])
                elif check_start_date <= end_date and end_date <= check_end_date:
                    if line[1] in unavailable_car_list:
                        pass
                    else:
                        unavailable_car_list.append(line[1])
            return unavailable_car_list

    def get_available_cars(self, start_date, end_date):
        unavailable_car_list = self.catch_unavailable_cars(start_date, end_date)
        all_cars = []
        available_car_list = []
        with open("./data/cars.csv", "r") as car_file:
            csv_reader = csv.reader(car_file)
            next(csv_reader)
            for line in csv_reader:
                all_cars.append(line)
        for i in range(len(all_cars)):
            if all_cars[i][0] not in unavailable_car_list:
                available_car_list.append(all_cars[i])
        return available_car_list
            




    def get_order_ssn(self, ssn):
        with open("./data/orders.csv", "r") as orders_file:
            csv_reader = csv.reader(orders_file)
            next(csv_reader)
            for line in csv_reader:
                if line[2] == ssn:
                    self.__order_ssn.append(line)
            return self.__order_ssn


    def get_order_licence_plate(self, licence_plate):
        all_orders = []
        with open("./data/orders.csv", "r") as orders_file:
            csv_reader = csv.reader(orders_file)
            next(csv_reader)
            for line in csv_reader:
                all_orders.append(line)
            for i in range(len(all_orders)):
                if all_orders[i][1] == line[1][:len(licence_plate)].upper():
                    self.__order_licence_plate.append(all_orders[i])
            return self.__order_licence_plate
