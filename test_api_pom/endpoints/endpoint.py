import allure

class Endpoint:
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Verifying response title is correct')
    def assert_response_title_is_correct(self, title):
        assert self.json['title'] == title

    @allure.step('Verifying response code is 200 or 201')
    def assert_response_code_is_200(self):
        assert self.response.status_code in [200, 201]

    @allure.step('Check that response error code is received')
    def assert_bad_request_code_is_not_200(self):
        assert self.response.status_code != 200