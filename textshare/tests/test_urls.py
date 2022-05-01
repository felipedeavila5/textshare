from django.urls import get_resolver


def test_app_text_in_urls():
    """
    The path to the text app should be in urlpatterns
    """
    apps_in_urls = [url_pattern.app_name for url_pattern in get_resolver().url_patterns]
    assert "text" in apps_in_urls
