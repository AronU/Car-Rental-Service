import datetime
class Order:
    def __init__(self, ID, start_date, end_date):
        self.__ID = ID
        self.__start_date = start_date
        self.__end_date = end_date

    def __str__(self):
        return "{},{},{}".format(self.__ID, self.__start_date,
                                 self.__end_date)

    def __repr__(self):
        return self.__str__()

    def get_ID(self):
        return self.__ID

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

# fannar = Order('1', '2018, 5, 12', '2018,10,12')
# print(fannar)