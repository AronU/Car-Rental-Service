from models.Order import Order
import csv
import random

class OrderRepository:

    def __init__(self):
        pass

    def test(self, start_date=0, end_date=0):
        with open("./data/orders.csv", "r") as orders_file:
            print(orders_file)

P = OrderRepository.test(1)

print(P)