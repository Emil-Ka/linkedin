from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from authentication.models import User
from job.models import Vacancy
from authentication.serializers import UserSerializer
from job.pagination import Pagination
from job.permissions import IsHR, IsThatResponseCreator, IsThatVacancyCreator, IsAdmin, IsThatResumeCreator, is_that_vacancy_creator
from job.serializers import ResponseSerializer, VacancySerializer, ResumeSerializer
from job.models import Vacancy, Response, Resume
from rest_framework.response import Response as DjangoResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes

class VacancyViewSet(ModelViewSet):
  queryset = Vacancy.objects.all()
  serializer_class = VacancySerializer
  pagination_class = Pagination

  @action(methods=['POST'], detail=False, url_path='create', permission_classes=[IsAuthenticated & (IsHR | IsAdmin)])
  def create_vacancy(self, request):
    email = request.user
    user = User.objects.get(email=email)
    request.data['user'] = user.id

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return DjangoResponse(serializer.data)

  @action(methods=['DELETE'], detail=False, url_path='delete', permission_classes=[IsAuthenticated & (IsHR & IsThatVacancyCreator | IsAdmin)])
  def delete_vacancy(self, request):
    id = request.data.get('id')

    if id is None:
      raise ValidationError({'error': 'vacancy id not found'})

    vacancy = Vacancy.objects.get(id=id)
    vacancy.delete()

    return DjangoResponse({'message': f'vacancy with id #{id} was successfully deleted'})

  @action(methods=['PATCH'], detail=False, url_path='update', permission_classes=[IsAuthenticated & (IsHR & IsThatVacancyCreator | IsAdmin)])
  def update_vacancy(self, request):
    id = request.data.get('id')

    if id is None:
      raise ValidationError({'error': 'vacancy id not found'})

    try:
      vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
      raise NotFound({'error': 'vacancy with this id was not found'})

    for key in request.data:
      if request.data.get(key) is not None:
        setattr(vacancy, key, request.data.get(key))

    vacancy.save()
    data = self.serializer_class(vacancy).data

    return DjangoResponse(data)



class ResumeViewSet(ModelViewSet):
  queryset = Resume.objects.all()
  serializer_class = ResumeSerializer
  pagination_class = Pagination

  def get_queryset(self):
    email = self.request.user

    if not email.is_authenticated:
      raise AuthenticationFailed({'error': 'unauthorized user'})

    user = User.objects.get(email=email)

    queryset = self.queryset.filter(user=user)

    return queryset

  @action(methods=['POST'], detail=False, url_path='create', permission_classes=[IsAuthenticated])
  def create_resume(self, request):
    email = request.user
    user = User.objects.get(email=email)
    request.data['user'] = user.id

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return DjangoResponse(serializer.data)

  @action(methods=['DELETE'], detail=False, url_path=r'delete/(?P<id>.*)', permission_classes=[IsAuthenticated & (IsThatResumeCreator | IsAdmin)])
  def delete_resume(self, request, id):
    id = request.data.get('id')

    if id is None:
      raise ValidationError({'error': 'resume id not found'})

    resume = Resume.objects.get(id=id)
    resume.delete()

    return DjangoResponse({'message': f'resume with id #{id} was successfully deleted'})

  @action(methods=['PATCH'], detail=False, url_path='update', permission_classes=[IsAuthenticated & (IsThatResumeCreator | IsAdmin)])
  def update_resume(self, request):
    id = request.data.get('id')

    if id is None:
      raise ValidationError({'error': 'resume id not found'})

    try:
      resume = Resume.objects.get(id=id)
    except Resume.DoesNotExist:
      raise NotFound({'error': 'resume with this id was not found'})

    for key in request.data:
      if request.data.get(key) is not None:
        setattr(resume, key, request.data.get(key))

    resume.save()
    data = self.serializer_class(resume).data

    return DjangoResponse(data)


class ResponseViewSet(ModelViewSet):
  queryset = Response.objects.all()
  serializer_class = ResponseSerializer
  pagination_class = Pagination

  def get_queryset(self):
    email = self.request.user

    if not email.is_authenticated:
      raise AuthenticationFailed({'error': 'unauthorized user'})

    user = User.objects.get(email=email)
    queryset = self.queryset.filter(user=user)

    return queryset

  @action(methods=['GET'], detail=False, url_path=r'by_vacancy/(?P<vacancy_id>.*)', permission_classes=[IsAuthenticated & IsHR])
  def show_by_vacncy(self, request, vacancy_id):
    if not is_that_vacancy_creator(request, vacancy_id):
      raise AuthenticationFailed({'error': 'you are not the creator of this vacancy'})

    queryset = self.queryset.filter(vacancy=vacancy_id)
    print(queryset)

    return DjangoResponse({'responses': list(queryset.values())})

  @action(methods=['POST'], detail=False, url_path='create', permission_classes=[IsAuthenticated])
  def create_response(self, request):
    email = request.user
    user = User.objects.get(email=email)
    request.data['user'] = user.id

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return DjangoResponse(serializer.data)

  @action(methods=['DELETE'], detail=False, url_path='delete', permission_classes=[IsAuthenticated & (IsThatResponseCreator | IsAdmin)])
  def delete_resume(self, request):
    id = request.data.get('id')

    if id is None:
      raise ValidationError({'error': 'response id not found'})

    response = Response.objects.get(id=id)
    response.delete()

    return DjangoResponse({'message': f'response with id #{id} was successfully deleted'})