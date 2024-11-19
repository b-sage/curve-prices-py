from curve_prices.client_core import ClientCore

class TradesClient(ClientCore):

    path = 'trades/'

    def get_trades(
        self, 
        chain: str, 
        address: str, 
        main_token: str,
        reference_token: str,
        page: int=1,
        per_page: int=1000,
        include_state: bool=False
    ):
        endpoint = f"{chain}/{address}" + self._build_query(
            False,
            main_token=main_token,
            reference_token=reference_token,
            page=page,
            per_page=par_page,
            include_state=include_state
        )
        return self._execute_request(endpoint)

