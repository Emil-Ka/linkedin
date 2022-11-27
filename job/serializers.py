from rest_framework import serializers
from job.models import Vacancy, Response, Resume

class VacancySerializer(serializers.ModelSerializer):
  class Meta:
    model = Vacancy
    fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Resume
    fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Response
    fields = '__all__'