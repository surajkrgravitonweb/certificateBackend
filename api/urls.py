from django.urls import path
from .views import *

urlpatterns = [
    # path('students/', StudentListCreate.as_view(), name='student-list-create'),
    # path('grades/', GradeListCreate.as_view(), name='grade-list-create'),
    path('login/', LoginView.as_view(), name='api-login'),
     path('certificates/', CertificateAPIView.as_view()),
      path('certificates/<str:student_id>/', CertificateDetailView.as_view(), name='certificate-detail'),
]