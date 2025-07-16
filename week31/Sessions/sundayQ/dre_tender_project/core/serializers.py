from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Project, Tender


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    owned_by = UserSerializer(read_only = True)

    class Meta:
        models = Project
        fields = ['id', 'title', 'description', 'ceated_at', 'owned_by']

class TenderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Tender
        fields = ['id', 'user', 'projects', 'price', 'created_at']
        read_only_fields = ['created_at']