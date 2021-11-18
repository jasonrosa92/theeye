from django.db import models


class EventUser(models.Model):
    """
    Model of user actions
    """
    session_id = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    saved_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

