from pydantic import BaseModel

class AddressDto(BaseModel):
    city: str
    district: str
    street: str