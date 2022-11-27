from rest_framework.viewsets import ModelViewSet
from job.serializers import ResponseSerializer, VacancySerializer, ResumeSerializer
from job.models import Vacancy, Resume, Response

class VacancyViewSet(ModelViewSet):
  queryset = Vacancy.objects.all()
  serializer_class = VacancySerializer

class ResumeViewSet(ModelViewSet):
  queryset = Resume.objects.all()
  serializer_class = ResumeSerializer

class ResponseViewSet(ModelViewSet):
  queryset = Response.objects.all()
  serializer_class = ResponseSerializer