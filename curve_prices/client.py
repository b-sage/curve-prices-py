from curve_prices.endpoints import (
    ChainsEndpoints,
    CrvUsdEndpoints,
    DaoEndpoints,
    HealthEndpoints,
    LendingEndpoints,
    LiquidityEndpoints,
    LpOhlcEndpoints,
    OhlcEndpoints,
    PoolsEndpoints,
    SnapshotsEndpoints,
    TradesEndpoints,
    UsdPriceEndpoints,
    VolumeEndpoints
)

class CurvePricesClient:

    def __init__(self, base_url: str="https://prices.curve.fi/"):
        self.chains = ChainsEndpoints(base_url)
        self.crvusd = CrvUsdEndpoints(base_url)
        self.dao = DaoEndpoints(base_url)
        self.health = HealthEndpoints(base_url)
        self.lending = LendingEndpoints(base_url)
        self.liquidity = LiquidityEndpoints(base_url)
        self.lp_ohlc = LpOhlcEndpoints(base_url)
        self.ohlc = OhlcEndpoints(base_url)
        self.pools = PoolsEndpoints(base_url)
        self.snapshots = SnapshotsEndpoints(base_url)
        self.trades = TradesEndpoints(base_url)
        self.usd_price = UsdPriceEndpoints(base_url)
        self.volume = VolumeEndpoints(base_url)







