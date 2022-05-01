from text.models import TextModel
import pytest


def test_create_text_model(db):
    """
    It should create a TextModel object
    """
    TextModel.objects.create(content="Fake Text")
    assert TextModel.objects.count() == 1


def test_text_model_fields(db):
    """
    It should create a TextModel object
    """
    content = "Fake Text"
    TextModel.objects.create(content=content)
    text_obj = TextModel.objects.all().first()
    assert text_obj.content == content
