from django.test import Client
from rest_framework.test import APIClient
from rest_framework import status
from text.models import TextModel
from conftest import text, user
import pytest


def test_empty_list_texts(db, user):
    """
    Should return no text object
    """
    client = Client()
    client.force_login(user=user)
    response = client.get("/text/api/texts/")
    assert len(response.json()) == 0


def test_list_texts_auth(db, user):
    """
    Should list text objects when authenticated
    """
    client = Client()
    client.force_login(user=user)
    response = client.get("/text/api/texts/")
    assert response.status_code == status.HTTP_200_OK


def test_list_texts_not_auth(db):
    """
    Shouldn't allow list text objects when not authenticated
    """
    client = Client()
    response = client.get("/text/api/texts/")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_details_text_by_uuid(db, text):
    """
    Should show details of a text by uuid
    """
    client = Client()
    response = client.get("/text/api/texts/" + str(text.uuid))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize(
    "content, expected_status",
    [("", status.HTTP_201_CREATED), ("Fake Text Content", status.HTTP_201_CREATED)],
)
def test_create_text(db, content, expected_status):
    """
    Should create a text
    """
    client = Client()
    response = client.post("/text/api/texts/", {"content": content})
    assert response.status_code == expected_status
    assert TextModel.objects.first().content == content


def test_update_text(db, text):
    """
    Should update a text
    """
    fake_content = "Fake Text Content"
    client = APIClient()
    response = client.put(
        "/text/api/texts/" + str(text.uuid),
        {"content": fake_content},
    )
    assert TextModel.objects.first().content == fake_content
    assert response.status_code == status.HTTP_200_OK


def test_partial_update_text(db, text):
    """
    Should update partial a text
    """
    fake_content = "Fake Text Content"
    client = APIClient()
    response = client.patch(
        "/text/api/texts/" + str(text.uuid),
        {"content": fake_content},
    )
    assert response.status_code == status.HTTP_200_OK
    assert TextModel.objects.first().content == fake_content


def test_remove_text(db, text, user):
    """
    Should not allow delete a text
    """
    client = Client()
    response = client.delete("/text/api/texts/" + str(text.uuid))
    assert len(TextModel.objects.all()) > 0
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
