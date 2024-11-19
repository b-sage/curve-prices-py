from curve_prices.client_core import ClientCore

class HealthClient(ClientCore):

    path = ''

    def ping(self):
        endpoint = 'ping/'
        return self._execute_request(endpoint)
