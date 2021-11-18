from django.db import models


class ErrorsLog(models.Model):
    """"
    Error log model
    """
    created = models.DateTimeField(auto_now_add=True)
    payload = models.TextField()
    errors = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.created.isoformat()

