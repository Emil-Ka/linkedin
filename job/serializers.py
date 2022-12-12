from rest_framework import serializers
from job.models import Vacancy, Response, Response

class VacancySerializer(serializers.ModelSerializer):
  class Meta:
    model = Vacancy
    fields = ['id', 'title', 'company_name', 'salary', 'text', 'user']

  def validate(self, data):
    if data['salary'] is not None and data['salary'] <= 13026:
      raise serializers.ValidationError({'error': 'salary cannot be less than the minimum wage in the Russian Federation'})

    return data

class ResumeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Response
    fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Response
    fields = '__all__'