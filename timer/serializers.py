import re
from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from timer.models import Solution


result_pattern = re.compile('^\d{2}:\d{2}:\d{2}$')


class SolutionSerializer(ModelSerializer):
    author = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Solution
        fields = '__all__'

    def validate(self, attrs):
        if not result_pattern.match(attrs['result']):
            raise ValidationError('Result must match the format XX:XX:XX')
        return attrs
