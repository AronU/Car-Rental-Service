from repositories.OrderRepo import OrderRepository

class OrderService:
    def __init__(self):
        self.__order_repo = OrderRepository()

    def add_order(self, order):
        self.__order_repo.add_order(order)

    def get_random_id(self):
        random_id = self.__order_repo.set_random_id()
        return random_id

    def get_order_ssn(self, ssn):
        order_list_ssn = self.__order_repo.get_order_ssn(ssn)
        return order_list_ssn