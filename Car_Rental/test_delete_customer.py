from services.CustomerService import CustomerService
from services.OrderService import OrderService
from services.CarService import CarService

from repositories.OrderRepo import OrderRepository

from datetime import date, datetime

order_repo = OrderRepository()
start = date(2020, 1, 23)
end = date(2020, 1, 28)
unavail_list = order_repo.catch_unavailable_cars(start, end)
print(unavail_list)