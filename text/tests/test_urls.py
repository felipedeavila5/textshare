from django.urls import resolve
from text.viewsets import TextViewSet
from conftest import text


def test_url_path_api():
    """
    There should be a path to the text api
    """
    resolve("/text/api/texts/")


def test_resolve_textviewset():
    """
    There should be a viewset path for the text
    """
    response = resolve("/text/api/texts/")
    assert response.func.__name__ == TextViewSet.as_view({"get": "list"}).__name__


def test_url_path_api_details(db, text):
    """
    There should be a path to the text object
    """
    resolve("/text/api/texts/" + str(text.uuid))
