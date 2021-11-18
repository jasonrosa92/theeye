from rest_framework import viewsets
from .serializers import ErrorLogSerializer
from apps.errors.models import ErrorsLog


class ErrorLogView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ErrorLogSerializer
    queryset = ErrorsLog.objects.all()
