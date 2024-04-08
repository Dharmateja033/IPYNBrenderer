import pytest
# from src.IPYNBrenderer.youtube import get_time_info
# from src.IPYNBrenderer.custom_exception import InvalidURLException

from IPYNBrenderer import get_time_info
from IPYNBrenderer.custom_exception import InvalidURLException

good_URL_data = [
    ("https://youtu.be/roO5VGxOw2s", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", 42),
]


URL_id_bad_data = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),  # exception
    ("https://www.youtube.com/watch?v==roO5VGxOw2s&t=22s"),
]


@pytest.mark.parametrize(
    "URL, response", good_URL_data
)  # This decorator tells pytest to run the test function multiple times, each time with different parameters specified in the good_URL_data list
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response


""" This test function verifies that the get_time_info function correctly raises an InvalidURLException 
    when provided with invalid YouTube URLs. It achieves this by using the pytest.raises context manager to check for the expected exception during the execution of the test."""


@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)
