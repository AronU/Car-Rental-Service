from services.CustomerService import CustomerService
from services.OrderService import OrderService
from services.CarService import CarService

customer_service = CustomerService()
order_service = OrderService()
car_service = CarService()
kennitala = "0905953189"
history_list = customer_service.user_history(kennitala)
print(history_list)