from model_bakery import baker
from django.test import Client
from django.contrib import auth
import pytest


@pytest.fixture
def text():
    return baker.make("text.TextModel")


@pytest.fixture
def user():
    return baker.make("auth.User")


@pytest.fixture
def user_anonymous():
    client = Client()
    user = auth.get_user(client)
    return user
