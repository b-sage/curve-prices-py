from curve_prices.endpoints import EndpointsCore

class LiquidityEndpoints(EndpointsCore):

    path = 'v1/liquidity/'

    def get_liquidity(self, chain: str, address: str, page: int=1, per_page: int=1000, include_state: bool=False):
        endpoint = f"{chain}/{address}" + self._build_query(
            False,
            page=page,
            per_page=per_page,
            include_state=include_state
        )
        return self._execute_request(endpoint)
    
