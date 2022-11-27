from django.contrib import admin
from testing.models import Test, Question, Option, Answer, PassedTest

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(PassedTest)
admin.site.register(Option)