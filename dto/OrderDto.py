from pydantic import BaseModel

from dto.AddressDto import AddressDto


class OrderDto(BaseModel):
    id: str
    name: str
    address: AddressDto
    price: int
    currency: str
