from enum import Enum
from typing import Optional

class ResultType(Enum):
    SUCCESS = 'success'
    FAILURE = 'failure'

class Result:
    def __init__(self,
            status: ResultType = None,
            message: str = None) -> None:
        
        self._status: ResultType = status
        self._message: str = message
    
    @property
    def status(self) -> Optional[ResultType]:
        return self._status

    @status.setter
    def status(self, status: ResultType) -> None:
        self._status = status

    @property
    def message(self) -> Optional[str]:
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        self._message = message