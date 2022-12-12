from rest_framework.permissions import BasePermission
from rest_framework.exceptions import ValidationError, NotFound
from authentication.models import User
from authentication.roles import HR, ADMIN
from job.models import Vacancy, Response, Resume

class IsHR(BasePermission):
  def has_permission(self, request, view):
    email = request.user
    user = User.objects.get(email=email)

    return user.role == HR

class IsAdmin(BasePermission):
  def has_permission(self, request, view):
    email = request.user
    user = User.objects.get(email=email)

    return user.role == ADMIN

class IsThatVacancyCreator(BasePermission):
  def has_permission(self, request, view):
    email = request.user
    user = User.objects.get(email=email)

    vacancy_id = request.data.get('id')

    if vacancy_id is None:
      raise ValidationError({'error': 'vacancy id not found'})

    try:
      vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist:
      raise NotFound({'error': 'vacancy with this id was not found'})

    vacancy_creator_email = vacancy.user
    vacancy_creator_id = User.objects.get(email=vacancy_creator_email).id

    return vacancy_creator_id == user.id

class IsThatResumeCreator(BasePermission):
  def has_permission(self, request, view):
    email = request.user
    user = User.objects.get(email=email)

    resume_id = request.data.get('id')

    if resume_id is None:
        raise ValidationError({'error': 'resume id not found'})

    try:
      resume = Resume.objects.get(id=resume_id)
    except Resume.DoesNotExist:
      raise NotFound({'error': 'resume with this id was not found'})

    resume_creator_email = resume.user
    resume_creator_id = User.objects.get(email=resume_creator_email).id

    return resume_creator_id == user.id

class IsThatResponseCreator(BasePermission):
  def has_permission(self, request, view):
    email = request.user
    user = User.objects.get(email=email)

    response_id = request.data.get('id')

    if response_id is None:
        raise ValidationError({'error': 'response id not found'})

    try:
      response = Response.objects.get(id=response_id)
    except Response.DoesNotExist:
      raise NotFound({'error': 'response with this id was not found'})

    response_creator_email = response.user
    response_creator_id = User.objects.get(email=response_creator_email).id

    return response_creator_id == user.id

def is_that_vacancy_creator(request, vacancy_id):
  email = request.user
  user = User.objects.get(email=email)

  if vacancy_id is None:
      raise ValidationError({'error': 'vacancy id not found'})

  try:
    vacancy = Vacancy.objects.get(id=vacancy_id)
  except Vacancy.DoesNotExist:
    raise NotFound({'error': 'vacancy with this id was not found'})

  vacancy_creator_email = vacancy.user
  vacancy_creator_id = User.objects.get(email=vacancy_creator_email).id

  return vacancy_creator_id == user.id
