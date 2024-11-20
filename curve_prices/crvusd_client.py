from curve_prices.client_core import ClientCore

class CrvUsdClient(ClientCore):

    path = 'crvusd/'
    
    def get_llamma_ohlc(
        self, 
        chain: str, 
        address: str, 
        start: int, 
        end: int, 
        agg_number: int=None, 
        agg_units: int=None
    ):
        endpoint = f"llamma_ohlc/{chain}/{address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

    def get_llamma_trades(self, chain: str, address: str, page: int=1, per_page: int=1000):
        endpoint = f"llamma_trades/{chain}/{address}" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)    

    def get_llammma_events(self, chain: str, address: str, page: int=1, per_page: int=1000):
        endpoint = f"llamma_events/{chain}/{address}" + self._build_query(
            False,
            page=page,
            per_page=per_page
        )
        return self._execute_request(endpoint)

    def get_markets(self, chain: str, fetch_on_chain: bool=False, page: int=1, per_page: int=1000):
        endpoint = f"markets/{chain}" + self._build_query(
            False,
            fetch_on_chain=fetch_on_chain,
            page=page,
            per_page=per_page
        )
        return self._execute_request(endpoint)

    def get_market(self, chain: str, address: str, fetch_on_chain: bool=False, agg: str='day'):
        endpoint = f"markets/{chain}/{address}" + self._build_query(
            False,
            fetch_on_chain=fetch_on_chain,
            agg=agg
        )
        return self._execute_request(endpoint)

    def get_supply(self, chain: str, start: int, end: int):
        endpoint = f"markets/{chain}/supply" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_market_loan_distribution(self, chain: str, controller: str):
        endpoint = f"markets/{chain}/{controller}/loans/distribution"
        return self._execute_request(endpoint)

    def get_market_collateral_events(self, chain: str, controller: str, user: str, pagination: int=1000, page: int=1):
        endpoint = f"collateral_events/{chain}/{controller}/{user}" + self._build_query(
            False,
            pagination=pagination,
            page=page
        )
        return self._execute_request(endpoint)

    def get_pegkeepers(self, chain: str):
        endpoint = f"pegkeepers/{chain}"
        return self._execute_request(endpoint)

    def get_pegkeeper(self, chain: str, address: str, page: int=1, pagination: int=1000):
        endpoint = f"pegkeepers/{chain}/{address}" + self._build_query(
            False,
            page=page,
            pagination=pagination
        )
        return self._execute_request(endpoint)

    def get_user_markets(self, chain: str, user: str, page: int=1, pagination: int=1000):
        endpoint = f"users/{chain}/{user}" + self._build_query(False, page=page, pgaination=pagination)
        return self._execute_request(endpoint)

    def get_user_market_stats(self, chain: str, user: str, controller: str):
        endpoint = f"users/{chain}/{user}/{controller}"
        return self._execute_request(endpoint)

    def get_user_market_snapshot(
        self,
        chain: str,
        user: str,
        controller: str,
        page: int=1,
        per_page: int=1000,
        start: int=None,
        end: int=None
    ):
        endpoint = f"users/{chain}/{user}/{controller}/snapshots" + self._build_query(
            False,
            page=page,
            per_page=per_page,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)

    def get_market_users(self, chain: str, controller: str, page: int=1, per_page: int=1000):
        endpoint = f"users/{chain}/{contoller_address}/users" + self._build_query(
            False,
            page=page,
            per_page=per_page
        )
        return self._execute_request(endpoint)

    def get_user_stats(self, user: str):
        endpoint = f"savings/{user}/stats"
        return self._execute_request(endpoint)

    def get_user_events(self, user: str, page: int=1, per_page: int=1000):
        endpoint = f"savings/{user}/events" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_events(self, page: int=1, per_page: int=1000):
        endpoint = f"savings/events" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_yield(self, start: int, end: int, interval: str='day'):
        endpoint = f"savings/yield" + self._build_query(False, start=start, end=end, interval=interval)
        return self._execute_request(endpoint)

    def get_revenue(self, page: int=1, per_page: int=1000):
        endpoint = f"savings/revenue" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_stats(self):
        endpoint = f"savings/statistics"
        return self._execute_request(endpoint)

    def get_market_soft_liquidation_ratio(self, chain: str, controller: str, start: int=None, end: int=None):
        endpoint = f"liquidations/{chain}/{controller}/soft_liquidation_ratio" + self._build_query(
            False,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)

    def get_market_detailed_liquidation_history(self, chain: str, controller: str, start: int=None, end: int=None):
        endpoint = f"liquidations/{chain}/{controller}/history/detailed" + self._build_query(
            False,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)
    
    def get_market_aggregated_liquidation_history(self, chain: str, controller: str, start: int=None, end: int=None):
        endpoint = f"liquidations/{chain}/{controller}/history/aggregated" + self._build_query(
            False,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)
    
    def get_aggregated_liquidation_history(self, chain: str, start: int=None, end: int=None):
        endpoint = f"liquidations/{chain}/history/aggregated" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_market_liquidation_losses(self, chain: str, controller: str, start: int=None, end: int=None):
        endpoint = f"liquidations/{chain}/{controller}/losses/history" + self._build_query(
            False,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)

    def get_market_health_distribution(self, chain: str, controller: str):
        endpoint = f"liquidations/{chain}/{controller}/health/distribution"
        return self._execute_request(endpoint)

    def get_market_cr_distribution(self, chain: str, controller: str):
        endpoint = f"liquidations/{chain}/{contoller_address}/cr/distribution"
        return self._execute_request(endpoint)

    def get_market_health_overview(self, chain: str, controller: str, fetch_on_chain: bool=False):
        endpoint = f"liquidations/{chain}/{controller}/overview" + self._build_query(False, fetch_on_chain=fetch_on_chain)
        return self._execute_request(endpoint)

    def get_market_losses_per_band_range(self, chain: str, controller: str, start: int=None, end: int=None, statistic: str="mean"):
        endpoint = f"liquidations/{chain}/{controller}/losses_per_band_range" + self._build_query(
            False,
            start=start,
            end=end,
            statistic=statistic
        )
        return self._execute_request(endpoint)

    def get_market_hard_liquidated_users(self, chain: str, controller: str, start: int=None, end: int=None):
        endpoint = f"liquidations/{chain}/{controller}/hard/users" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_market_hard_liquidation_total(self, chain: str, controller: str):
        endpoint = f"liquidations/{chain}/{controller}/hard/total"
        return self._execute_request(endpoint)

