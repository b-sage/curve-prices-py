import requests

class ClientCore:

    def __init__(self, base_url: str='https://prices.curve.fi/v1/'):
        self.base_url = base_url + self.path
        self.session = requests.Session()
    
    def _execute_request(self, endpoint):
        res = self.session.get(self.base_url + endpoint)
        assert res.status_code == 200, f"Bad status code: {res.status_code}"
        return res.json()

    def _build_query(self, has_query: bool, **kwargs):
        if all(not v for v in kwargs.values()):
            return ''
        start = '&' if has_query else '?'
        return start + '&'.join([f"{k}={v}" for k, v in kwargs.items() if v is not None])

