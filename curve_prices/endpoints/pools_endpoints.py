from curve_prices.endpoints import EndpointsCore

class PoolsEndpoints(EndpointsCore):

    path = 'v1/pools/'

    def get_pool_metadata(self, chain: str, address: str):
        endpoint = f"{chain}/{address}/metadata"
        return self._execute_request(endpoint)

    def get_pool_data(self, chain: str, address: str):
        endpoint = f"{chain}/{address}"
        return self._execute_request(endpoint)

