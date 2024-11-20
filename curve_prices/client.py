from curve_prices.chains_client import ChainsClient
from curve_prices.crvusd_client import CrvUsdClient
from curve_prices.dao_client import DaoClient
from curve_prices.health_client import HealthClient
from curve_prices.lending_client import LendingClient
from curve_prices.liquidity_client import LiquidityClient
from curve_prices.lp_ohlc_client import LpOhlcClient
from curve_prices.ohlc_client import OhlcClient
from curve_prices.pools_client import PoolsClient
from curve_prices.snapshots_client import SnapshotsClient
from curve_prices.trades_client import TradesClient
from curve_prices.usd_price_client import UsdPriceClient
from curve_prices.volume_client import VolumeClient

class CurvePricesClient:

    def __init__(self, base_url: str="https://prices.curve.fi/"):
        self.chains = ChainsClient(base_url)
        self.crvusd = CrvUsdClient(base_url)
        self.dao = DaoClient(base_url)
        self.health = HealthClient(base_url)
        self.lending = LendingClient(base_url)
        self.liquidity = LiquidityClient(base_url)
        self.lp_ohlc = LpOhlcClient(base_url)
        self.ohlc = OhlcClient(base_url)
        self.pools = PoolsClient(base_url)
        self.snapshots = SnapshotsClient(base_url)
        self.trades = TradesClient(base_url)
        self.usd_price = UsdPriceClient(base_url)
        self.volume = VolumeClient(base_url)







