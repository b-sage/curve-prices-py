from curve_prices.client_core import ClientCore

class ChainsClient(ClientCore):

    path = 'v1/chains/'

    def get_chains(self):
        endpoint = ''
        return self._execute_request(endpoint)

    def get_chain(self, chain: str, per_page: int=1000, page: int=1):
        endpoint = f"{chain}" + self._build_query(False, per_page=per_page, page=page)
        return self._execute_request(endpoint)

    def get_transaction_activity(self, start: int=None, end: int=None):
        endpoint = f"activity/transactions" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_user_activity(self, start: int=None, end: int=None):
        endpoint = f"activity/users" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

