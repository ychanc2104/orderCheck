from dto import OrderDto
from worker.OrderCurrencyConverter.AbstractCurrencyConverter import AbstractCurrencyConverter


class USDToTWDConverter(AbstractCurrencyConverter):
    def convert(self, order: OrderDto) -> OrderDto:
        if order.currency == "USD":
            order.price = order.price * 31
            order.currency = "TWD"
        return order