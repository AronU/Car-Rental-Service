from repositories.OrderRepo import OrderRepository

class OrderService:
    def __init__(self):
        self.__order_repo = OrderRepository()

    def add_order(self, order):
        self.__order_repo.add_order(order)

    def get_random_id(self):
        random_id = self.__order_repo.set_random_id()
        return random_id