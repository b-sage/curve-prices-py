from curve_prices.client_core import ClientCore

class DaoClient(ClientCore):

    path = 'v1/dao/'

    def get_gauges_overview(self):
        endpoint = f"gauges/overview"
        return self._execute_request(endpoint)

    def get_votes_overview(self):
        endpoint = f"votes/overview"
        return self._execute_request(endpoint)

    def get_user_gauge_votes(self, user: str):
        endpoint = f"gauges/votes/user/{user}"
        return self._execute_request(endpoint)

    def get_user_proposal_votes(self, user: str, pagination: int=1000, page: int=1):
        endpoint = f"proposals/votes/user/{user}" + self._build_query(False, pagination=pagination, page=page)
        return self._execute_request(endpoint)

    def get_gauge_for_pool(self, chain: str, pool: str):
        endpoint = f"pools/{chain}/{pool}/gauge"
        return self._execute_request(endpoint)

    def get_gauge_for_market(self, chain: str, controller: str):
        endpoint = f"lending/{chain}/{controller}/gauge"
        return self._execute_request(endpoint)

    def get_votes_for_gauge(self, gauge: str):
        endpoint = f"gauges/{gauge}/votes"
        return self._execute_request(endpoint)

    def get_gauge_metadata(self, gauge: str):
        endpoint = f"gauges/{gauge}/metadata"
        return self._execute_request(endpoint)

    def get_gauge_weight_history(self, gauge: str):
        endpoint = f"gauges/{gauge}/weight_history"
        return self._execute_request(endpoint)

    def get_gauge_deployment(self, gauge: str):
        endpoint = f"gauges/{gauge}/deployment"
        return self._execute_request(endpoint)

    def get_user_crv_locks(self, user: str):
        endpoint = f"locks/{user}"
        return self._execute_request(endpoint)

    def get_daily_crv_lock_history(self, days_back: int):
        endpoint = f"locks/daily/{days_back}"
        return self._execute_request(endpoint)

    def get_crv_supply_breakdown(self, days_back: int):
        endpoint = f"supply/{days_back}"
        return self._execute_request(endpoint)

    def get_largest_lockers(self, pagination: int=1000, page: int=1):
        endpoint = f"lockers" + self._build_query(False, pagination=pagination, page=page)
        return self._execute_request(endpoint)

    def get_proposals(self, search_string: str=None, pagination: int=1000, page: int=1, status_filter:str='all', type_filter: str='all'):
        endpoint = f"proposals" + self._build_query(
            False,
            search_string=search_string,
            pagination=pagination,
            page=page,
            status_filter=status_filter,
            type_filter=type_filter
        )
        return self._execute_request(endpoint)

    def get_proposal(self, type_: str, vote_id: int):
        endpoint = f"proposals/details/{type}/{vote_id}"
        return self._execute_request(endpoint)

    def get_fee_distributions(self, page: int=1, per_page: int=1000):
        endpoint = f"fees/distributions" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_weekly_crvusd_fees(self, start: int=None, end: int=None):
        endpoint = f"fees/crvusd/weekly" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_weekly_pool_fees(self, start: int=None, end: int=None):
        endpoint = f"fees/pools/weekly" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_pending_pool_fees(self, chain: str):
        endpoint = f"fees/{chain}/pending"
        return self._execute_request(endpoint)

    def get_fee_settlements(self, prior_to: int):
        endpoint = f"fees/settlements" + self._build_query(False, timestamp=prior_to)
        return self._execute_request(endpoint)

    def get_collected_fees(self):
        endpoint = f"fees/collected"
        return self._execute_request(endpoint)

    def get_staged_fees(self):
        endpoint = f"fees/staged"
        return self._execute_request(endpoint)

