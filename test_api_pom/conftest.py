import pytest
import allure
from test_api_pom.endpoints.create_post import CreatePostClass
from test_api_pom.endpoints.update_endpoint import UpdatePostClass

@pytest.fixture()
def create_post_endpoint():
    return CreatePostClass()

@pytest.fixture()
def update_post_endpoint():
    return UpdatePostClass()



