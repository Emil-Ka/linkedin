from django.contrib import admin
from job.models import Vacancy, Response, Resume

admin.site.register(Vacancy)
admin.site.register(Response)
admin.site.register(Resume)