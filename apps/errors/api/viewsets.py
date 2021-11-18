from rest_framework import viewsets
from .models import ErrorsLog
from .serializers import ErrorLogSerializer



class ErrorLogView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ErrorLogSerializer
    queryset = ErrorsLog.objects.all()
