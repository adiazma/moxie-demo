from abc import ABC, abstractmethod
from models.results_model import Result
from connection.session.model import RandomSession

class BaseProject:

    VERIFY: bool = False

    def __init__(self, **kwargs) -> None:
        self.VERIFY = kwargs.get('proxy', False)
        self._session = RandomSession(delay=0.1, rand_max=0.1)

    @abstractmethod
    def run(self) -> Result:
        raise NotImplementedError