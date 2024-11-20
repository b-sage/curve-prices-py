from curve_prices.client_core import ClientCore

class LpOhlcClient(ClientCore):

    path = 'v1/lp_ohlc/'

    def get_lp_ohlc(
        self,
        chain: str,
        address: str,
        start: int,
        end: int,
        agg_number: int=None,
        agg_units: str=None,
        price_units: str='usd'
    ):
        endpoint = f"{chain}/{address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units,
                price_units=price_units
        )
        return self._execute_request(endpoint)

