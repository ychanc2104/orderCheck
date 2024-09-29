import pytest

from dto import OrderDto
from dto.AddressDto import AddressDto
from services.CreateOrderService import CreateOrderService


@pytest.fixture
def address_input():
    return AddressDto(city="taipei", district="da an", street="fuxing-south-road")


@pytest.fixture
def order_input(address_input):
    return OrderDto(id="A0000001", name="Hotel Inn", price=1000, currency="TWD", address=address_input)


@pytest.mark.parametrize("name, price, currency, expected_error, expected_price", [
    ("Hotel Inn", 1000, "TWD", None, 1000),  # Valid input
    ("Hotel inn 飯店", 1000, "TWD", "Name contains non-English characters", 1000),  # Invalid: Non-English characters
    ("Hotel inn", 1000, "TWD", "Name is not capitalized", 1000),  # Invalid: Name not capitalized
    ("Hotel Inn", 2001, "TWD", "Price is over 2000", 1000),  # Invalid: Price is over 2000
    ("Hotel Inn", 1000, "CNY", "Currency format is wrong", 1000),  # Invalid: Currency format is wrong
    ("Hotel Inn", 10, "USD", None, 10*31),  # Valid input: transform USD to TWD
    ("Hotel Inn", 500, "USD", "Price is over 2000", 500*31),  # Invalid: Price is over 2000

])
def test_create_order_name(order_input, name, price, currency, expected_error, expected_price):
    service = CreateOrderService()

    order_input.name = name
    order_input.price = price
    order_input.currency = currency

    response = service.request(order_input)

    assert response.errorMessage == expected_error
    if response.errorMessage is None:
        assert response.data.price == expected_price
        assert response.data.currency == "TWD"


if __name__ == "__main__":
    pytest.main()