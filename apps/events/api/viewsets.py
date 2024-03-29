from datetime import datetime
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response

from apps.events.models import EventUser
from .serializers import EventUserSerializer
from apps.events.tasks.events import event_task


class EventView(mixins.ListModelMixin,  viewsets.GenericViewSet):
    serializer_class = EventUserSerializer
    queryset = EventUser.objects.all()

    def create(self, request, *args, **kwargs):
        event_task.delay(request.data)
        return Response(status=status.HTTP_202_ACCEPTED)

    def get_queryset(self):
        """
        Customize method to filter by parameters
        """
        queryset = EventUser.objects.all()

        start_date = self.request.query_params.get('start_date')
        if start_date:
            start_date = datetime.fromisoformat(start_date)
            queryset = queryset.filter(timestamp__gte=start_date)

        end_date = self.request.query_params.get('end_date')
        if end_date:
            end_date = datetime.fromisoformat(end_date)
            queryset = queryset.filter(timestamp__lte=end_date)

        end_date = self.request.query_params.get('end_date')
        if end_date:
            end_date = datetime.fromisoformat(end_date)
            queryset = queryset.filter(timestamp__lte=end_date)

        session_id = self.request.query_params.get('session_id')
        if session_id:
            queryset = queryset.filter(session_id=session_id)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        return queryset
