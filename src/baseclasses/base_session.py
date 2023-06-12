from requests import Session
import os


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self,method, url, *args, **kwargs):
        return super().request(method, url=f'{self.base_url}{url}', **kwargs)


def api_session():
    return BaseSession(base_url=os.getenv('API_SERVICE_URL'))
