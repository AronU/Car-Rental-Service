# This gives the function access to the printer and printline functions in Universal_func.
from ui.Universal_func import printer, printline
# This names the Universal_func un_func.
import ui.Universal_func as un_func
# This imports the CSV module, which includes all the necessary built-in functions, and allows this file(the class) to parse CSV files.
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
        self.__AllPrices = []
    
    def get_LowPrice(self):
        ''' This function reads and fetches the contents in the csv file that is given. The function 
        reads through the data and checks if a specific data in each line is a low number. 
        If so it will store the line itself in a list. '''
        with open("./data/cars.csv", "r") as price_file:
            self.__LowPrice = []
            csv_reader = csv.reader(price_file)
            next(csv_reader)
            for line in csv_reader:
                line[5] = int(line[5])
                if 0 < line[5] < 11000:
                    self.__LowPrice.append(line)
        return self.__LowPrice

    def get_MediumPrice(self):
        ''' This function reads and fetches the contents in the csv file that is given. The function 
        reads through the data and checks if a specific data in each line is a medium number. 
        If so it will store the line itself in a list. '''
        with open("./data/cars.csv", "r") as price_file:
            self.__MediumPrice = []
            csv_reader = csv.reader(price_file)
            next(csv_reader)
            for line in csv_reader:
                line[5] = int(line[5])
                if 11000 <= line[5] < 20000:
                    self.__MediumPrice.append(line)
        return self.__MediumPrice
    
    def get_HighPrice(self):
        ''' This function reads and fetches the contents in the csv file that is given. The function 
        reads through the data and checks if a specific data in each line is a high number. 
        If so it will store the line itself in a list. '''
        with open("./data/cars.csv", "r") as price_file:
            self.__HighPrice = []
            csv_reader = csv.reader(price_file)
            next(csv_reader)
            for line in csv_reader:
                line[5] = int(line[5])
                if line[5] >= 20000:
                    self.__HighPrice.append(line)
        return self.__HighPrice

    def get_all_prices(self):
        ''' This function reads and fetches the contents in the csv file that is given and stores
        it's contents in a list. '''
        with open("./data/cars.csv", "r") as price_file:
            self.__AllPrices = []
            csv_reader = csv.reader(price_file)
            next(csv_reader)
            for line in csv_reader:
                self.__AllPrices.append(line)
        return self.__AllPrices
