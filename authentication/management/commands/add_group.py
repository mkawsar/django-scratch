from typing import Any, Optional
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add user group'
    

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        groups = ['admin', 'manager', 'user']
        permissions = Permission.objects.all()
        print(permissions[0])
        # for group in groups:
        #     Group.objects.create(name = group)
        # return super().handle(*args, **options)
