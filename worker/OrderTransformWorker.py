from dto import OrderDto
from worker.OrderCurrencyConverter.AbstractCurrencyConverter import AbstractCurrencyConverter


class OrderTransformWorker:
    def __init__(self, currency_converter: AbstractCurrencyConverter):
        self.currency_converter = currency_converter

    def transform_order(self, order: OrderDto) -> OrderDto:
        order = self.transform_currency(order)
        # TODO: other transform logic

        return order

    def transform_currency(self, order: OrderDto) -> OrderDto:
        return self.currency_converter.convert(order)