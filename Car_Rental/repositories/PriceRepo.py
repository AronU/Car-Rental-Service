import csv

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