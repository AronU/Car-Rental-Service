# This imports the csv built-in 
# Gives the function access to the printline function in Universal_func named un_func
from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

import csv

# Constant variables used as commands in the input.
Back_1 = "b"
Back_2 = "back"
Home_1 = "h"
Home_2 = "main menu"

class PriceRepository:

    def __init__(self):
        self.__LowPrice = []
        self.__MediumPrice = []
        self.__HighPrice = []
    
    def get_LowPrice(self):
        with open("Car_Rental/data/cars.csv", "r") as price_file:
            csv_reader = csv.reader(price_file)
            next(csv_reader)
            for line in csv_reader:
                if 0 < line[5] < "11000":
                    self.__LowPrice.append(line)
        return self.__LowPrice

    def get_MediumPrice(self):
        with open("Car_Rental/data/cars.csv", "r") as price_file:
            csv_reader = csv.reader(price_file)
            next(csv_reader)
            for line in csv_reader:
                if "11000" <= line[5] < "20000":
                    self.__MediumPrice.append(line)
        return self.__MediumPrice
    
    def get_HighPrice(self):
        with open("Car_Rental/data/cars.csv", "r") as price_file:
            csv_reader = csv.reader(price_file)
            next(csv_reader)
            for line in csv_reader:
                if line[5] >= "20000":
                    self.__HighPrice.append(line)
        return self.__HighPrice

    def get_all_prices(self):
        with open("./data/cars.csv", "r") as price_file:
            self.__AllPrices = []
            csv_reader = csv.reader(price_file)
            next(csv_reader)
            for line in csv_reader:
                self.__AllPrices.append(line)
        return self.__AllPrices
