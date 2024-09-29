import abc
import time
from typing import TypeVar, Generic

from fastapi import HTTPException
from pydantic_core import ValidationError

from base.ResponseDto import ResponseDto

RequestInput = TypeVar('RequestInput')
ResponseOutput = TypeVar('ResponseOutput')

class BaseService(Generic[RequestInput, ResponseOutput]):
    def request(self, input: RequestInput):
        try:
            return self.generate_response(data=self.process_data(input), time_start=time.time())
        except HTTPException as e:
            return self.generate_response(data=None, errorMessage=e.detail, time_start=time.time())
        except ValidationError as e:
            return self.generate_response(data=None, errorMessage=str(e), time_start=time.time())

    @abc.abstractmethod
    def process_data(self, input: RequestInput) -> ResponseOutput:
        return NotImplemented

    def generate_response(self, data: ResponseDto | None, time_start: float, errorMessage: str | None=None) -> ResponseDto:
        time_end = time.time()
        return ResponseDto(
            success=True if errorMessage is None else False,
            data=data,
            responseTime=f"{((time_end - time_start) * 1000):.0f} ms",
            errorMessage=errorMessage
        )
