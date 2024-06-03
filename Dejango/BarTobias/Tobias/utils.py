from django.contrib.auth.models import Permission
def is_chefe(user):
    return user.groups.filter(name='Chefe').exists()

def is_funcionario(user):
    return user.groups.filter(name='Funcionario').exists()

def assign_all_permissions_to_superuser(user):
    if user.is_superuser:
        all_permissions = Permission.objects.all()
        user.user_permissions.set(all_permissions)
        user.save()