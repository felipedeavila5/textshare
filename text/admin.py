from django.contrib import admin
from .models import TextModel


@admin.register(TextModel)
class TextModelAdmin(admin.ModelAdmin):
    list_display = ("uuid", "content")
