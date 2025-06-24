import allure
import requests
from test_api_pom.endpoints.endpoint import Endpoint

class GetEndpointClass(Endpoint):


    @allure.step('Getting endpoint')
    def get__specific_endpoint(self, get_id, headers=None):
        headers = headers if headers else self.url
        self.response = requests.get(f'{self.url}/{get_id}', headers)
        self.json = self.response.json()
        print(f'Getting endpoint ID {get_id} response: ', self.response)
        print(f'Request {get_id} took {self.response.elapsed.total_seconds()} seconds: ')
        print('Generating full Allure request logs')
        self.log_response()
        return self.response
