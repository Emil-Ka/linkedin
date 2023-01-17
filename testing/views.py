from rest_framework.viewsets import ModelViewSet
from testing.serializers import TestSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer, PassedTestSerializer, ResultsSerializer
from testing.models import Test, Question, Option, Answer, PassedTest, Results
from authentication.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response as DjangoResponse
from rest_framework.decorators import action
from job.permissions import IsAdmin
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed

class TestViewSet(ModelViewSet):
  queryset = Test.objects.all()
  serializer_class = TestSerializer

  @action(methods=['POST'], detail=False, url_path='create', permission_classes=[IsAuthenticated & IsAdmin])
  def create_test(self, request):
    email = request.user
    user = User.objects.get(email=email)
    request.data['user'] = user.id

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return DjangoResponse(serializer.data)

  @action(methods=['DELETE'], detail=False, url_path=r'delete/(?P<test_id>.*)', permission_classes=[IsAuthenticated & IsAdmin])
  def delete_test(self, request, test_id):
    if test_id is None:
      raise ValidationError({'error': 'test id not found'})

    try:
      test = Test.objects.get(id=test_id)
    except Test.DoesNotExist:
      raise NotFound({'error': 'test with this id was not found'})

    test.delete()

    return DjangoResponse({'message': f'test with id #{test_id} was successfully deleted'})

  @action(methods=['PATCH'], detail=False, url_path='update', permission_classes=[IsAuthenticated & IsAdmin])
  def delete_test(self, request):
    test_id = request.data.get('id')

    if test_id is None:
      raise ValidationError({'error': 'test id not found'})

    try:
      test = Test.objects.get(id=test_id)
    except Test.DoesNotExist:
      raise NotFound({'error': 'test with this id was not found'})

    for key in request.data:
      if request.data.get(key) is not None:
        setattr(test, key, request.data.get(key))

    test.save()
    data = self.serializer_class(test).data

    return DjangoResponse(data)

class QuestionViewSet(ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

  def get_queryset(self):
    queryset = Question.objects.all()
    test = self.request.query_params.get('test')

    if test is not None:
      queryset = queryset.filter(test=test)

    return queryset

  @action(methods=['POST'], detail=False, url_path='create', permission_classes=[IsAuthenticated & IsAdmin])
  def create_question(self, request):
    email = request.user
    user = User.objects.get(email=email)
    request.data._mutable = True
    request.data['user'] = user.id

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return DjangoResponse(serializer.data)

  @action(methods=['DELETE'], detail=False, url_path=r'delete/(?P<question_id>.*)', permission_classes=[IsAuthenticated & IsAdmin])
  def delete_question(self, request, question_id):
    if question_id is None:
      raise ValidationError({'error': 'question id not found'})

    try:
      question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
      raise NotFound({'error': 'question with this id was not found'})

    question.delete()

    return DjangoResponse({'message': f'test with id #{question_id} was successfully deleted'})

  @action(methods=['PATCH'], detail=False, url_path='update', permission_classes=[IsAuthenticated & IsAdmin])
  def update_question(self, request):
    question_id = request.data.get('id')

    if question_id is None:
      raise ValidationError({'error': 'question id not found'})

    try:
      question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
      raise NotFound({'error': 'question with this id was not found'})

    for key in request.data:
      if request.data.get(key) is not None:
        setattr(question, key, request.data.get(key))

    question.save()
    data = self.serializer_class(question).data

    return DjangoResponse(data)

class OptionViewSet(ModelViewSet):
  queryset = Option.objects.all()
  serializer_class = OptionSerializer

  def get_queryset(self):
    queryset = Option.objects.all()
    question = self.request.query_params.get('question')

    if question is not None:
      queryset = queryset.filter(question=question)

    return queryset

  @action(methods=['POST'], detail=False, url_path='create', permission_classes=[IsAuthenticated & IsAdmin])
  def create_option(self, request):
    email = request.user
    user = User.objects.get(email=email)
    request.data['user'] = user.id

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return DjangoResponse(serializer.data)

  @action(methods=['DELETE'], detail=False, url_path=r'delete/(?P<option_id>.*)', permission_classes=[IsAuthenticated & IsAdmin])
  def delete_option(self, request, option_id):
    if option_id is None:
      raise ValidationError({'error': 'option id not found'})

    try:
      option = Option.objects.get(id=option_id)
    except Option.DoesNotExist:
      raise NotFound({'error': 'option with this id was not found'})

    option.delete()

    return DjangoResponse({'message': f'option with id #{option_id} was successfully deleted'})

  @action(methods=['PATCH'], detail=False, url_path='update', permission_classes=[IsAuthenticated & IsAdmin])
  def update_option(self, request):
    option_id = request.data.get('id')

    if option_id is None:
      raise ValidationError({'error': 'option id not found'})

    try:
      option = Option.objects.get(id=option_id)
    except Option.DoesNotExist:
      raise NotFound({'error': 'option with this id was not found'})

    for key in request.data:
      if request.data.get(key) is not None:
        setattr(option, key, request.data.get(key))

    option.save()
    data = self.serializer_class(option).data

    return DjangoResponse(data)

class AnswerViewSet(ModelViewSet):
  queryset = Answer.objects.all()
  serializer_class = AnswerSerializer

  def get_queryset(self):
    queryset = self.queryset
    test = self.request.query_params.get('test')

    if test is not None:
      queryset = queryset.filter(test=test)

    return queryset

  @action(methods=['POST'], detail=False, url_path='create', permission_classes=[IsAuthenticated & IsAdmin])
  def create_answer(self, request):
    email = request.user
    user = User.objects.get(email=email)
    request.data['user'] = user.id

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return DjangoResponse(serializer.data)

  @action(methods=['POST'], detail=False, url_path='check', permission_classes=[IsAuthenticated])
  def check_answer(self, request):
    email = request.user
    user = User.objects.get(email=email)
    user_id = getattr(user, 'id')
    score = 0
    count = len(request.data.keys())

    for key in request.data.keys():
      question_id = key
      user_option_id = request.data.get(key)

      try:
        answer = Answer.objects.get(question=question_id)
      except Answer.DoesNotExist:
        raise NotFound({'error': 'answer for this question was not found'})

      option_text = getattr(answer, 'option')
      option = Option.objects.get(text=option_text, question=question_id)
      option_id = getattr(option, 'id')

      if (user_option_id == str(option_id)):
        score += 1

      question = Question.objects.get(id=question_id)
      test_name = getattr(question, 'test')
      test = Test.objects.get(name=test_name)
      test_id = getattr(test, 'id')

      user_option = Option.objects.get(id=user_option_id)

      try:
        result = Results.objects.get(question=question_id, user=user_id)
        setattr(result, 'option', user_option)
        result.save()
      except Results.DoesNotExist:
        result_data = {
          'user': user_id,
          'option': user_option_id,
          'question': question_id,
          'test': test_id
        }

        resultSerializer = ResultsSerializer(data=result_data)
        resultSerializer.is_valid(raise_exception=True)
        resultSerializer.save()

    total = round(score / count * 100)

    try:
      passed_test = PassedTest.objects.get(user=user_id, test=test_id)
      setattr(passed_test, 'result', total)
      passed_test.save()
    except PassedTest.DoesNotExist:
      passed_test_data = {
        'user': user_id,
        'test': test_id,
        'result': total
      }
      passed_test_serializer = PassedTestSerializer(data=passed_test_data)
      passed_test_serializer.is_valid(raise_exception=True)
      passed_test_serializer.save()

    return DjangoResponse({'result': total})


  @action(methods=['DELETE'], detail=False, url_path=r'delete/(?P<answer_id>.*)', permission_classes=[IsAuthenticated & IsAdmin])
  def delete_answer(self, request, answer_id):
    if answer_id is None:
      raise ValidationError({'error': 'answer id not found'})

    try:
      answer = Answer.objects.get(id=answer_id)
    except Answer.DoesNotExist:
      raise NotFound({'error': 'answer with this id was not found'})

    answer.delete()

    return DjangoResponse({'message': f'answer with id #{answer_id} was successfully deleted'})

  @action(methods=['PATCH'], detail=False, url_path='update', permission_classes=[IsAuthenticated & IsAdmin])
  def update_answer(self, request):
    answer_id = request.data.get('id')
    question_id = request.data.get('question')
    option_id = request.data.get('option')

    if answer_id is None:
      raise ValidationError({'error': 'answer id not found'})

    try:
      answer = Answer.objects.get(id=answer_id)
    except Answer.DoesNotExist:
      raise NotFound({'error': 'answer with this id was not found'})

    try:
      option = Option.objects.get(id=option_id)
    except Option.DoesNotExist:
      raise NotFound({'error': 'option with this id was not found'})

    try:
      question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
      raise NotFound({'error': 'question with this id was not found'})

    setattr(answer, 'question', question)
    setattr(answer, 'option', option)

    answer.save()
    data = self.serializer_class(answer).data

    return DjangoResponse(data)

class PassedTestViewSet(ModelViewSet):
  queryset = PassedTest.objects.all()
  serializer_class = PassedTestSerializer

  def get_queryset(self):
    email = self.request.user
    user = User.objects.get(email=email)

    if user is None:
      raise AuthenticationFailed({'error': 'user is not find'})

    queryset = self.queryset.filter(user=user)

    return queryset

  @action(methods=['POST'], detail=False, url_path='create', permission_classes=[IsAuthenticated])
  def create_passed_test(self, request):
    email = request.user
    user = User.objects.get(email=email)
    request.data['user'] = user.id

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return DjangoResponse(serializer.data)

  @action(methods=['DELETE'], detail=False, url_path=r'delete/(?P<test_id>.*)', permission_classes=[IsAuthenticated & IsAdmin])
  def delete_passed_test(self, request, test_id):
    if test_id is None:
      raise ValidationError({'error': 'passed test id not found'})

    try:
      passed_test = PassedTest.objects.get(id=test_id)
    except PassedTest.DoesNotExist:
      raise NotFound({'error': 'passed test with this id was not found'})

    passed_test.delete()

    return DjangoResponse({'message': f'passed test with id #{test_id} was successfully deleted'})

  @action(methods=['PATCH'], detail=False, url_path='update', permission_classes=[IsAuthenticated])
  def update_passed_test(self, request):
    passed_id = request.data.get('id')

    if passed_id is None:
      raise ValidationError({'error': 'passed test id not found'})

    try:
      passed_test = PassedTest.objects.get(id=passed_id)
    except PassedTest.DoesNotExist:
      raise NotFound({'error': 'passed test with this id was not found'})

    for key in request.data:
      if request.data.get(key) is not None:
        setattr(passed_test, key, request.data.get(key))

    passed_test.save()
    data = self.serializer_class(passed_test).data

    return DjangoResponse(data)

class ResultsViewSet(ModelViewSet):
  queryset = Results.objects.all()
  serializer_class = ResultsSerializer

  def get_queryset(self):
    email = self.request.user
    user = User.objects.get(email=email)

    test_id = self.request.query_params.get('test')

    results = Results.objects.filter(user=getattr(user, 'id'), test=test_id)

    return results

  @action(methods=['PATCH'], detail=False, url_path='update', permission_classes=[IsAuthenticated])
  def create_results(self, request):
    email = request.user
    user = User.objects.get(email=email)

    try:
      result = Results.objects.get(question=request.data.get('question'), user=getattr(user, 'id'))
    except Results.DoesNotExist:
      raise NotFound({'error': 'result was not found'})

    option = Option.objects.get(id=request.data.get('option'))
    question = Question.objects.get(id=request.data.get('question'))

    setattr(result, 'question', question)
    setattr(result, 'option', option)

    result.save()

    return DjangoResponse({'message': 'success'})

  @action(methods=['DELETE'], detail=False, url_path=r'delete/(?P<result_id>.*)', permission_classes=[IsAuthenticated & IsAdmin])
  def delete_result(self, request, result_id):
    if result_id is None:
      raise ValidationError({'error': 'result id not found'})

    try:
      result = Results.objects.get(id=result_id)
    except PassedTest.DoesNotExist:
      raise NotFound({'error': 'result with this id was not found'})

    result.delete()

    return DjangoResponse({'message': f'result with id #{result_id} was successfully deleted'})



# from rest_framework.response import Response
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
