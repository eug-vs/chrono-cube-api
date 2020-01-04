from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Solution(models.Model):
    result = models.CharField('Result', max_length=8)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.result} (Solution {self.id})'
