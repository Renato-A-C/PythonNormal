from django.core.management.base import BaseCommand
from django.contrib.auth.models import Funcionario, Permission

class Command(BaseCommand):
    help = 'Assign all permissions to superusers'

    def handle(self, *args, **options):
        all_permissions = Permission.objects.all()
        superusers = Funcionario.objects.filter(is_superuser=True)
        
        for user in superusers:
            user.user_permissions.set(all_permissions)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Assigned all permissions to superuser {user.username}'))
