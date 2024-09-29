from abc import ABC, abstractmethod

from dto.OrderDto import OrderDto


class AbstractCurrencyConverter(ABC):
    @abstractmethod
    def convert(self, order: OrderDto) -> OrderDto:
        pass