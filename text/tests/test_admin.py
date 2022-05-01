from django.contrib import admin
from text.models import TextModel


def test_registered_text_model():
    "The TextModel should be registered in admin"
    registered = [model for model, model_admin in admin.site._registry.items()]
    assert TextModel in registered
