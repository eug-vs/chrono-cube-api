from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from timer.models import Solution
from timer.serializers import SolutionSerializer


class SolutionViewSet(ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=author__id', '=author__username']
