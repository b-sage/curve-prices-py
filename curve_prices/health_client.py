from curve_prices.client_core import ClientCore

class HealthClient(ClientCore):

    path = ''

    def ping(self):
        endpoint = 'ping'
        print(self.base_url + endpoint)
        return self._execute_request(endpoint)
