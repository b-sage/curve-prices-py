from curve_prices.client_core import ClientCore

class PoolsClient(ClientCore):

    path = 'pools/'

    def get_pool_metadata(self, chain: str, address: str):
        endpoint = f"{chain}/{address}/metadata"
        return self._execute_request(endpoint)

    def get_pool_data(self, chain: str, address: str):
        endpoint = f"{chain}/{address}"
        return self._execute_request(endpoint)

