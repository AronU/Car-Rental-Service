from services.CustomerService import CustomerService
from services.OrderService import OrderService
from services.CarService import CarService

from repositories.OrderRepo import OrderRepository

from datetime import date, datetime

order_repo = OrderRepository()
order_service = OrderService()
car_service = CarService()
start = date(2019, 1, 23)
end = date(2019, 1, 28)

available_cars = car_service.get_available_cars()
print(available_cars)
print(car_service.check_if_car_is_rented("HK 468"))




