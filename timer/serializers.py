import re
from django.core.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    DateTimeField,
)

from django.contrib.auth.models import User
from timer.models import Solution


result_pattern = re.compile('^\d{2}:\d{2}:\d{2}$')


class SolutionSerializer(ModelSerializer):
    author = PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True)
    date = DateTimeField(read_only=True)

    class Meta:
        model = Solution
        fields = ['id', 'result', 'author', 'date']

    def validate(self, attrs):
        if not result_pattern.match(attrs['result']):
            raise ValidationError('Result must match the format XX:XX:XX')
        return attrs
