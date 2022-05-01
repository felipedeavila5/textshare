import uuid
from rest_framework.viewsets import ModelViewSet
from .models import TextModel
from .serializers import TextSerializer
from .permissions import NotListOrIsAuthenticated


class TextViewSet(ModelViewSet):
    queryset = TextModel.objects.all()
    serializer_class = TextSerializer
    lookup_field = "uuid"
    permission_classes = [NotListOrIsAuthenticated]
