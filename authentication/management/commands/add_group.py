from typing import Any, Optional
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

GROUPS = ['admin', 'manger', 'user']


class Command(BaseCommand):
    help = 'Add user group'

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        for group in GROUPS:
            Group.objects.get_or_create(name=group)
        return 'Added successfully'
