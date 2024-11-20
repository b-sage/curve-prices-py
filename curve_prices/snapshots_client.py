from curve_prices.client_core import ClientCore

class SnapshotsClient(ClientCore):

    path = 'v1/snapshots/'

    def get_pool_snapshot(self, chain: str, address: str, start: int, end: int):
        endpoint = f"{chain}/{address}" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_pool_tvl_snapshot(self, chain: str, address: str, start: int, end: int, unit: str='day'):
        endpoint = f"{chain}/{address}/tvl" + self._build_query(False, start=start, end=end, unit=unit)
        return self._execute_request(endpoint)

