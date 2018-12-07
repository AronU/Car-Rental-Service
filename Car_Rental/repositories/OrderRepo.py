from models.Order import Order
import csv

class OrderRepository:

    def __init__(self):
        self.__all_orders = []

    def add_order(self, order):
        with open("./data/orders.csv", "a+") as orders_file:
            orders_file.write('\n' + order.__repr__())