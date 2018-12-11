from services.CustomerService import CustomerService
from services.OrderService import OrderService
from services.CarService import CarService

customer_service = CustomerService()
order_service = OrderService()
car_service = CarService()
licence_plate = "TE 378"
price = car_service.get_car_price(licence_plate)
print(type(price))
print(price)