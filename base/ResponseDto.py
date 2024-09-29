from pydantic import BaseModel
from typing import TypeVar, Generic, List

T = TypeVar('T')

class ResponseDto(BaseModel):
    success: bool
    data: T|None = None
    responseTime: str
    errorMessage: str|None = None
