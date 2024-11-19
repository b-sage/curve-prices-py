from curve_prices.client_core import ClientCore

class VolumeClient(ClientCore):

    path = 'volume/'

    def get_pool_usd_volume(self, chain: str, address: str, start: int, end: int, interval: str='day'):
        endpoint = f"usd/{chain}/{address}" + self._build_query(
            False,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

    def get_pool_token_volume(
        self, 
        chain: str,
        address: str,
        main_token: str,
        reference_token: str,
        start: int,
        end: int,
        interval: str="day"
    ):
        endpoint = f"{chain}/{address}" + self._build_query(
            False,
            main_token=main_token,
            reference_token=reference_token,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

    def get_chain_usd_volume(self, chain: str, start: int, end: int, interval: str='day'):
        endpoint = f"{chain}/all" + self._build_query(
            False,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)
