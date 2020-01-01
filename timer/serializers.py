from rest_framework.serializers import ModelSerializer
from timer.models import Solution


class SolutionSerializer(ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'
