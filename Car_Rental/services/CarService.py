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

    def return_car(self, licence_plate):
        '''This function is pulled from the return car UI and goes into the
         repo to switch the car to an available state.-Aron'''
        self.__car_repo.return_car(licence_plate)

    def valid_check_licence_plate(self, licence_plate):
        '''Verifies if the licence plate it is given is real or not. Returns True if real, False if not.'''
        valid_check = self.__car_repo.verify_licence_plate(licence_plate)
        return valid_check
