import json

from celery import shared_task

from apps.events.api.serializers import EventUserSerializer
from apps.errors.models import ErrorsLog


@shared_task
def event_task(data):
    serializer = EventUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        errors = []
        for k,v in serializer.errors.items():
            errors.append(f'{k}: {",".join(v)}')

        ErrorsLog.objects.create(payload=json.dumps(data), error=','.join(errors))

