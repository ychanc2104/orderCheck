from fastapi import HTTPException

from dto import OrderDto
from utils import get_error
from worker.validation.AbstractValidationStrategy import AbstractValidationStrategy


# 驗證名稱是否是 ASCII 字符
class NameAsciiValidationStrategy(AbstractValidationStrategy):
    def validate(self, order: OrderDto, language: str = "en"):
        if not order.name.isascii():
            raise HTTPException(status_code=400, detail=get_error("order.name.invalid", language))

# 驗證名稱是否符合標題格式
class NameTitleValidationStrategy(AbstractValidationStrategy):
    def validate(self, order: OrderDto, language: str = "en"):
        if not order.name.istitle():
            raise HTTPException(status_code=400, detail=get_error("order.name.title.case.invalid", language))

# 驗證價格是否符合規範
class PriceValidationStrategy(AbstractValidationStrategy):
    def validate(self, order: OrderDto, language: str = "en"):
        if order.price > 2000 or (order.currency == "USD" and order.price * 31 > 2000):
            raise HTTPException(status_code=400, detail=get_error("order.price.over.2000", language))

# 驗證貨幣是否有效
class CurrencyValidationStrategy(AbstractValidationStrategy):
    def validate(self, order: OrderDto, language: str = "en"):
        if order.currency not in ["TWD", "USD"]:
            raise HTTPException(status_code=400, detail=get_error("order.currency.invalid", language))
