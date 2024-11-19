from curve_prices.client_core import ClientCore

class OhlcClient(ClientCore):

    path = 'ohlc/'

    def get_ohlc(
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
        endpoint = f"{chain}/{address}" + self._build_query(
                False, 
                main_token=main_token, 
                reference_token=reference_token, 
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

