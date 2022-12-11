from rest_framework.viewsets import ModelViewSet
from testing.serializers import TestSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer, PassedTestSerializer
from testing.models import Test, Question, Option, Answer, PassedTest

class TestViewSet(ModelViewSet):
  queryset = Test.objects.all()
  serializer_class = TestSerializer

class QuestionViewSet(ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

  def get_queryset(self):
    queryset = Question.objects.all()
    test = self.request.query_params.get('test')

    if test is not None:
      queryset = queryset.filter(test=test)

    return queryset


class OptionViewSet(ModelViewSet):
  queryset = Option.objects.all()
  serializer_class = OptionSerializer

  def get_queryset(self):
    queryset = Option.objects.all()
    question = self.request.query_params.get('question')

    if question is not None:
      queryset = queryset.filter(question=question)

    return queryset

class AnswerViewSet(ModelViewSet):
  queryset = Answer.objects.all()
  serializer_class = AnswerSerializer

class PassedTestViewSet(ModelViewSet):
  queryset = PassedTest.objects.all()
  serializer_class = PassedTestSerializer


#  from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.core import serializers
# from testing.models import Test
# from testing.serializers import TestSerializer

# #objects.all - все записи, objects.get(id) - 1 запись по id
# # many=True - чтобы отобразились все записи

# @api_view()
# def test_view(request):
#   tests = Test.objects.all()
#   data = TestSerializer(instance=tests, many=True).data
#   return Response(data={'data': data})
