import pytest

TEST_DATA = [
    {"title": "My title", "body": "my body", "userId": 1},
    {"title": "My title2", "body": "my body2", "userId": 2}
]

NEGATIVE_DATA = [
    {"title": ["My title"], "body": "my body", "userId": 1},
    {"title": {"My title2": ''}, "body": "my body2", "userId": 2}
]

@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.assert_response_code_is_200()
    create_post_endpoint.assert_response_title_is_correct(data['title'])

@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_negative_data(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.assert_bad_request_code_is_not_200()
    create_post_endpoint.assert_response_title_is_correct(data['title'])

def test_put_a_post(update_post_endpoint):
    payload = {
        "title": "UpdatedTitle",
        "body": "UpdatedBody",
        "userId": 2
    }
    update_post_endpoint.make_changes_in_post(42, payload)
    update_post_endpoint.assert_response_title_is_correct(payload['title'])
    update_post_endpoint.assert_response_code_is_200()

