# This gives the class in this file access to the class PriceRepository that is stored in the folder repositories.
from repositories.PriceRepo import PriceRepository

class PriceService:
    def __init__(self):
        '''  '''
        self.__priceRepo = PriceRepository()
    
    def get_LowPrice(self):
        ''' This function pulls the low price list from PriceRepository '''
        low_price_list = self.__priceRepo.get_LowPrice()
        return low_price_list
    
    def get_MediumPrice(self):
        '''  '''
        medium_price_list = self.__priceRepo.get_MediumPrice()
        return medium_price_list
    
    def get_HighPrice(self):
        '''  '''
        high_price_list = self.__priceRepo.get_HighPrice()
        return high_price_list
    
    def get_all_prices(self):
        '''  '''
        all_prices_list = self.__priceRepo.get_all_prices()
        return all_prices_list