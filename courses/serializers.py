from rest_framework import serializers
from .models import Course

# Serializers translate database data to/from JSON


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')
