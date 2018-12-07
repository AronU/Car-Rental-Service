from repositories.OrderRepo import OrderRepository
from models.Order import Order


order = Order(50, "LK 500", 2904972649, "29/04/1997", "30/04/1997")
order_repo = OrderRepository()

order_repo.add_order(order)
all_ids = order_repo.get_all_ids()
print(order_repo.set_random_id())