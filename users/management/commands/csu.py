from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@example.com")
        user.set_password("123qwe")
        user.is_active = True
        user.is_Staff = True
        user.is_superuser = True
        user.save()