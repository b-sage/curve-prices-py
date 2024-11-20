from curve_prices.endpoints import EndpointsCore

class HealthEndpoints(EndpointsCore):

    path = ''

    def ping(self):
        endpoint = 'ping'
        return self._execute_request(endpoint)
