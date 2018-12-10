# This gives the class in this file access to the class PriceRepository that is stored in the folder repositories.
from repositories.PriceRepo import PriceRepository

class PriceService:
    def __init__(self):
        ''' This function renames the class PriceRepository. '''
        self.__priceRepo = PriceRepository()
    
    def get_LowPrice(self):
        ''' This function pulls the low price list from PriceRepository and returns it. '''
        low_price_list = self.__priceRepo.get_LowPrice()
        return low_price_list
    
    def get_MediumPrice(self):
        ''' This function pulls the medium price list from PriceRepository and returns it. '''
        medium_price_list = self.__priceRepo.get_MediumPrice()
        return medium_price_list
    
    def get_HighPrice(self):
        ''' This function pulls the high price list from PriceRepository and returns it. '''
        high_price_list = self.__priceRepo.get_HighPrice()
        return high_price_list
    
    def get_all_prices(self):
        ''' This function pulls the all prices list from PriceRepository and returns it. '''
        all_prices_list = self.__priceRepo.get_all_prices()
        return all_prices_list