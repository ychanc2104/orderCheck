from abc import ABC, abstractmethod
from dto.OrderDto import OrderDto


class AbstractValidationStrategy(ABC):
    @abstractmethod
    def validate(self, order: OrderDto, language: str):
        pass
