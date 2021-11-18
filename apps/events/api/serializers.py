from django.utils import timezone
from rest_framework import serializers

from errors.models import EventUser


class EventUserSerializer(serializers.ModelSerializer):
    """
    Data Validation Serializer
    """

    class Meta:
        model = EventUser
        exclude = ['saved_date', ]

    def data_validator(self, value):
        """
        validates if the dictionary is valid and contains data
        """
        if value == '':
            raise serializers.ValidationError("The data is empty")
        try:
            dict(value)
        except ValueError:
            raise serializers.ValidationError("This collected data is invalid")

        return value

    def timestamp_validator(self, value):
        """
        time date validator (checks that the date is not greater than the current date)
        """
        if value > timezone.now():
            raise serializers.ValidationError("Timestamp is invalid")

        return value