import requests

class CurvePricesClient:

    def __init__(
        self,
        base_url: str="https://prices.curve.fi/v1/"
    ):
        self.base_url = base_url
        self.session = requests.Session()

    def _execute_request(self, endpoint):
        res = self.session.get(self.base_url + endpoint)
        assert res.status_code == 200, "Bad status code: {res.status_code}"
        return res.json()

    def _build_query(self, has_query: bool, **kwargs):
        if all(not v for v in kwargs.values()):
            return ''
        start = '&' if has_query else '?'
        return start + '&'.join([f"{k}={v}" for k, v in kwargs.items() if v is not None])

    def get_chains(self):
        endpoint = 'chains/'
        return self._execute_request(endpoint)

    def get_chain(self, chain: str, per_page: int=1000, page: int=1):
        endpoint = f"chains/{chain}" + self._build_query(False, per_page=per_page, page=page)
        return self._execute_request(endpoint)

    def get_transaction_activity(self, start: int=None, end: int=None):
        endpoint = f"chains/activity/transactions" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_user_activity(self, start: int=None, end: int=None):
        endpoint = f"chains/activity/users" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_lending_chains(self):
        endpoint = f"lending/chains/"
        return self._execute_request(endpoint)

    def get_pool_metadata(self, chain: str, address: str):
        endpoint = f"pools/{chain}/{address}/metadata"
        return self._execute_request(endpoint)

    def get_pool_data(self, chain: str, address: str):
        endpoint = f"pools/{chain}/{address}"
        return self._execute_request(endpoint)

    def get_ohlc(
        self, 
        chain: str, 
        address: str, 
        main_token: str, 
        reference_token: str, 
        start: int, 
        end: int, 
        agg_number: int=None, 
        agg_units: str=None
    ):
        endpoint = f"ohlc/{chain}/{address}" + self._build_query(
                False, 
                main_token=main_token, 
                reference_token=reference_token, 
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

    def get_lp_ohlc(
        self,
        chain: str,
        address: str,
        start: int,
        end: int,
        agg_number: int=None,
        agg_units: str=None,
        price_units: str='usd'
    ):
        endpoint = f"lp_ohlc/{chain}/{address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units,
                price_units=price_units
        )
        return self._execute_request(endpoint)

    def get_llamma_ohlc_crvusd(
        self, 
        chain: str, 
        address: str, 
        start: int, 
        end: int, 
        agg_number: int=None, 
        agg_units: int=None
    ):
        endpoint = f"crvusd/llamma_ohlc/{chain}/{address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

    def get_llamma_ohlc_lending(
        self, 
        chain: str,
        address: str,
        start: int,
        end: int,
        agg_number: int=None,
        agg_units: str=None
    ):
        endpoint = f"lending/llamma_ohlc/{chain}/{address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

    def get_oracle_ohlc(
        self,
        chain: str,
        controller_address: str,
        start: int,
        end: int,
        agg_number: int=None,
        agg_units: str=None
    ):
        endpoint = f"lending/oracle_ohlc/{chain}/{controller_address}" + self._build_query(
                False,
                start=start,
                end=end,
                agg_number=agg_number,
                agg_units=agg_units
        )
        return self._execute_request(endpoint)

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
        endpoint = f"trades/{chain}/{address}" + self._build_query(
            False,
            main_token=main_token,
            reference_token=reference_token,
            page=page,
            per_page=par_page,
            include_state=include_state
        )
        return self._execute_request(endpoint)

    def get_llamma_trades(self, chain: str, address: str, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/llamma_trades/{chain}/{address}" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_usd_prices(self, chain: str):
        endpoint = f"usd_price/{chain}"
        return self._execute_request(endpoint)

    def get_usd_price(self, chain: str, address: str):
        endpoint = f"usd_price/{chain}/{address}"
        return self._execute_request(endpoint)

    def get_usd_price_history(self, chain: str, address: str, start: int, end: int, interval: str='day'):
        endpoint = f"usd_price/{chain}/{address}/history" + self._build_query(
            False,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

    def get_liquidity(self, chain: str, address: str, page: int=1, per_page: int=1000, include_state: bool=False):
        endpoint = f"liquidity/{chain}/{address}" + self._build_query(
            False,
            page=page,
            per_page=per_page,
            include_state=include_state
        )
        return self._execute_request(endpoint)

    def get_llammma_liquidity(self, chain: str, address: str, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/llamma_events/{chain}/{address}" + self._build_query(
            False,
            page=page,
            per_page=per_page
        )
        return self._execute_request(endpoint)

    def get_pool_usd_volume(self, chain: str, address: str, start: int, end: int, interval: str='day'):
        endpoint = f"volume/usd/{chain}/{address}" + self._build_query(
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
        endpoint = f"volume/{chain}/{address}" + self._build_query(
            False,
            main_token=main_token,
            reference_token=reference_token,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

    def get_chain_usd_volume(self, chain: str, start: int, end: int, interval: str='day'):
        endpoint = f"volume/{chain}/all" + self._build_query(
            False,
            start=start,
            end=end,
            interval=interval
        )
        return self._execute_request(endpoint)

    def get_pool_snapshot(self, chain: str, address: str, start: int, end: int):
        endpoint = f"snapshots/{chain}/{address}" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_pool_tvl_snapshot(self, chain: str, address: str, start: int, end: int, unit: str='day'):
        endpoint = f"snapshots/{chain}/{address}/tvl" + self._build_query(False, start=start, end=end, unit=unit)
        return self._execute_request(endpoint)

    def get_crvusd_markets(self, chain: str, fetch_on_chain: bool=False, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/markets/{chain}" + self._build_query(
            False,
            fetch_on_chain=fetch_on_chain,
            page=page,
            per_page=per_page
        )
        return self._execute_request(endpoint)

    def get_crvusd_market_snapshot(self, chain: str, address: str, fetch_on_chain: bool=False, agg: str='day'):
        endpoint = f"crvusd/markets/{chain}/{address}" + self._build_query(
            False,
            fetch_on_chain=fetch_on_chain,
            agg=agg
        )
        return self._execute_request(endpoint)

    def get_crvusd_market_supply(self, chain: str, start: int, end: int):
        endpoint = f"crvusd/markets/{chain}/supply" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_crvusd_loan_distribution(self, chain: str, controller_address: str):
        endpoint = f"crvusd/markets/{chain}/{controller_address}/loans/distribution"
        return self._execute_request(endpoint)

    def get_crvusd_collateral_events(self, chain: str, controller_address: str, user: str, pagination: int=1000, page: int=1):
        endpoint = f"crvusd/collateral_events/{chain}/{controller_address}/{user}" + self._build_query(
            False,
            pagination=pagination,
            page=page
        )
        return self._execute_request(endpoint)

    def get_pegkeepers(self, chain: str):
        endpoint = f"crvusd/pegkeepers/{chain}"
        return self._execute_request(endpoint)

    def get_pegkeeper(self, chain: str, address: str, page: int=1, pagination: int=1000):
        endpoint = f"crvusd/pegkeepers/{chain}/{address}" + self._build_query(
            False,
            page=page,
            pagination=pagination
        )
        return self._execute_request(endpoint)

    def get_llamma_events(self, chain: str, address: str, page: int=1, pagination: int=1000):
        endpoint = f"crvusd/llamma_events/{chain}/{address}" + self._build_query(False, page=page, pagination=pagination)
        return self._execute_request(endpoint)

    def get_crvusd_user_markets(self, chain: str, user: str, page: int=1, pagination: int=1000):
        endpoint = f"crvusd/users/{chain}/{user}" + self._build_query(False, page=page, pgaination=pagination)
        return self._execute_request(endpoint)

    def get_crvusd_user_metrics(self, chain: str, user: str, controller_address: str):
        endpoint = f"crvusd/users/{chain}/{user}/{controller_address}"
        return self._execute_request(endpoint)

    def get_crvusd_user_snapshot(
        self,
        chain: str,
        user: str,
        controller_address: str,
        page: int=1,
        per_page: int=1000,
        start: int=None,
        end: int=None
    ):
        endpoint = f"crvusd/users/{chain}/{user}/{controller_address}/snapshots" + self._build_query(
            False,
            page=page,
            per_page=per_page,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)

    def get_crvusd_market_users(self, chain: str, controller_address: str, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/users/{chain}/{contoller_address}/users" + self._build_query(
            False,
            page=page,
            per_page=per_page
        )
        return self._execute_request(endpoint)

    def get_crvusd_user_stats(self, user: str):
        endpoint = f"crvusd/savings/{user}/stats"
        return self._execute_request(endpoint)

    def get_crvusd_user_events(self, user: str, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/savings/{user}/events" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_crvusd_events(self, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/savings/events" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_crvusd_yield(self, start: int, end: int, interval: str='day'):
        endpoint = f"crvusd/savings/yield" + self._build_query(False, start=start, end=end, interval=interval)
        return self._execute_request(endpoint)

    def get_crvusd_revenue(self, page: int=1, per_page: int=1000):
        endpoint = f"crvusd/savings/revenue" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_crvusd_stats(self):
        endpoint = f"crvusd/savings/statistics"
        return self._execute_request(endpoint)

    def get_crvusd_soft_liquidation_ratio(self, chain: str, controller_address: str, start: int=None, end: int=None):
        endpoint = f"crvusd/liquidations/{chain}/{controller_address}/soft_liquidation_ratio" + self._build_query(
            False,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)

    def get_crvusd_detailed_market_liquidation_history(self, chain: str, controller_address: str, start: int=None, end: int=None):
        endpoint = f"crvusd/liquidations/{chain}/{controller_address}/history/detailed" + self._build_query(
            False,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)
    
    def get_crvusd_aggregated_market_liquidation_history(self, chain: str, controller_address: str, start: int=None, end: int=None):
        endpoint = f"crvusd/liquidations/{chain}/{controller_address}/history/aggregated" + self._build_query(
            False,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)
    
    def get_crvusd_aggregated_liquidation_history(self, chain: str, start: int=None, end: int=None):
        endpoint = f"crvusd/liquidations/{chain}/history/aggregated" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_crvusd_market_liquidation_losses(self, chain: str, controller_address: str, start: int=None, end: int=None):
        endpoint = f"crvusd/liquidations/{chain}/{controller_address}/losses/history" + self._build_query(
            False,
            start=start,
            end=end
        )
        return self._execute_request(endpoint)

    def get_crvusd_market_health_distribution(self, chain: str, controller_address: str):
        endpoint = f"crvusd/liquidations/{chain}/{controller_address}/health/distribution"
        return self._execute_request(endpoint)

    def get_crvusd_market_cr_distribution(self, chain: str, controller_address: str):
        endpoint = f"crvusd/liquidations/{chain}/{contoller_address}/cr/distribution"
        return self._execute_request(endpoint)

    def get_crvusd_health_overview(self, chain: str, controller_address: str, fetch_on_chain: bool=False):
        endpoint = f"crvusd/liquidations/{chain}/{controller_address}/overview" + self._build_query(False, fetch_on_chain=fetch_on_chain)
        return self._execute_request(endpoint)

    def get_crvusd_losses_per_band_range(self, chain: str, controller_address: str, start: int=None, end: int=None, statistic: str="mean"):
        endpoint = f"crvusd/liquidations/{chain}/{controller_address}/losses_per_band_range" + self._build_query(
            False,
            start=start,
            end=end,
            statistic=statistic
        )
        return self._execute_request(endpoint)

    def get_crvusd_hard_liquidated_users(self, chain: str, controller_address: str, start: int=None, end: int=None):
        endpoint = f"crvusd/liquidations/{chain}/{controller_address}/hard/users" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_crvusd_hard_liquidation_total(self, chain: str, controller_address: str):
        endpoint = f"crvusd/liquidations/{chain}/{controller_address}/hard/total"
        return self._execute_request(endpoint)

    def get_gauges_overview(self):
        endpoint = f"dao/gauges/overview"
        return self._execute_request(endpoint)

    def get_votes_overview(self):
        endpoint = f"dao/votes/overview"
        return self._execute_request(endpoint)

    def get_user_gauge_votes(self, user: str):
        endpoint = f"dao/gauges/votes/user/{user}"
        return self._execute_request(endpoint)

    def get_user_proposal_votes(self, user: str, pagination: int=1000, page: int=1):
        endpoint = f"dao/proposals/votes/user/{user}" + self._build_query(False, pagination=pagination, page=page)
        return self._execute_request(endpoint)

    def get_gauge_for_pool(self, chain: str, pool: str):
        endpoint = f"dao/pools/{chain}/{pool}/gauge"
        return self._execute_request(endpoint)

    def get_gauge_for_market(self, chain: str, controller_address: str):
        endpoint = f"dao/lending/{chain}/{controller_address}/gauge"
        return self._execute_request(endpoint)

    def get_votes_for_gauge(self, gauge: str):
        endpoint = f"dao/gauges/{gauge}/votes"
        return self._execute_request(endpoint)

    def get_gauge_metadata(self, gauge: str):
        endpoint = f"dao/gauges/{gauge}/metadata"
        return self._execute_request(endpoint)

    def get_gauge_weight_history(self, gauge: str):
        endpoint = f"dao/gauges/{gauge}/weight_history"
        return self._execute_request(endpoint)

    def get_gauge_deployment(self, gauge: str):
        endpoint = f"dao/gauges/{gauge}/deployment"
        return self._execute_request(endpoint)

    def get_user_crv_locks(self, user: str):
        endpoint = f"dao/locks/{user}"
        return self._execute_request(endpoint)

    def get_daily_crv_lock_history(self, days_back: int):
        endpoint = f"dao/locks/daily/{days_back}"
        return self._execute_request(endpoint)

    def get_crv_supply_breakdown(self, days_back: int):
        endpoint = f"dao/supply/{days_back}"
        return self._execute_request(endpoint)

    def get_largest_lockers(self, pagination: int=1000, page: int=1):
        endpoint = f"dao/lockers" + self._build_query(False, pagination=pagination, page=page)
        return self._execute_request(endpoint)

    def get_proposals(self, search_string: str=None, pagination: int=1000, page: int=1, status_filter:str='all', type_filter: str='all'):
        endpoint = f"dao/proposals" + self._build_query(
            False,
            search_string=search_string,
            pagination=pagination,
            page=page,
            status_filter=status_filter,
            type_filter=type_filter
        )
        return self._execute_request(endpoint)

    def get_proposal(self, type_: str, vote_id: int):
        endpoint = f"dao/proposals/details/{type}/{vote_id}"
        return self._execute_request(endpoint)

    def get_fee_distributions(self, page: int=1, per_page: int=1000):
        endpoint = f"dao/fees/distributions" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_weekly_crvusd_fees(self, start: int=None, end: int=None):
        endpoint = f"dao/fees/crvusd/weekly" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_weekly_pool_fees(self, start: int=None, end: int=None):
        endpoint = f"dao/fees/pools/weekly" + self._build_query(False, start=start, end=end)
        return self._execute_request(endpoint)

    def get_pending_pool_fees(self, chain: str):
        endpoint = f"dao/fees/{chain}/pending"
        return self._execute_request(endpoint)

    def get_fee_settlements(self, prior_to: int):
        endpoint = f"dao/fees/settlements" + self._build_query(False, timestamp=prior_to)
        return self._execute_request(endpoint)

    def get_collected_fees(self):
        endpoint = f"dao/fees/collected"
        return self._execute_request(endpoint)

    def get_staged_fees(self):
        endpoint = f"dao/fees/staged"
        return self._execute_request(endpoint)

    def get_lending_market(self, chain: str, controller_address: str, fetch_on_chain: bool=False, agg: str='day'):
        endpoint = f"lending/markets/{chain}/{controller_address}/snapshots" + self._build_query(
            False,
            fetch_on_chain=fetch_on_chain,
            agg=agg
        )
        return self._execute_request(endpoint)

    def get_lending_market_loan_distribution(self, chain: str, controller_address: str):
        endpoint = f"lending/markets/{chain}/{controller_address}/loans/distribution"
        return self._execute_request(endpoint)

    def get_lending_market_llamma_events(self, chain: str, address: str, page: int=1, per_page: int=1000):
        endpoint = f"lending/llamma_events/{chain}/{address}" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)

    def get_lending_market_llamma_trades(self, chain: str, address: str, page: int=1, per_page: int=1000):
        endpoint = f"lending/llamma_trades/{chain}/{address}" + self._build_query(False, page=page, per_page=per_page)
        return self._execute_request(endpoint)
















