from rest_framework import serializers
from testing.models import Test, Question, Option, Answer, PassedTest, Results

class TestSerializer(serializers.ModelSerializer):
  class Meta:
    model = Test
    fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Option
    fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = '__all__'

class PassedTestSerializer(serializers.ModelSerializer):
  class Meta:
    model = PassedTest
    fields = '__all__'

class ResultsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Results
    fields = '__all__'