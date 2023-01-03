import logging
from typing import Any, Optional
from authentication.models import User
from django.core.management.base import BaseCommand

USERS = [
    {
        'name': 'admin',
        'email': 'admin@example.com',
        'password': '123456'
    },
    {
        'name': 'manager',
        'email': 'manager@example.com',
        'password': '123456'
    },
    {
        'name': 'user',
        'email': 'user@example.com',
        'password': '123456'
    }
]


class Command(BaseCommand):
    help = 'Add user'

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        for user in USERS:
            if user['name'] == 'admin':
                admin, created = User.objects.get_or_create(username=user['name'], first_name=user['name'],
                                                            email=user['email'], is_staff=True,
                                                            is_superuser=True)
                admin.set_password(user['password'])
                admin.save()
                admin.groups.add(1)
            elif user['name'] == 'manager':
                manager, created = User.objects.get_or_create(username=user['name'], first_name=user['name'],
                                                              email=user['email'], is_staff=True)
                manager.set_password(user['password'])
                manager.save()
                manager.groups.add(2)
            else:
                new_user, created = User.objects.get_or_create(username=user['name'], first_name=user['name'],
                                                               email=user['email'])
                new_user.set_password(user['password'])
                new_user.save()
                new_user.groups.add(3)

        return 'Added successfully'
