from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project, Tour, ProjectMember

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class ProjectMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectMember
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']
