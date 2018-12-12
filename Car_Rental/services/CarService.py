from repositories.CarRepo import CarRepository

class CarService:
    def __init__(self):
        self.__car_repo = CarRepository()

    def get_available_cars(self):
        '''This function is pulled from the UI and is supposed to 
           go into the Car Repository and get the available car list 
           from there. - Aron 05/12'''
        available_car_list = self.__car_repo.get_available_cars()
        return available_car_list

    def get_unavailable_cars(self):
        '''This function is pulled from the UI and is supposed to 
       go into the Car Repository and get the unavailable car list 
       from there. - Aron 05/12'''
        unavailable_car_list = self.__car_repo.get_unavailable_cars()
        return unavailable_car_list

    def get_all_cars(self):
        '''This function is pulled from the UI and is suppposed to go
        into the car repository and get all car list from there - Fannar 12/12'''
        all_car_list = self.__car_repo.get_all_cars()
        return all_car_list

    def get_licence_plate(self, license_plate):
        '''This function is pulled from the UI and is supposed to go
        into the car repository and get the car with matching licence
        plate - Fannar 12/12'''
        car_licence_plate = self.__car_repo.get_car_licence_plate(licence_plate)
        return car_licence_plate

    def return_car(self, licence_plate):
        '''This function is pulled from the return car UI and goes into the
         repo to switch the car to an available state.-Aron'''
        self.__car_repo.return_car(licence_plate)

    def valid_check_licence_plate(self, licence_plate):
        '''Verifies if the licence plate it is given is real or not. Returns True if real, False if not.'''
        return self.__car_repo.verify_licence_plate(licence_plate)
    
    def get_car_price(self, licence_plate):
        '''Is called by UI layer to get a price of a specific car. Goes 
        into car repository layer for this info. - Aron'''
        return self.__car_repo.car_price(licence_plate)
