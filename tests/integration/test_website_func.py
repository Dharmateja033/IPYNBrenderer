import pytest
from IPYNBrenderer033.website import render_website
from IPYNBrenderer033.custom_exception import InvalidURLException


class TestRenderSite:
    URL_test_success_data = [
        ("http://pytorch.org", "successfully rendered website"),
        ("https://pytorch.org", "successfully rendered website"),
    ]

    URL_test_bad_data = [
        ("http://pytorch"),
        ("http//pytorch"),
        ("http:/pytorch"),
        ("http/pytorch"),
        ("http/pytorch"),
        ("pytorch.org"),
        ("http://asyef/"),
    ]

    @pytest.mark.parametrize("URL, response", URL_test_success_data)
    def test_render_site_success(self, URL, response):
        assert render_website(URL) == response

    @pytest.mark.parametrize("URL", URL_test_bad_data)
    def test_render_site_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_website(URL)
