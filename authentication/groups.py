from django.contrib.auth.models import Group
from authentication.roles import ROLE_CHOICES, USER, HR, ADMIN

user_group, created = Group.objects.get_or_create(name=ROLE_CHOICES[USER][1])
hr_group, created = Group.objects.get_or_create(name=ROLE_CHOICES[HR][1])
admin_group, created = Group.objects.get_or_create(name=ROLE_CHOICES[ADMIN][1])

groups_dict = {
    USER: user_group,
    HR: hr_group,
    ADMIN: admin_group,
}
