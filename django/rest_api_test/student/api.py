from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class StudentList(APIView):
    def get(self, request):
        model = Student.objects.all()
        serializer = StudentSerializer(model, many=True)
        return Response(serializer.data)