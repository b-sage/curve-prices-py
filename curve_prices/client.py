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

    def chain(self, chain: str, per_page: int=1000, page: int=1):
        endpoint = f"chains/{chain}" + self._build_query(False, per_page=per_page, page=page)
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

    def pool_metadata(self, chain: str, address: str):
        endpoint = f"pools/{chain}/{address}/metadata"
        return self._execute_request(endpoint)

    def pool_data(self, chain: str, address: str):
        endpoint = f"pools/{chain}/{address}"
        return self._execute_request(endpoint)

    def ohlc(
        self, 
        chain: str, 
        address: str, 
        main_token: str, 
        reference_token: str, 
        start: int, 
        end: int, 
        agg_number: int=None, 
        agg_units: str=None
    ):
        endpoint = f"ohlc/{chain}/{address}" + self._build_query(
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
        address: str,
        start: int,
        end: int,
        agg_number: int=None,
        agg_units: str=None,
        price_units: str='usd'
    ):
        endpoint = f"lp_ohlc/{chain}/{address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units,
                price_units=price_units
        )
        return self._execute_request(endpoint)

    def llamma_ohlc_crvusd(
        self, 
        chain: str, 
        address: str, 
        start: int, 
        end: int, 
        agg_number: int=None, 
        agg_units: int=None
    ):
        endpoint = f"crvusd/llamma_ohlc/{chain}/{address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

    def llamma_ohlc_lending(
        self, 
        chain: str,
        address: str,
        start: int,
        end: int,
        agg_number: int=None,
        agg_units: str=None
    ):
        endpoint = f"lending/llamma_ohlc/{chain}/{address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

    def oracle_ohlc(
        self,
        chain: str,
        controller_address: str,
        start: int,
        end: int,
        agg_number: int=None,
        agg_units: str=None
    ):
        endpoint = f"lending/oracle_ohlc/{chain}/{controller_address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

    def trades(
        self, 
        chain: str, 
        address: str, 
        main_token: str,
        reference_token: str,
        page: int=1,
        per_page: int=1000,
        include_state: bool=False
    ):
        endpoint = f"trades/{chain}/{address}" + self._build_query(
            False,
            main_token=main_token,
            reference_token=reference_token,
            page=page,
            per_page=par_page,
            include_state=include_state
        )
        return self._execute_request(endpoint)

    def llamma_trades(self, chain: str, address: str, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/llamma_trades/{chain}/{address}" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def usd_prices(self, chain: str):
        endpoint = f"usd_price/{chain}"
        return self._execute_request(endpoint)

    def usd_price(self, chain: str, address: str):
        endpoint = f"usd_price/{chain}/{address}"
        return self._execute_request(endpoint)

    def usd_price_history(self, chain: str, address: str, start: int, end: int, interval: str='day'):
        endpoint = f"usd_price/{chain}/{address}/history" + self._build_query(
            False,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

    def liquidity(self, chain: str, address: str, page: int=1, per_page: int=1000, include_state: bool=False):
        endpoint = f"liquidity/{chain}/{address}" + self._build_query(
            False,
            page=page,
            per_page=per_page,
            include_state=include_state
        )
        return self._execute_request(endpoint)

    def llammma_liquidity(self, chain: str, address: str, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/llamma_events/{chain}/{address}" + self._build_query(
            False,
            page=page,
            per_page=per_page
        )
        return self._execute_request(endpoint)

    def pool_usd_volume(self, chain: str, address: str, start: int, end: int, interval: str='day'):
        endpoint = f"volume/usd/{chain}/{address}" + self._build_query(
            False,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

    def pool_token_volume(
        self, 
        chain: str,
        address: str,
        main_token: str,
        reference_token: str,
        start: int,
        end: int,
        interval: str="day"
    ):
        endpoint = f"volume/{chain}/{address}" + self._build_query(
            False,
            main_token=main_token,
            reference_token=reference_token,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

    def chain_usd_volume(self, chain: str, start: int, end: int, interval: str='day'):
        endpoint = f"volume/{chain}/all" + self._build_query(
            False,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

    def pool_snapshot(self, chain: str, address: str, start: int, end: int):
        endpoint = f"snapshots/{chain}/{address}" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def pool_tvl_snapshot(self, chain: str, address: str, start: int, end: int, unit: str='day'):
        endpoint = f"snapshots/{chain}/{address}/tvl" + self._build_query(False, start=start, end=end, unit=unit)
        return self._execute_request(endpoint)

    def crvusd_markets(self, chain: str, fetch_on_chain: bool=False, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/markets/{chain}" + self._build_query(
            False,
            fetch_on_chain=fetch_on_chain,
            page=page,
            per_page=per_page
        )
        return self._execute_request(endpoint)

    def crvusd_market_snapshot(self, chain: str, address: str, fetch_on_chain: bool=False, agg: str='day'):
        endpoint = f"crvusd/markets/{chain}/{address}" + self._build_query(
            False,
            fetch_on_chain=fetch_on_chain,
            agg=agg
        )
        return self._execute_request(endpoint)

    def crvusd_market_supply(self, chain: str, start: int, end: int):
        endpoint = f"crvusd/markets/{chain}/supply" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def crvusd_loan_distribution(self, chain: str, controller_address: str):
        endpoint = f"crvusd/markets/{chain}/{controller_address}/loans/distribution"
        return self._execute_request(endpoint)

    def crvusd_collateral_events(self, chain: str, controller_address: str, user: str, pagination: int=1000, page: int=1):
        endpoint = f"crvusd/collateral_events/{chain}/{controller_address}/{user}" + self._build_query(
            False,
            pagination=pagination,
            page=page
        )
        return self._execute_request(endpoint)

    def pegkeepers(self, chain: str):
        endpoint = f"crvusd/pegkeepers/{chain}"
        return self._execute_request(endpoint)

    def pegkeeper(self, chain: str, address: str, page: int=1, pagination: int=1000):
        endpoint = f"crvusd/pegkeepers/{chain}/{address}" + self._build_query(
            False,
            page=page,
            pagination=pagination
        )
        return self._execute_request(endpoint)

    def llamma_events(self, chain: str, address: str, page: int=1, pagination: int=1000):
        endpoint = f"crvusd/llamma_events/{chain}/{address}" + self._build_query(False, page=page, pagination=pagination)
        return self._execute_request(endpoint)





