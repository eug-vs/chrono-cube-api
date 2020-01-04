from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
