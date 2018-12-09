from models.Order import Order
import csv
import random

class OrderRepository:

    def __init__(self):
        pass

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
                return random_id

    def get_all_ids(self):
        id_list = []
        with open('./data/IDs.csv', 'r') as id_file:
            csv_reader = csv.reader(id_file)
            next(csv_reader)
            for row in csv_reader:
                id_list.append(row)
            return id_list