from services.CustomerService import CustomerService
from services.OrderService import OrderService

customer_service = CustomerService()
order_service = OrderService()


random_id = order_service.get_random_id()
print(random_id)
