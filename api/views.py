from rest_framework import generics
from .models import Student, Grade, UserProfile
# from .serializers import StudentSerializer, GradeSerializer

# class StudentListCreate(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class GradeListCreate(generics.ListCreateAPIView):
#     queryset = Grade.objects.all()
#     serializer_class = GradeSerializer


from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('email')
        password = request.data.get('password')
        user_profile = UserProfile.objects.filter(email=username).filter(password=password)
        if user_profile:
            
            return Response({'token': 'True'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

from .models import Certificate
from .serializers import CertificateSerializer
from django.shortcuts import get_object_or_404
class CertificateAPIView(APIView):
    def post(self, request):
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .serializers import CertificateSerializer

class CertificateDetailView(APIView):
    def get(self, request, student_id):
        certificate = get_object_or_404(Certificate, student_id=student_id)
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data)