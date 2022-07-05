# serializers의 역할:
# 받아온 데이터를 보기 좋게 JSON형식으로 바꿔주는 역할

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'