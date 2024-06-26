from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Класс для создания суперюзера"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.ru',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()
