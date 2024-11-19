import requests

class CurvePricesClient:

    def __init__(
        self,
        base_url: str="https://prices.curve.fi/v1/"
    ):
        self.base_url = base_url
        self.session = requests.Session()

    def _execute_request(self, endpoint):
        res = self.session.get(self.base_url + endpoint)
        assert res.status_code == 200, "Bad status code: {res.status_code}"
        return res.json()

    def _build_query(self, has_query: bool, **kwargs):
        if all(not v for v in kwargs.values()):
            return ''
        start = '&' if has_query else '?'
        return start + '&'.join([f"{k}={v}" for k, v in kwargs.items() if v is not None])

    def chains(self):
        endpoint = 'chains/'
        return self._execute_request(endpoint)

    def chain(self, chain_name: str, per_page: int=1000, page: int=1):
        endpoint = f"chains/{chain_name}" + self._build_query(False, per_page=per_page, page=page)
        return self._execute_request(endpoint)

    def transaction_activity(self, start: int=None, end: int=None):
        endpoint = f"chains/activity/transactions" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def user_activity(self, start: int=None, end: int=None):
        endpoint = f"chains/activity/users" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def lending_chains(self):
        endpoint = f"lending/chains/"
        return self._execute_request(endpoint)

    def pool_metadata(self, chain: str, pool_address: str):
        endpoint = f"pools/{chain}/{pool_address}/metadata"
        return self._execute_request(endpoint)

    def pool_data(self, chain: str, pool_address: str):
        endpoint = f"pools/{chain}/{pool_address}"
        return self._execute_request(endpoint)

    def ohlc(
        self, 
        chain: str, 
        pool_address: str, 
        main_token: str, 
        reference_token: str, 
        start: int, 
        end: int, 
        agg_number: int=None, 
        agg_units: str=None
    ):
        endpoint = f"ohlc/{chain}/{pool_address}" + self._build_query(
                False, 
                main_token=main_token, 
                reference_token=reference_token, 
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

    def lp_ohlc(
        self,
        chain: str,
        pool_address: str,
        start: int,
        end: int,
        agg_number: int=None,
        agg_units: str=None,
        price_units: str='usd'
    ):
        endpoint = f"lp_ohlc/{chain}/{pool_address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units,
                price_units=price_units
        )
        return self._execute_request(endpoint)

    def llamma_ohlc_crvusd(self, chain: str, pool_address: str, start: int, end: int, agg_number: int=None, agg_units: int=None):
        endpoint = f"crvusd/llamma_ohlc/{chain}/{pool_address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)


