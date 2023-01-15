from django.db import models
from simple_history.models import HistoricalRecords
from authentication.models import User

class Test(models.Model):
  name = models.CharField(verbose_name='Название теста', max_length=255)
  cover = models.ImageField(verbose_name='Обложка', upload_to='covers')
  time = models.IntegerField(verbose_name='Время на выполнение')
  desc = models.TextField(verbose_name='Описание теста')

  history = HistoricalRecords()

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Тест'
    verbose_name_plural = 'Тесты'


class Question(models.Model):
  test = models.ForeignKey(Test, on_delete=models.CASCADE)
  text = models.TextField(verbose_name='Вопрос')
  photo = models.ImageField(verbose_name='Фото', upload_to='questions', blank=True)

  history = HistoricalRecords()

  def __str__(self):
    return self.text

  class Meta:
    verbose_name = 'Вопрос'
    verbose_name_plural = 'Вопросы'


class Option(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.TextField(verbose_name='Вариант ответа')

  history = HistoricalRecords()

  def __str__(self):
    return self.text

  class Meta:
    verbose_name = 'Вариант ответа'
    verbose_name_plural='Варианты ответов'


class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  option = models.ForeignKey(Option, on_delete=models.CASCADE)

  history = HistoricalRecords()

  def __str__(self):
    return str(self.id)

  class Meta:
    verbose_name = 'Ответ'
    verbose_name_plural = 'Ответы'


class PassedTest(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  test = models.ForeignKey(Test, related_name='tests', on_delete=models.CASCADE)
  result = models.FloatField(verbose_name='результат')

  history = HistoricalRecords()

  def __str__(self):
    return self.user.email + ' passed ' + self.test.name

  class Meta:
    verbose_name = 'Результат'
    verbose_name_plural = 'Результаты'

class Results(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  test = models.ForeignKey(Test, on_delete=models.CASCADE)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  option = models.ForeignKey(Option, on_delete=models.CASCADE)

  history = HistoricalRecords()

  def __str__(self):
    return 'the option_id' + self.option + 'chosen by' + self.user.email

  class Meta:
    verbose_name = 'Выбранный вариант ответа'
    verbose_name_plural = 'Выбранные варианты ответа'