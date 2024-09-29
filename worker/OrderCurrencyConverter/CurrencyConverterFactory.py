from worker.OrderCurrencyConverter.AbstractCurrencyConverter import AbstractCurrencyConverter
from worker.OrderCurrencyConverter.NoOpConverter import NoOpConverter
from worker.OrderCurrencyConverter.UsdToTwdConverter import USDToTWDConverter


class CurrencyConverterFactory:

    @staticmethod
    def get_converter(currency: str) -> AbstractCurrencyConverter:
        if currency == "USD":
            return USDToTWDConverter()
        else:
            return NoOpConverter()
