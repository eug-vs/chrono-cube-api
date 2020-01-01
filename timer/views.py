from rest_framework.viewsets import ModelViewSet

from timer.models import Solution
from timer.serializers import SolutionSerializer


class SolutionViewSet(ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
