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