import re
from django.core.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    DateTimeField,
)

from django.contrib.auth.models import User
from timer.models import Solution

from users.serializers import UserSerializer

result_pattern = re.compile('^\d{2}:\d{2}:\d{2}$')


class SolutionSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    date = DateTimeField(read_only=True)
    author_id = PrimaryKeyRelatedField(
        source='author',
        queryset=User.objects.all(),
        allow_null=True,
        write_only=True,
    )

    class Meta:
        model = Solution
        fields = ['id', 'result', 'author', 'date', 'author_id']

    def validate(self, attrs):
        if not result_pattern.match(attrs['result']):
            raise ValidationError('Result must match the format XX:XX:XX')
        return attrs
