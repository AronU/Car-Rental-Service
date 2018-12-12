from services.CustomerService import CustomerService
from services.OrderService import OrderService
from services.CarService import CarService

from repositories.OrderRepo import OrderRepository

from datetime import date, datetime

order_repo = OrderRepository()
order_service = OrderService()
start = date(2019, 1, 23)
end = date(2019, 1, 28)

available_cars = order_service.available_cars(start, end)
print(available_cars)




