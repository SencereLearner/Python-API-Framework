import pytest
from test_api_pom.endpoints.create_post import CreatePostClass
from test_api_pom.endpoints.update_endpoint import UpdatePostClass
from test_api_pom.endpoints.get_endpoint import GetEndpointClass

@pytest.fixture()
def create_post_endpoint_fixture():
    return CreatePostClass()

@pytest.fixture()
def update_post_endpoint_fixture():
    return UpdatePostClass()

@pytest.fixture()
def get_specific_endpoint_fixture():
    return GetEndpointClass()



