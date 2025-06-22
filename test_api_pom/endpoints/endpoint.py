import allure

class Endpoint:
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Verifying response title is correct')
    def assert_response_title_is_correct(self, title):
        assert self.json['title'] == title