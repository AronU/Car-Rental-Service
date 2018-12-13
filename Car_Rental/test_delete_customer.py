from services.CustomerService import CustomerService
from services.OrderService import OrderService
from services.CarService import CarService

from repositories.OrderRepo import OrderRepository
from repositories.CarRepo import CarRepository

from datetime import date, datetime

order_repo = OrderRepository()
car_repo = CarRepository()
order_service = OrderService()
car_service = CarService()
start = date(2019, 1, 23)
end = date(2019, 1, 28)

car_histroy_list = car_repo.car_history("SJ 234")
print(car_histroy_list)



