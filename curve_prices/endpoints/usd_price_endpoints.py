from curve_prices.endpoints import EndpointsCore

class UsdPriceEndpoints(EndpointsCore):

    path = 'v1/usd_price/'

    def get_usd_prices(self, chain: str):
        endpoint = f"{chain}"
        return self._execute_request(endpoint)

    def get_usd_price(self, chain: str, address: str):
        endpoint = f"{chain}/{address}"
        return self._execute_request(endpoint)

    def get_usd_price_history(self, chain: str, address: str, start: int, end: int, interval: str='day'):
        endpoint = f"{chain}/{address}/history" + self._build_query(
            False,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

