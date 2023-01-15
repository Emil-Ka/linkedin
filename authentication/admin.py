from django.contrib import admin
from authentication.models import User
from import_export.admin import ExportActionMixin


class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'bio',
                    'role', 'is_active', 'is_staff', 'is_superuser')


admin.site.register(User, UserAdmin)
