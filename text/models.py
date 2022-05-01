from django.db import models
import uuid


class TextModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    content = models.CharField(max_length=65000, blank=True)
