from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from timer.models import Solution


class SolutionSerializer(ModelSerializer):
    author = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Solution
        fields = '__all__'
