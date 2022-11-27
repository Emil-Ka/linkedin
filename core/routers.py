from rest_framework.routers import DefaultRouter
from testing.views import TestViewSet, QuestionViewSet, OptionViewSet, AnswerViewSet, PassedTestViewSet
from job.views import VacancyViewSet, ResumeViewSet, ResponseViewSet
from authentication.views import UserViewSet

router = DefaultRouter()

router.register('tests', TestViewSet)
router.register('questions', QuestionViewSet)
router.register('options', OptionViewSet)
router.register('answers', AnswerViewSet)
router.register('passed_tests', PassedTestViewSet)
router.register('vacancies', VacancyViewSet)
router.register('resumes', ResumeViewSet)
router.register('responses', ResponseViewSet)
router.register('auth', UserViewSet)