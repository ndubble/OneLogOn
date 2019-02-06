from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from backend.server.models import Student
from backend.server.models import Admin
from backend.server.models import Company
from backend.server.models import SignIns
from backend.server.serializers import StudentSerializer
from backend.server.serializers import AdminSerializer
from backend.server.serializers import CompanySerializer
from backend.server.serializers import SignInsSerializer

def index(request):
    return render(request, 'index.html')

# /api/student
class StudentListCreate(generics.ListCreateAPIView):
    """
    Test student API endpoint
    """
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # test get
    def get(self, request):
        content = { 'message': 'mitch says hello' }
        return Response(content)

class AdminListCreate(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class CompanyListCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class SignInsListCreate(generics.ListCreateAPIView):
    queryset = SignIns.objects.all()
    serializer_class = SignInsSerializer
