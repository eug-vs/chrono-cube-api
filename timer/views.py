from rest_framework.viewsets import ModelViewSet

from timer.models import Solution
from timer.serializers import SolutionSerializer


class SolutionViewSet(ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    filterset_fields = ['author']

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(author=None if user.is_anonymous else user)
