from dto.OrderDto import OrderDto
from worker.validation import AbstractValidationStrategy


class OrderValidateWorker:
    def __init__(self, strategies: list[AbstractValidationStrategy]):
        self.strategies = strategies

    def validate(self, order: OrderDto, language: str = "en"):
        for strategy in self.strategies:
            strategy.validate(order, language)
