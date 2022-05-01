from django.urls import path
from .viewsets import TextViewSet

app_name = "text"

urlpatterns = [
    path(
        "api/texts/",
        TextViewSet.as_view({"get": "list", "post": "create"}),
        name="texts",
    ),
    path(
        "api/texts/<uuid:uuid>",
        TextViewSet.as_view(
            {"get": "retrieve", "put": "update", "patch": "partial_update"}
        ),
        name="texts_details",
    ),
]
