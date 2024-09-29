from dto import OrderDto
from worker.OrderCurrencyConverter.AbstractCurrencyConverter import AbstractCurrencyConverter


class NoOpConverter(AbstractCurrencyConverter):
    def convert(self, order: OrderDto) -> OrderDto:
        return order