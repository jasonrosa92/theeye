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


class ErrorsLog(models.Model):
    """"
    Error log model
    """
    created = models.DateTimeField(auto_now_add=True)
    payload = models.TextField()
    errors = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.created.isoformat()

