import allure
from test_api_pom.endpoints.endpoint import Endpoint

class UpdatePostClass(Endpoint):

    postId = 5

    @allure.step('Updating a post')
    def make_changes_in_post(self, requestId, payload, headers = None):
        self.send_request('PUT', self.url, requestId, payload, headers)