from django.contrib import admin
from job.models import Vacancy, Response, Resume
from import_export.admin import ExportActionMixin

class VacancyAdmin(ExportActionMixin, admin.ModelAdmin):
  list_display = ('user', 'title', 'company_name', 'text', 'salary')

class ResumeAdmin(ExportActionMixin, admin.ModelAdmin):
  list_display = ('user', 'title', 'text', 'salary')

class ResponseAdmin(ExportActionMixin, admin.ModelAdmin):
  list_display = ('user', 'vacancy', 'resume')

admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Resume, ResumeAdmin)