from base import BaseService
from dto.OrderDto import OrderDto
from worker.OrderCurrencyConverter.CurrencyConverterFactory import CurrencyConverterFactory
from worker.OrderTransformWorker import OrderTransformWorker
from worker.OrderValidateWorker import OrderValidateWorker
from worker.validation import NameAsciiValidationStrategy, NameTitleValidationStrategy, PriceValidationStrategy, \
    CurrencyValidationStrategy


class CreateOrderService(BaseService[OrderDto, OrderDto]):
    strategies = [
        NameAsciiValidationStrategy(),
        NameTitleValidationStrategy(),
        PriceValidationStrategy(),
        CurrencyValidationStrategy()
    ]

    def process_data(self, input: OrderDto):
        OrderValidateWorker(self.strategies).validate(input) # Strategy Pattern

        currency_converter = CurrencyConverterFactory.get_converter(input.currency)
        transformer = OrderTransformWorker(currency_converter) # DIP

        return transformer.transform_order(input)
