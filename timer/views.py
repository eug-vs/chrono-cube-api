from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from timer.models import Solution
from timer.serializers import SolutionSerializer


class SolutionViewSet(ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    filterset_fields = ['author']


class ScoreboardView(ListAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

    def list(self, request):
        best_solutions = []
        mapper = lambda solution: solution.result
        for user in User.objects.all():
            solutions = user.solution_set.all()
            if solutions:
                best = min(solutions, key=mapper)
                best_solutions.append(best)

        queryset = sorted(best_solutions, key=mapper)
        serializer = SolutionSerializer(queryset, many=True)
        return Response(serializer.data)
