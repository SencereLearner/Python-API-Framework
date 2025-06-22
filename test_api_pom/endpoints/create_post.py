import requests
import allure
from test_api_pom.endpoints.endpoint import Endpoint

class CreatePostClass(Endpoint):
# another approach is to use __init__ and pass data so upon class initialization all the data will be passed automatically
# And instead of using decorator: test_post_a_post(create_post_endpoint): I would have to create object of
# a class: create_post_endpoint = CreatePostClass()

    @allure.step('Creating a new post')
    def create_new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        response = requests.post(self.url, json=payload, headers=headers)
        self.json = response.json()
        return self.response

    @allure.step('Check that 400 error received')
    def assert_bad_request(self):
        assert self.response.status_code == 400

