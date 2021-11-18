from rest_framework import serializers

from .models import ErrorsLog


class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorsLog
        fields = '__all__'