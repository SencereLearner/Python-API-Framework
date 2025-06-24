import allure
from test_api_pom.endpoints.endpoint import Endpoint

class GetEndpointClass(Endpoint):


    @allure.step('Getting endpoint')
    def get_specific_endpoint(self, get_id):
        self.send_request('GET', self.url, get_id)
