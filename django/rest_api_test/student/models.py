from django.db import models

# Create your models here.

# 사용자 정의 모델
class Student(models.Model):
    # 모델 안에 추가하고싶은 정보 정의
    student_id = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()