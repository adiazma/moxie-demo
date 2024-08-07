from abc import ABC

class BaseConnection(ABC):

    def __init__(self, **kwargs) -> None:
        pass

    def connect(self, **kwargs) -> any:
        ...

    def read(self, **kwargs) -> any:
        ...
    
    def write(self, **kwargs) -> any:
        ...