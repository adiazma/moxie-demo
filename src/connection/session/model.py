from requests import Session, PreparedRequest, Response
import random, time

class RandomSession(Session):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.delay: int = kwargs.get('delay')
        self.rand_max: int = kwargs.get('rand_max')
        self.proxy_url: int = kwargs.get('proxy_url')
        
    def send(self, request: PreparedRequest, **kwargs) -> Response:
        # SEND REQUEST
        kwargs['timeout'] = 360
        time.sleep(self.delay + random.uniform(0, self.rand_max))
        if self.proxy_url:
            kwargs['proxies'] = {
                'http': self.proxy_url,
                'https': self.proxy_url,
            }
        response = super().send(request, **kwargs)
        return response