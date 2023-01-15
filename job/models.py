from django.db import models
from simple_history.models import HistoricalRecords
from authentication.models import User

class Resume(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=255, verbose_name='Заголовок резюме')
  text = models.TextField(verbose_name='Описание резюме')
  salary = models.FloatField(verbose_name='Зарплата', blank=True, null=True)

  history = HistoricalRecords()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Резюме'
    verbose_name_plural = 'Резюме'

class Vacancy(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=255, verbose_name='Заголовок вакансии')
  salary = models.FloatField(verbose_name='Зарплата', blank=True, null=True)
  company_name = models.CharField(max_length=255, verbose_name='Название компании')
  text = models.TextField(verbose_name='Описание вакансии')

  history = HistoricalRecords()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Вакансия'
    verbose_name_plural = 'Вакансии'

class Response(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
  resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

  history = HistoricalRecords()

  def __str__(self):
    return self.user.email + ' applied for ' + self.vacancy.title

  class Meta:
    verbose_name = 'Отклик'
    verbose_name_plural = 'Отклики'