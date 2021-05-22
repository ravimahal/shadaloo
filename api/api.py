from rest_framework import viewsets, permissions
from .serializers import UnitSerializer
from units.models import Unit

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [
        permissions.AllowAny
    ]
